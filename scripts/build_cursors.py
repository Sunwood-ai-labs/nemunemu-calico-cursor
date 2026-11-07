#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
"""Build Windows .cur, .ani, and animated GIF files from v2 sprite sheets.

Extracts 8 frames (4x2 grid) from each high-resolution sprite sheet in
`assets/sprites/`, removes low-alpha background noise, tightly crops around
the union bounding box of all 8 frames so the cursor fills the canvas maximally,
and generates:
  - `cursors/` (default 96x96 large cursor set)
  - `cursors/128x128/` (128x128 extra-large cursor set)
  - `cursors/96x96/` (96x96 large cursor set)
  - `cursors/64x64/` (64x64 medium cursor set)
  - `cursors/48x48/` (48x48 compact cursor set)
  - `cursors/32x32/` (32x32 classic cursor set)
  - `assets/gif/*.gif` and `assets/preview/hotspot-guide.png`

Use `--check` to validate existing `.cur` and `.ani` files (including Win32
`LoadCursorFromFileW` verification when running on Windows).
"""

from __future__ import annotations

import argparse
import ctypes
import shutil
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parent.parent
SPRITES_DIR = REPO_ROOT / "assets" / "sprites"
GIF_DIR = REPO_ROOT / "assets" / "gif"
PREVIEW_DIR = REPO_ROOT / "assets" / "preview"
CURSORS_DIR = REPO_ROOT / "cursors"
DOCS_PUBLIC_ASSETS = REPO_ROOT / "docs" / "public" / "assets"


@dataclass(frozen=True)
class CursorSpec:
    role: str
    filename_stem: str
    source_sheet: str
    output_gif: str
    label: str
    win_reg_key: str
    crop_box: tuple[int, int, int, int]  # (x0, y0, x1, y1) inside each 443.5x443.5 cell
    hotspots: dict[int, tuple[int, int]]


CURSOR_SPECS: tuple[CursorSpec, ...] = (
    CursorSpec(
        role="normal",
        filename_stem="nemunemu_normal",
        source_sheet="01_normal_sheet.png",
        output_gif="01_normal_64.gif",
        label="Normal Select (Arrow)",
        win_reg_key="Arrow",
        crop_box=(60, 38, 60 + 367, 38 + 367),
        hotspots={
            128: (5, 8),
            96: (3, 6),
            64: (2, 4),
            48: (2, 3),
            32: (1, 2),
        },
    ),
    CursorSpec(
        role="link",
        filename_stem="nemunemu_link",
        source_sheet="02_link_sheet.png",
        output_gif="02_link_64.gif",
        label="Link Select (Hand)",
        win_reg_key="Hand",
        crop_box=(32, 22, 32 + 395, 22 + 395),
        hotspots={
            128: (39, 2),
            96: (29, 1),
            64: (19, 1),
            48: (14, 1),
            32: (10, 0),
        },
    ),
    CursorSpec(
        role="text",
        filename_stem="nemunemu_text",
        source_sheet="03_text_sheet.png",
        output_gif="03_text_64.gif",
        label="Text Select (IBeam)",
        win_reg_key="IBeam",
        crop_box=(84, 62, 84 + 357, 62 + 357),
        hotspots={
            128: (16, 60),
            96: (12, 45),
            64: (8, 30),
            48: (6, 22),
            32: (4, 15),
        },
    ),
    CursorSpec(
        role="busy",
        filename_stem="nemunemu_busy",
        source_sheet="04_busy_sheet.png",
        output_gif="04_busy_64.gif",
        label="Busy (Wait)",
        win_reg_key="Wait",
        crop_box=(51, 52, 51 + 340, 52 + 340),
        hotspots={
            128: (64, 64),
            96: (48, 48),
            64: (32, 32),
            48: (24, 24),
            32: (16, 16),
        },
    ),
    CursorSpec(
        role="working",
        filename_stem="nemunemu_working",
        source_sheet="04_busy_sheet.png",
        output_gif="04_busy_64.gif",
        label="Working in Background (AppStarting)",
        win_reg_key="AppStarting",
        crop_box=(51, 52, 51 + 340, 52 + 340),
        hotspots={
            128: (64, 64),
            96: (48, 48),
            64: (32, 32),
            48: (24, 24),
            32: (16, 16),
        },
    ),
)

SIZES: tuple[tuple[int, Path], ...] = (
    (96, CURSORS_DIR),  # Default root cursors/ uses large 96x96
    (128, CURSORS_DIR / "128x128"),
    (96, CURSORS_DIR / "96x96"),
    (64, CURSORS_DIR / "64x64"),
    (48, CURSORS_DIR / "48x48"),
    (32, CURSORS_DIR / "32x32"),
)


