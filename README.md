<div align="center">
  <img src="./assets/header.svg" alt="Nemunemu Calico Cursor Banner" width="800" />

  <h1>🐾 Nemunemu Calico Cursor (v2)</h1>

  <p><strong>A sleepy calico cat &amp; mint pointer animated cursor theme for Windows 10 / 11</strong></p>

  <p>
    <a href="https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/nemunemu-calico-cursor/ci.yml?branch=main&amp;label=CI&amp;logo=github" alt="CI Status" /></a>
    <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/"><img src="https://img.shields.io/badge/Docs-VitePress-38B2AC?logo=vitepress&amp;logoColor=white" alt="Documentation" /></a>
    <img src="https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6?logo=windows&amp;logoColor=white" alt="Windows 10 / 11" />
    <img src="https://img.shields.io/badge/Format-32--bit%20BGRA%20.ani%20%2F%20.cur-4A3B32" alt="32-bit BGRA .ani / .cur" />
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-DD6B20.svg" alt="MIT License" /></a>
  </p>

  <p>
    <strong>English</strong> | <a href="./README.ja.md">日本語</a> | <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/">Documentation</a>
  </p>
</div>

---

## ✨ Overview

**Nemunemu Calico Cursor** (`ねむねむ三毛ネコ`) is an animated Windows mouse cursor theme featuring a sleepy calico cat stretching, yawning, waving its paw, and rolling beside a crisp mint-colored pointer. Every cursor is crafted as an **8-frame (~160ms per frame)** loop with full alpha transparency (`32-bit BGRA`) and tight bounding-box cropping in both animated (`.ani`) and static (`.cur`) formats.

<div align="center">
  <img src="./assets/gif/04_calico_cat_256.gif" alt="Nemunemu Calico Cat Mascot Preview (256x256)" width="160" />
</div>

- **4 Expressive v2 Cursor Designs Covering 5 Windows Roles**: Normal Select (`Arrow` — stretching & yawning), Link Select (`Hand` — waking & paw-waving), Text Select (`IBeam` — vertical stretching), and Busy / Working (`Wait` & `AppStarting` — rolling inside an 8-segment rotating ring).
- **5 Multi-DPI Size Variants (`128` / `96` Default / `64` / `48` / `32`)**: Tightly cropped around the 8-frame union bounding box so the calico cat fills the cursor canvas without wasted margins.
- **Automatic OS Cursor Size Enlargement (`SPI_SETCURSORSIZE`)**: Windows defaults to shrinking custom cursors to `32×32` (`CursorBaseSize = 32`). `install.ps1` automatically updates `CursorBaseSize`, `Accessibility\CursorSize`, and invokes Win32 `SystemParametersInfo(SPI_SETCURSORSIZE)` so your cursor renders at its full large size (`96×96` by default, or `128×128`) immediately.
- **Pixel-Accurate Hotspots & Safe Rollback**: Click hotspots are strictly aligned to the functional arrow tip, finger tip, I-beam shaft center, or spinner center. `uninstall.ps1` restores both your original cursors and your original `32px` OS cursor size from `backup-cursors.json`.

---

## 🎨 Cursor Gallery & Hotspot Coordinates

### Animated Cursor Previews

