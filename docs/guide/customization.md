# 🛠️ Build & Customization

All binary cursor files in `cursors/` are generated reproducibly from the 8-frame transparent GIF assets in `assets/gif/` using `scripts/build_cursors.py`.

---

## ⚙️ How `scripts/build_cursors.py` Works

Windows animated cursors (`.ani`) and static cursors (`.cur`) use specific binary container structures:

1. **32-bit BGRA `.cur` Frame Encoding**:
   - Each frame is converted to bottom-up `32-bit BGRA` pixel data preceded by a 40-byte `BITMAPINFOHEADER` (`biHeight = height * 2`, `biBitCount = 32`) and followed by a 1-bpp AND mask padded to 32-bit DWORD boundaries.
   - The `ICONDIR` (`idType = 2` for cursor) and `ICONDIRENTRY` embed the exact `(wXHotspot, wYHotspot)` coordinates for each target resolution (`64×64`, `48×48`, and `32×32`).
2. **RIFF `ACON` `.ani` Container Assembly**:
   - Wraps all 8 `.cur` frames inside a `RIFF` (`ACON`) container with an `anih` header (`cFrames = 8`, `cSteps = 8`, `iDispRate = 10` jiffies ≈ `166.7ms`, `fl = AF_ICON`), a `rate` chunk, a `seq ` chunk, and a `fram` (`icon`) list.

---

## 🔄 Rebuilding Cursors

Use `uv run` to execute the builder script without manually managing virtual environments:

```powershell
# Rebuild all 64x64, 48x48, and 32x32 cursors and hotspot-guide.png
uv run scripts/build_cursors.py
```

---

## ✅ Verifying Binary Integrity (`--check`)

The `--check` flag validates that every `.ani` and `.cur` file across `cursors/`, `cursors/48x48/`, and `cursors/32x32/` exists, has valid RIFF `ACON` / `ICONDIR` headers, contains 8 frames, and matches the expected `(X, Y)` hotspot coordinates:

```powershell
uv run scripts/build_cursors.py --check
```

---

## ✏️ Customizing Hotspots or Frame Timing

If you edit the artwork in `assets/gif/` or want to adjust click hotspots or animation speed:

1. Open `scripts/build_cursors.py`.
2. Update the hotspot coordinates or `jiffies` timing (`1 jiffy = 1/60 sec`).
3. Run `uv run scripts/build_cursors.py` followed by `uv run scripts/build_cursors.py --check`.
4. Inspect `assets/preview/hotspot-guide.png` to confirm the red crosshairs align with your pointer tips.
