# 🛠️ Build & Customization

All 120 binary cursor files in `cursors/` and preview GIFs in `assets/gif/` are generated reproducibly from the 10 high-resolution 4×2 PNG sprite sheets in `assets/sprites/` using `scripts/build_cursors.py`.

---

## ⚙️ How `scripts/build_cursors.py` Works

1. **Sprite Sheet Normalization, Slicing, Alpha Cleansing & Tight Cropping**:
   - Normalizes each 4×2 sprite sheet (`assets/sprites/01_normal_sheet.png` .. `10_move_sheet.png`) from `1774×887` to `1776×888` so every frame cell is an exact `444×444` square across all 8 frames.
   - Removes low-alpha background noise (`alpha < 128 -> 0`) and crops tightly around the 8-frame union bounding box (`crop_box`) so the cursor fills the canvas maximally without wasted margins.
2. **32-bit BGRA `.cur` Frame Encoding**:
   - Converts each frame to bottom-up `32-bit BGRA` pixel data preceded by a 40-byte `BITMAPINFOHEADER` (`biHeight = height * 2`, `biBitCount = 32`) and followed by a 1-bpp AND mask padded to 32-bit DWORD boundaries.
   - Embeds the exact `(wXHotspot, wYHotspot)` coordinates for each of the 10 roles across all 5 target resolutions (`128×128`, `96×96`, `64×64`, `48×48`, and `32×32`).
3. **RIFF `ACON` `.ani` Container Assembly**:
   - Wraps all 8 `.cur` frames inside a `RIFF` (`ACON`) container with an `anih` header (`cFrames = 8`, `cSteps = 8`, `jiffies = 10` ≈ `166.7ms`, `fl = AF_ICON`) and `LIST` (`fram` / `icon`) chunks.

---

## 🔄 Rebuilding Cursors

Use `uv run` to execute the builder script without manually managing virtual environments:

```powershell
# Rebuild all 128/96/64/48/32 cursors (120 files), GIF previews, and hotspot-guide.png
uv run scripts/build_cursors.py
```

---

## ✅ Verifying Binary Integrity (`--check`)

The `--check` flag validates that all 120 `.ani` and `.cur` files (10 roles × 2 formats × 6 directories: `cursors/` 96×96 default, `cursors/128x128/`, `cursors/96x96/`, `cursors/64x64/`, `cursors/48x48/`, and `cursors/32x32/`) exist, have valid RIFF `ACON` / `ICONDIR` headers, match the expected `(X, Y)` hotspot coordinates, and load cleanly via Win32 `LoadCursorFromFileW`:

```powershell
uv run scripts/build_cursors.py --check
```

---

## ✏️ Customizing Hotspots or Frame Timing

If you edit the sprite sheets in `assets/sprites/` or want to adjust click hotspots or animation speed:

1. Open `scripts/build_cursors.py`.
2. Update `crop_box`, `hotspots`, or `jiffies` timing (`1 jiffy = 1/60 sec`).
3. Run `uv run scripts/build_cursors.py` followed by `uv run scripts/build_cursors.py --check`.
4. Inspect `assets/preview/hotspot-guide.png` to confirm the red crosshairs align with your pointer tips across all 10 cursor cards.