def clean_rgba_alpha(img: Image.Image, threshold: int = 128) -> Image.Image:
    """Zero out low-alpha background noise (< threshold) and harden opaque pixels."""
    rgba = img.convert("RGBA")
    raw = bytearray(rgba.tobytes())
    for i in range(0, len(raw), 4):
        if raw[i + 3] < threshold:
            raw[i] = 0
            raw[i + 1] = 0
            raw[i + 2] = 0
            raw[i + 3] = 0
        else:
            raw[i + 3] = 255
    return Image.frombytes("RGBA", rgba.size, bytes(raw))


def extract_sheet_frames(sheet_path: Path, crop_box: tuple[int, int, int, int]) -> list[Image.Image]:
    """Slice a 4x2 sprite sheet into 8 tightly-cropped, alpha-cleaned RGBA frames."""
    with Image.open(sheet_path) as sheet:
        cleaned = clean_rgba_alpha(sheet, threshold=128)
        w, h = cleaned.size
        cw = w / 4.0
        ch = h / 2.0
        cx0, cy0, cx1, cy1 = crop_box
        frames: list[Image.Image] = []
        for row in range(2):
            for col in range(4):
                ox = int(round(col * cw))
                oy = int(round(row * ch))
                cell = cleaned.crop((ox, oy, ox + int(round(cw)), oy + int(round(ch))))
                cropped = cell.crop((cx0, cy0, cx1, cy1))
                frames.append(cropped)
        return frames


def resize_cursor_frame(frame: Image.Image, target_size: int) -> Image.Image:
    """Resize a high-res cropped RGBA frame to target_size with crisp outlines."""
    resized = frame.resize((target_size, target_size), Image.Resampling.LANCZOS)
    return clean_rgba_alpha(resized, threshold=96)


def save_transparent_gif(frames: list[Image.Image], out_path: Path, duration_ms: int = 160) -> None:
    """Save RGBA frames as an animated transparent GIF."""
    pal_frames: list[Image.Image] = []
    for frame in frames:
        alpha = frame.getchannel("A")
        mask = Image.eval(alpha, lambda a: 255 if a < 128 else 0)
        pal = frame.convert("RGB").quantize(colors=255, method=Image.Quantize.FASTOCTREE)
        pal.paste(255, mask)
        pal_frames.append(pal)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pal_frames[0].save(
        out_path,
        save_all=True,
        append_images=pal_frames[1:],
        duration=duration_ms,
        loop=0,
        transparency=255,
        disposal=2,
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


def generate_hotspot_guide(extracted_cache: dict[str, list[Image.Image]]) -> Path:
    """Generate `assets/preview/hotspot-guide.png` showing hotspots on all 4 v2 designs."""
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PREVIEW_DIR / "hotspot-guide.png"

    unique_specs = [s for s in CURSOR_SPECS if s.role != "working"]
    card_w, card_h = 285, 380
    padding = 24
    header_h = 76
    canvas_w = padding * 2 + card_w * len(unique_specs) + padding * (len(unique_specs) - 1)
    canvas_h = header_h + card_h + padding * 2

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (248, 250, 249, 255))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    draw.text(
        (padding, 20),
        "Nemunemu Calico Cursor v2 - Tight-Cropped Hotspot Guide (128 / 96 / 64 / 48 / 32)",
        fill=(32, 48, 42, 255),
        font=font,
    )
    draw.text(
        (padding, 42),
        "Red crosshair marks the active click/point coordinate (hotspot_x, hotspot_y) across all 8 animation frames.",
        fill=(88, 108, 100, 255),
        font=font,
    )

    scale = 2  # 96 * 2 = 192x192 preview box
    box_size = 96 * scale

    for idx, spec in enumerate(unique_specs):
        card_x = padding + idx * (card_w + padding)
        card_y = header_h

        draw.rounded_rectangle(
            [card_x, card_y, card_x + card_w, card_y + card_h],
            radius=12,
            fill=(255, 255, 255, 255),
            outline=(210, 225, 218, 255),
            width=2,
        )

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

        frame96 = resize_cursor_frame(extracted_cache[spec.source_sheet][0], 96)
        enlarged = frame96.resize((box_size, box_size), Image.Resampling.NEAREST)
        canvas.paste(enlarged, (bx0, by0), enlarged)

        draw.rectangle(
            [bx0, by0, bx0 + box_size, by0 + box_size],
            outline=(180, 200, 190, 255),
            width=1,
        )

        hx, hy = spec.hotspots[96]
        px = bx0 + hx * scale + scale // 2
        py = by0 + hy * scale + scale // 2
        draw.line([(px - 14, py), (px + 14, py)], fill=(230, 35, 50, 255), width=2)
        draw.line([(px, py - 14), (px, py + 14)], fill=(230, 35, 50, 255), width=2)
        draw.ellipse(
            [px - 4, py - 4, px + 4, py + 4],
            outline=(255, 255, 255, 255),
            fill=(230, 35, 50, 255),
        )

        ty = by0 + box_size + 14
        draw.text((card_x + 16, ty), spec.label, fill=(24, 36, 32, 255), font=font)
        draw.text(
            (card_x + 16, ty + 20),
            f"File: {spec.filename_stem}.ani / .cur",
            fill=(70, 90, 82, 255),
            font=font,
        )
        h128 = spec.hotspots[128]
        h96 = spec.hotspots[96]
        h64 = spec.hotspots[64]
        h48 = spec.hotspots[48]
        h32 = spec.hotspots[32]
        draw.text(
            (card_x + 16, ty + 40),
            f"96x96 (Default): ({h96[0]}, {h96[1]})",
            fill=(200, 30, 45, 255),
            font=font,
        )
        draw.text(
            (card_x + 16, ty + 58),
            f"128x128: ({h128[0]}, {h128[1]}) | 64x64: ({h64[0]}, {h64[1]})",
            fill=(70, 90, 82, 255),
            font=font,
        )
        draw.text(
            (card_x + 16, ty + 76),
            f"48x48: ({h48[0]}, {h48[1]}) | 32x32: ({h32[0]}, {h32[1]})",
            fill=(70, 90, 82, 255),
            font=font,
        )
        if spec.role == "busy":
            draw.text(
                (card_x + 16, ty + 96),
                "(Also used for nemunemu_working)",
                fill=(100, 120, 112, 255),
                font=font,
            )

    canvas.save(out_path)
    return out_path


