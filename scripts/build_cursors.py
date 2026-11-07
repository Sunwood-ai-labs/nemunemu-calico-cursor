#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
"""Build Windows .cur and .ani cursor files from animated GIF assets.

Generates 64x64 (default), 48x48, and 32x32 cursor sets along with a visual
hotspot guide image (`assets/preview/hotspot-guide.png`).
Use `--check` to validate existing `.cur` and `.ani` files (including Win32
`LoadCursorFromFileW` verification when running on Windows).
"""

from __future__ import annotations

import argparse
import ctypes
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parent.parent
GIF_DIR = REPO_ROOT / "assets" / "gif"
PREVIEW_DIR = REPO_ROOT / "assets" / "preview"
CURSORS_DIR = REPO_ROOT / "cursors"


@dataclass(frozen=True)
class CursorSpec:
    role: str
    filename_stem: str
    source_gif: str
    label: str
    win_reg_key: str
    hotspots: dict[int, tuple[int, int]]


CURSOR_SPECS: tuple[CursorSpec, ...] = (
    CursorSpec(
        role="normal",
        filename_stem="nemunemu_normal",
        source_gif="01_normal_64.gif",
        label="Normal Select (Arrow)",
        win_reg_key="Arrow",
        hotspots={64: (11, 9), 48: (8, 7), 32: (6, 5)},
    ),
    CursorSpec(
        role="link",
        filename_stem="nemunemu_link",
        source_gif="02_link_64.gif",
        label="Link Select (Hand)",
        win_reg_key="Hand",
        hotspots={64: (21, 6), 48: (16, 5), 32: (11, 3)},
    ),
    CursorSpec(
        role="text",
        filename_stem="nemunemu_text",
        source_gif="03_text_64.gif",
        label="Text Select (IBeam)",
        win_reg_key="IBeam",
        hotspots={64: (18, 32), 48: (14, 24), 32: (9, 16)},
    ),
    CursorSpec(
        role="busy",
        filename_stem="nemunemu_busy",
        source_gif="04_busy_64.gif",
        label="Busy (Wait)",
        win_reg_key="Wait",
        hotspots={64: (32, 32), 48: (24, 24), 32: (16, 16)},
    ),
    CursorSpec(
        role="working",
        filename_stem="nemunemu_working",
        source_gif="04_busy_64.gif",
        label="Working in Background (AppStarting)",
        win_reg_key="AppStarting",
        hotspots={64: (32, 32), 48: (24, 24), 32: (16, 16)},
    ),
)

SIZES: tuple[tuple[int, Path], ...] = (
    (64, CURSORS_DIR),
    (48, CURSORS_DIR / "48x48"),
    (32, CURSORS_DIR / "32x32"),
)