| Preview | Cursor Name | Windows Role (`Registry`) | Animated / Static Files | v2 Animation Description |
| :---: | :--- | :--- | :--- | :--- |
| <img src="./assets/gif/01_normal_64.gif" alt="Normal Select" width="64" /> | **Normal Select** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | A sleepy calico cat stretching its paws and yawning beside a crisp mint arrow pointer. |
| <img src="./assets/gif/02_link_64.gif" alt="Link Select" width="64" /> | **Link Select** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | A pointing hand with a mint cuff while the calico cat wakes up and waves its paw. |
| <img src="./assets/gif/03_text_64.gif" alt="Text Select" width="64" /> | **Text Select** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | The calico cat stretching up along a mint I-beam (click axis strictly aligned to the I-beam shaft). |
| <img src="./assets/gif/04_busy_64.gif" alt="Busy / Working" width="64" /> | **Busy / Working** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani`<br>`nemunemu_busy.cur`<br>`nemunemu_working.cur` | The calico cat rolling and stretching inside an 8-segment rotating mint capsule ring. |

### Hotspot Verification & Coordinate Table

<div align="center">
  <img src="./assets/preview/hotspot-guide.png" alt="Hotspot Verification Guide" width="680" />
</div>

| Cursor Role | Sprite Sheet (4×2 Grid) | `128×128` | `96×96` (Default) | `64×64` | `48×48` | `32×32` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Normal Select (`Arrow`)** | `assets/sprites/01_normal_sheet.png` | `(5, 8)` | **`(3, 6)`** | `(2, 4)` | `(2, 3)` | `(1, 2)` |
| **Link Select (`Hand`)** | `assets/sprites/02_link_sheet.png` | `(39, 2)` | **`(29, 1)`** | `(19, 1)` | `(14, 1)` | `(10, 0)` |
| **Text Select (`IBeam`)** | `assets/sprites/03_text_sheet.png` | `(16, 60)` | **`(12, 45)`** | `(8, 30)` | `(6, 22)` | `(4, 15)` |
| **Busy / Working (`Wait`, `AppStarting`)** | `assets/sprites/04_busy_sheet.png` | `(64, 64)` | **`(48, 48)`** | `(32, 32)` | `(24, 24)` | `(16, 16)` |

---

## 🚀 Quick Start (Installation)

### Method 1: One-Command PowerShell Install (Recommended)

Run `install.ps1` from PowerShell in the repository root. It copies the cursor files to `%LOCALAPPDATA%\Cursors\NemunemuCalico`, backs up your previous cursor paths and `CursorBaseSize` to `backup-cursors.json`, and immediately activates both the new cursor size (`SPI_SETCURSORSIZE`) and cursor scheme (`SPI_SETCURSORS`) without logging out:

```powershell
# Install default Large 96x96 cursors (recommended for crisp visibility)
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Install Extra-Large 128x128 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# Or install 64x64 / 48x48 / 32x32 variants
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 64
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

### Method 2: GUI Install via `install.inf`

1. Right-click `install.inf` in File Explorer and select **Install** (`インストール`).
2. Open the Windows Mouse Properties dialog (`Win + R` → `main.cpl` → **Pointers** tab).
3. Select the **Nemunemu Calico** scheme from the dropdown and click **Apply**.

---

## 🔄 Uninstall & Restore

To restore your previous cursor scheme and original Windows cursor size (`32px`) from `%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json`:

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```

---

## 🛠️ Build & Verify from Source

All `.ani`, `.cur`, and preview `.gif` files are deterministically generated from the 4×2 PNG sprite sheets in `assets/sprites/` using `scripts/build_cursors.py`.

```powershell
# Rebuild all 128/96/64/48/32 .ani/.cur files, GIF previews, and hotspot-guide.png
uv run scripts/build_cursors.py

# Verify RIFF ACON headers, 32-bit BGRA frames, hotspots, and Win32 LoadCursorFromFileW
uv run scripts/build_cursors.py --check
```

---

## 📁 Repository Structure

```text
nemunemu-calico-cursor/
├── assets/
│   ├── gif/                     # Tight-cropped 8-frame transparent GIF previews (64x64 & 256x256)
│   ├── sprites/                 # High-resolution v2 4x2 (8-frame) PNG sprite sheets
│   ├── preview/                 # Hotspot coordinate verification guide (hotspot-guide.png)
│   ├── icon.svg                 # Project icon (128x128)
│   └── header.svg               # Repository hero banner (800x240)
├── cursors/                     # Built 32-bit BGRA .ani and .cur files
│   ├── *.ani / *.cur            # Default Large 96x96 cursors
│   ├── 128x128/                 # Extra-Large 128x128 cursors
│   ├── 96x96/                   # Large 96x96 cursors
│   ├── 64x64/                   # Medium 64x64 cursors
│   ├── 48x48/                   # Compact 48x48 cursors
│   └── 32x32/                   # Classic 32x32 cursors
├── docs/                        # Bilingual VitePress documentation site (EN / JA)
├── scripts/
│   └── build_cursors.py         # Sprite sheet slicer, tight-cropper, .ani/.cur builder & verifier
├── install.ps1                  # One-command installer with SPI_SETCURSORSIZE & live refresh
├── uninstall.ps1                # One-command uninstaller and size/scheme restorer
├── install.inf                  # Windows Explorer right-click INF installer
└── LICENSE                      # MIT License
```

---

## 📄 License

Released under the [MIT License](./LICENSE). Copyright (c) 2026 Sunwood-ai-labs.