def build_all() -> list[Path]:
    """Extract v2 sprite sheets, build GIF previews, and generate all .ani/.cur sets."""
    generated: list[Path] = []
    extracted_cache: dict[str, list[Image.Image]] = {}

    for spec in CURSOR_SPECS:
        if spec.source_sheet not in extracted_cache:
            sheet_path = SPRITES_DIR / spec.source_sheet
            if not sheet_path.exists():
                raise FileNotFoundError(f"Missing sprite sheet: {sheet_path}")
            extracted_cache[spec.source_sheet] = extract_sheet_frames(sheet_path, spec.crop_box)

    # 1. Generate animated GIFs in assets/gif/
    GIF_DIR.mkdir(parents=True, exist_ok=True)
    for spec in CURSOR_SPECS:
        if spec.role == "working":
            continue
        raw_frames = extracted_cache[spec.source_sheet]
        gif64_frames = [resize_cursor_frame(f, 64) for f in raw_frames]
        gif_path = GIF_DIR / spec.output_gif
        save_transparent_gif(gif64_frames, gif_path, duration_ms=160)
        generated.append(gif_path)

    # Also generate 256x256 calico cat hero GIF from normal stretching animation
    hero256_frames = [resize_cursor_frame(f, 256) for f in extracted_cache["01_normal_sheet.png"]]
    hero256_path = GIF_DIR / "04_calico_cat_256.gif"
    save_transparent_gif(hero256_frames, hero256_path, duration_ms=160)
    generated.append(hero256_path)

    # 2. Generate .ani and .cur across all 6 target directories
    for size, out_dir in SIZES:
        out_dir.mkdir(parents=True, exist_ok=True)
        for spec in CURSOR_SPECS:
            raw_frames = extracted_cache[spec.source_sheet]
            sized_frames = [resize_cursor_frame(f, size) for f in raw_frames]
            hx, hy = spec.hotspots[size]

            ani_path = out_dir / f"{spec.filename_stem}.ani"
            cur_path = out_dir / f"{spec.filename_stem}.cur"

            ani_path.write_bytes(frames_to_ani_bytes(sized_frames, hx, hy, jiffies=10))
            cur_path.write_bytes(image_to_cur_bytes(sized_frames[0], hx, hy))
            generated.extend((ani_path, cur_path))

    # 3. Generate hotspot guide
    guide_path = generate_hotspot_guide(extracted_cache)
    generated.append(guide_path)

    # 4. Sync to docs/public/assets if present
    if DOCS_PUBLIC_ASSETS.exists():
        (DOCS_PUBLIC_ASSETS / "gif").mkdir(parents=True, exist_ok=True)
        (DOCS_PUBLIC_ASSETS / "preview").mkdir(parents=True, exist_ok=True)
        for g in GIF_DIR.glob("*.gif"):
            shutil.copy2(g, DOCS_PUBLIC_ASSETS / "gif" / g.name)
        shutil.copy2(guide_path, DOCS_PUBLIC_ASSETS / "preview" / guide_path.name)

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
    """Verify all 60 cursor files structurally and via Win32 LoadCursorFromFileW if on Windows."""
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
        f"[OK] Verified {checked_count} cursor files (.ani & .cur across default/128/96/64/48/32) "
        f"{'with Win32 LoadCursorFromFileW ' if is_win else ''}and hotspot-guide.png."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or validate Nemunemu Calico v2 cursors.")
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