def image_to_cur_bytes(img: Image.Image, hotspot_x: int, hotspot_y: int) -> bytes:
    """Encode an RGBA PIL Image as a standard Windows .cur binary (32-bit BGRA DIB)."""
    rgba = img.convert("RGBA")
    width, height = rgba.size
    if not (1 <= width <= 256 and 1 <= height <= 256):
        raise ValueError(f"Unsupported cursor dimensions: {width}x{height}")

    raw_rgba = rgba.tobytes()
    xor_rows = bytearray()
    and_rows = bytearray()
    and_stride = ((width + 31) // 32) * 4

    # DIB rows are stored bottom-up (from height - 1 down to 0)
    for y in range(height - 1, -1, -1):
        row_offset = y * width * 4
        and_row = bytearray(and_stride)
        for x in range(width):
            px = row_offset + x * 4
            r = raw_rgba[px]
            g = raw_rgba[px + 1]
            b = raw_rgba[px + 2]
            a = raw_rgba[px + 3]
            xor_rows.extend((b, g, r, a))
            if a == 0:
                byte_idx = x // 8
                bit_idx = 7 - (x % 8)
                and_row[byte_idx] |= 1 << bit_idx
        and_rows.extend(and_row)

    bmi_header = struct.pack(
        "<IIIHHIIIIII",
        40,  # biSize
        width,  # biWidth
        height * 2,  # biHeight (includes XOR + AND masks)
        1,  # biPlanes
        32,  # biBitCount (32-bit BGRA)
        0,  # biCompression (BI_RGB)
        len(xor_rows) + len(and_rows),  # biSizeImage
        0,  # biXPelsPerMeter
        0,  # biYPelsPerMeter
        0,  # biClrUsed
        0,  # biClrImportant
    )
    dib_data = bmi_header + bytes(xor_rows) + bytes(and_rows)

    b_width = 0 if width == 256 else width
    b_height = 0 if height == 256 else height

    icon_dir = struct.pack("<HHH", 0, 2, 1)  # Reserved=0, Type=2 (CUR), Count=1
    dir_entry = struct.pack(
        "<BBBBHHII",
        b_width,
        b_height,
        0,  # bColorCount
        0,  # bReserved
        hotspot_x,  # wPlanes = hotspot X for CUR
        hotspot_y,  # wBitCount = hotspot Y for CUR
        len(dib_data),  # dwBytesInRes
        6 + 16,  # dwImageOffset
    )
    return icon_dir + dir_entry + dib_data


def make_riff_chunk(fourcc: bytes, payload: bytes) -> bytes:
    """Create a 2-byte word-aligned RIFF chunk."""
    if len(fourcc) != 4:
        raise ValueError(f"Invalid FourCC: {fourcc!r}")
    pad = b"\x00" if (len(payload) % 2 == 1) else b""
    return fourcc + struct.pack("<I", len(payload)) + payload + pad


def frames_to_ani_bytes(
    frames: list[Image.Image],
    hotspot_x: int,
    hotspot_y: int,
    jiffies: int = 10,
) -> bytes:
    """Encode a list of RGBA frames into a Windows RIFF ACON (.ani) binary."""
    if not frames:
        raise ValueError("At least one frame is required to build .ani")

    n_frames = len(frames)
    # anih structure (36 bytes):
    # cbSize, cFrames, cSteps, cx, cy, cBitCount, cPlanes, jiffies, fl (AF_ICON=0x1)
    anih_payload = struct.pack(
        "<IIIIIIIII",
        36,
        n_frames,
        n_frames,
        0,
        0,
        0,
        0,
        jiffies,
        0x00000001,
    )
    anih_chunk = make_riff_chunk(b"anih", anih_payload)

    icon_chunks = bytearray()
    for frame in frames:
        cur_bytes = image_to_cur_bytes(frame, hotspot_x, hotspot_y)
        icon_chunks.extend(make_riff_chunk(b"icon", cur_bytes))

    fram_list = make_riff_chunk(b"LIST", b"fram" + bytes(icon_chunks))
    acon_payload = b"ACON" + anih_chunk + fram_list
    return make_riff_chunk(b"RIFF", acon_payload)


def load_gif_frames(gif_path: Path, target_size: int) -> list[Image.Image]:
    """Extract all frames from an animated GIF as RGBA images at target_size."""
    frames: list[Image.Image] = []
    with Image.open(gif_path) as im:
        n_frames = getattr(im, "n_frames", 1)
        for idx in range(n_frames):
            im.seek(idx)
            rgba = im.convert("RGBA")
            if rgba.size != (target_size, target_size):
                rgba = rgba.resize(
                    (target_size, target_size),
                    Image.Resampling.NEAREST,
                )
            frames.append(rgba)
    return frames


def generate_hotspot_guide() -> Path:
    """Generate `assets/preview/hotspot-guide.png` showing hotspots on all 4 designs."""
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PREVIEW_DIR / "hotspot-guide.png"

    # Unique visual designs (normal, link, text, busy)
    unique_specs = [s for s in CURSOR_SPECS if s.role != "working"]
    card_w, card_h = 280, 360
    padding = 24
    header_h = 76
    canvas_w = padding * 2 + card_w * len(unique_specs) + padding * (len(unique_specs) - 1)
    canvas_h = header_h + card_h + padding * 2

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (248, 250, 249, 255))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    # Title banner
    draw.text(
        (padding, 20),
        "Nemunemu Calico Cursor - Hotspot Reference Guide (64x64 / 48x48 / 32x32)",
        fill=(32, 48, 42, 255),
        font=font,
    )
    draw.text(
        (padding, 42),
        "Red crosshair marks the active click/point coordinate (hotspot_x, hotspot_y) verified across all 8 animation frames.",
        fill=(88, 108, 100, 255),
        font=font,
    )

    scale = 3  # 64 * 3 = 192x192 preview box
    box_size = 64 * scale

    for idx, spec in enumerate(unique_specs):
        card_x = padding + idx * (card_w + padding)
        card_y = header_h

        # Card background
        draw.rounded_rectangle(
            [card_x, card_y, card_x + card_w, card_y + card_h],
            radius=12,
            fill=(255, 255, 255, 255),
            outline=(210, 225, 218, 255),
            width=2,
        )

        # Checkerboard inside preview area
        bx0 = card_x + (card_w - box_size) // 2
        by0 = card_y + 16
        cell = 12
        for cy in range(0, box_size, cell):
            for cx in range(0, box_size, cell):
                is_even = ((cx // cell) + (cy // cell)) % 2 == 0
                c = (242, 245, 244, 255) if is_even else (228, 234, 231, 255)
                draw.rectangle(
                    [bx0 + cx, by0 + cy, bx0 + cx + cell - 1, by0 + cy + cell - 1],
                    fill=c,
                )

        # Paste enlarged Frame 0
        frames = load_gif_frames(GIF_DIR / spec.source_gif, 64)
        enlarged = frames[0].resize((box_size, box_size), Image.Resampling.NEAREST)
        canvas.paste(enlarged, (bx0, by0), enlarged)

        # Draw border around preview box
        draw.rectangle(
            [bx0, by0, bx0 + box_size, by0 + box_size],
            outline=(180, 200, 190, 255),
            width=1,
        )

        # Draw hotspot crosshair
        hx, hy = spec.hotspots[64]
        px = bx0 + hx * scale + scale // 2
        py = by0 + hy * scale + scale // 2
        draw.line([(px - 14, py), (px + 14, py)], fill=(230, 35, 50, 255), width=2)
        draw.line([(px, py - 14), (px, py + 14)], fill=(230, 35, 50, 255), width=2)
        draw.ellipse(
            [px - 4, py - 4, px + 4, py + 4],
            outline=(255, 255, 255, 255),
            fill=(230, 35, 50, 255),
        )

        # Text metadata
        ty = by0 + box_size + 16
        draw.text((card_x + 18, ty), spec.label, fill=(24, 36, 32, 255), font=font)
        draw.text(
            (card_x + 18, ty + 22),
            f"File: {spec.filename_stem}.ani / .cur",
            fill=(70, 90, 82, 255),
            font=font,
        )
        h64 = spec.hotspots[64]
        h48 = spec.hotspots[48]
        h32 = spec.hotspots[32]
        draw.text(
            (card_x + 18, ty + 44),
            f"64x64 Hotspot: ({h64[0]}, {h64[1]})",
            fill=(200, 30, 45, 255),
            font=font,
        )
        draw.text(
            (card_x + 18, ty + 64),
            f"48x48 Hotspot: ({h48[0]}, {h48[1]})",
            fill=(70, 90, 82, 255),
            font=font,
        )
        draw.text(
            (card_x + 18, ty + 84),
            f"32x32 Hotspot: ({h32[0]}, {h32[1]})",
            fill=(70, 90, 82, 255),
            font=font,
        )
        if spec.role == "busy":
            draw.text(
                (card_x + 18, ty + 104),
                "(Also used for nemunemu_working)",
                fill=(100, 120, 112, 255),
                font=font,
            )

    canvas.save(out_path)
    return out_path


def build_all() -> list[Path]:
    """Generate all .ani and .cur files across 64x64, 48x48, and 32x32."""
    generated: list[Path] = []
    for size, out_dir in SIZES:
        out_dir.mkdir(parents=True, exist_ok=True)
        for spec in CURSOR_SPECS:
            gif_path = GIF_DIR / spec.source_gif
            if not gif_path.exists():
                raise FileNotFoundError(f"Missing source GIF: {gif_path}")

            frames = load_gif_frames(gif_path, size)
            hx, hy = spec.hotspots[size]

            ani_path = out_dir / f"{spec.filename_stem}.ani"
            cur_path = out_dir / f"{spec.filename_stem}.cur"

            ani_path.write_bytes(frames_to_ani_bytes(frames, hx, hy, jiffies=10))
            cur_path.write_bytes(image_to_cur_bytes(frames[0], hx, hy))

            generated.extend((ani_path, cur_path))

    guide_path = generate_hotspot_guide()
    generated.append(guide_path)
    return generated


def verify_cur_bytes(data: bytes, expected_size: int, expected_hotspot: tuple[int, int]) -> None:
    """Validate binary structure of a .cur buffer."""
    if len(data) < 62:
        raise ValueError(f".cur buffer too small ({len(data)} bytes)")
    reserved, ico_type, count = struct.unpack_from("<HHH", data, 0)
    if (reserved, ico_type, count) != (0, 2, 1):
        raise ValueError(f"Invalid CUR header: {(reserved, ico_type, count)}")
    b_w, b_h, _, _, hx, hy, bytes_in_res, offset = struct.unpack_from("<BBBBHHII", data, 6)
    actual_w = 256 if b_w == 0 else b_w
    actual_h = 256 if b_h == 0 else b_h
    if (actual_w, actual_h) != (expected_size, expected_size):
        raise ValueError(f"CUR size mismatch: got {actual_w}x{actual_h}, expected {expected_size}")
    if (hx, hy) != expected_hotspot:
        raise ValueError(f"CUR hotspot mismatch: got {(hx, hy)}, expected {expected_hotspot}")
    if offset + bytes_in_res != len(data):
        raise ValueError("CUR resource size does not match file length")


def verify_ani_bytes(data: bytes, expected_size: int, expected_hotspot: tuple[int, int]) -> None:
    """Validate binary structure of a RIFF ACON (.ani) file."""
    if len(data) < 64 or data[:4] != b"RIFF" or data[8:12] != b"ACON":
        raise ValueError("Invalid RIFF ACON header")
    riff_size = struct.unpack_from("<I", data, 4)[0]
    if riff_size + 8 != len(data):
        raise ValueError(f"RIFF size mismatch: header says {riff_size + 8}, actual {len(data)}")
    if data[12:16] != b"anih":
        raise ValueError("Missing anih chunk")
    cb_size, c_frames, c_steps, _, _, _, _, jiffies, fl = struct.unpack_from("<IIIIIIIII", data, 20)
    if cb_size != 36 or c_frames != 8 or c_steps != 8 or jiffies != 10 or fl != 1:
        raise ValueError(f"Unexpected anih values: cbSize={cb_size}, frames={c_frames}, fl={fl}")
    # Verify first embedded icon chunk
    list_pos = 20 + 36
    if data[list_pos : list_pos + 4] != b"LIST" or data[list_pos + 8 : list_pos + 12] != b"fram":
        raise ValueError("Missing LIST fram chunk")
    icon_pos = list_pos + 12
    if data[icon_pos : icon_pos + 4] != b"icon":
        raise ValueError("Missing first icon chunk")
    icon_len = struct.unpack_from("<I", data, icon_pos + 4)[0]
    icon_data = data[icon_pos + 8 : icon_pos + 8 + icon_len]
    verify_cur_bytes(icon_data, expected_size, expected_hotspot)


def check_all() -> None:
    """Verify all 30 cursor files structurally and via Win32 LoadCursorFromFileW if on Windows."""
    is_win = sys.platform == "win32"
    load_cursor = None
    destroy_cursor = None
    if is_win:
        user32 = ctypes.windll.user32
        load_cursor = user32.LoadCursorFromFileW
        load_cursor.argtypes = [ctypes.c_wchar_p]
        load_cursor.restype = ctypes.c_void_p
        destroy_cursor = user32.DestroyCursor
        destroy_cursor.argtypes = [ctypes.c_void_p]
        destroy_cursor.restype = ctypes.c_int

    checked_count = 0
    for size, out_dir in SIZES:
        for spec in CURSOR_SPECS:
            hx, hy = spec.hotspots[size]
            ani_path = out_dir / f"{spec.filename_stem}.ani"
            cur_path = out_dir / f"{spec.filename_stem}.cur"

            for path, is_ani in ((ani_path, True), (cur_path, False)):
                if not path.exists():
                    raise FileNotFoundError(f"Missing cursor file: {path}")
                raw = path.read_bytes()
                if is_ani:
                    verify_ani_bytes(raw, size, (hx, hy))
                else:
                    verify_cur_bytes(raw, size, (hx, hy))

                if load_cursor is not None and destroy_cursor is not None:
                    handle = load_cursor(str(path))
                    if not handle:
                        raise RuntimeError(f"Win32 LoadCursorFromFileW failed for {path}")
                    destroy_cursor(handle)

                checked_count += 1

    guide_path = PREVIEW_DIR / "hotspot-guide.png"
    if not guide_path.exists():
        raise FileNotFoundError(f"Missing hotspot guide: {guide_path}")

    print(
        f"[OK] Verified {checked_count} cursor files (.ani & .cur across 64/48/32) "
        f"{'with Win32 LoadCursorFromFileW ' if is_win else ''}and hotspot-guide.png."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or validate Nemunemu Calico cursors.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate existing .ani/.cur files without rebuilding.",
    )
    args = parser.parse_args()

    if args.check:
        check_all()
        return 0

    generated = build_all()
    print(f"Generated {len(generated)} files in {REPO_ROOT}")
    check_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
