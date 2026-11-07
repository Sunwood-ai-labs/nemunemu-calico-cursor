<div align="center">
  <img src="./assets/header.svg" alt="Nemunemu Calico Cursor Banner" width="800" />

  <h1>🐾 Nemunemu Calico Cursor</h1>

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

**Nemunemu Calico Cursor** (`ねむねむ三毛ネコ`) is an animated Windows mouse cursor theme featuring a sleepy calico cat nestled beside a clean mint-colored pointer. Every cursor is crafted as an **8-frame (~160ms per frame)** loop with full alpha transparency (`32-bit BGRA`) in both animated (`.ani`) and static (`.cur`) formats.

<div align="center">
  <img src="./assets/gif/04_calico_cat_256.gif" alt="Nemunemu Calico Cat Mascot Preview (256x256)" width="160" />
</div>

- **4 Cursor Designs Covering 5 Windows Cursor Roles**: Normal Select (`Arrow`), Link Select (`Hand`), Text Select (`IBeam`), and Busy / Working (`Wait` & `AppStarting`).
- **3 Multi-DPI Size Variants**: Standard `64×64` (`cursors/`), medium `48×48` (`cursors/48x48/`), and compact `32×32` (`cursors/32x32/`).
- **Pixel-Accurate Hotspots**: Each cursor's click hotspot is aligned to the functional pointer tip, finger tip, I-beam center, or spinner center—so the cat mascot never interferes with clicking accuracy.
- **One-Command Instant Apply & Safe Rollback**: `install.ps1` backs up your current cursor scheme to `backup-cursors.json` and applies the theme immediately via `SystemParametersInfo(SPI_SETCURSORS)` without requiring a reboot.

---

## 🎨 Cursor Gallery & Hotspot Coordinates

### Animated Cursor Previews

| Preview (64×64) | Cursor Name | Windows Role (`Registry`) | Animated / Static Files | Design Description |
| :---: | :--- | :--- | :--- | :--- |
| <img src="./assets/gif/01_normal_64.gif" alt="Normal Select" width="64" /> | **Normal Select** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | A sleepy calico cat dozing next to a crisp mint arrow pointer. |
| <img src="./assets/gif/02_link_64.gif" alt="Link Select" width="64" /> | **Link Select** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | A pointing hand with a mint cuff accompanied by the sleepy calico cat. |
| <img src="./assets/gif/03_text_64.gif" alt="Text Select" width="64" /> | **Text Select** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | The calico cat sitting beside a mint I-beam (click axis strictly aligned to the I-beam center). |
| <img src="./assets/gif/04_busy_64.gif" alt="Busy / Working" width="64" /> | **Busy / Working** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani`<br>`nemunemu_busy.cur`<br>`nemunemu_working.cur` | 8 mint capsules orbiting around the sleeping calico cat. |

### Hotspot Verification & Coordinate Table

<div align="center">
  <img src="./assets/preview/hotspot-guide.png" alt="Hotspot Verification Guide" width="680" />
</div>

| Cursor Role | Source GIF | Sprite Sheet (4×2 Grid) | Hotspot `64×64` | Hotspot `48×48` | Hotspot `32×32` |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Normal Select (`Arrow`)** | `assets/gif/01_normal_64.gif` | `assets/sprites/01_normal_sheet.png` | `(11, 9)` | `(8, 7)` | `(6, 5)` |
| **Link Select (`Hand`)** | `assets/gif/02_link_64.gif` | `assets/sprites/02_link_sheet.png` | `(21, 6)` | `(16, 5)` | `(11, 3)` |
| **Text Select (`IBeam`)** | `assets/gif/03_text_64.gif` | `assets/sprites/03_text_sheet.png` | `(18, 32)` | `(14, 24)` | `(9, 16)` |
| **Busy / Working (`Wait`, `AppStarting`)** | `assets/gif/04_busy_64.gif` | `assets/sprites/04_busy_sheet.png` | `(32, 32)` | `(24, 24)` | `(16, 16)` |

---

## 🚀 Quick Start (Installation)

### Method 1: One-Command PowerShell Install (Recommended)

Run the installer script from PowerShell in the repository root. It copies the cursor files to `%LOCALAPPDATA%\Cursors\NemunemuCalico`, saves your previous cursor settings to `backup-cursors.json`, updates `HKCU:\Control Panel\Cursors`, and refreshes Windows cursors immediately via Win32 API `SystemParametersInfo(SPI_SETCURSORS)`:

```powershell
# Install standard 64x64 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Or install 48x48 / 32x32 size variants
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

### Method 2: GUI Install via `install.inf`

1. Right-click `install.inf` in File Explorer and select **Install** (`インストール`).
2. Open the Windows Mouse Properties dialog (`Win + R` → `main.cpl` → **Pointers** tab).
3. Select the **Nemunemu Calico** scheme from the dropdown and click **Apply**.

---

## 🔄 Uninstall & Restore

To restore your previous cursor settings from the automatic backup (`%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json`) and remove the installed files:

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```

---

## 🛠️ Build & Verify from Source

All `.ani` and `.cur` files are deterministically generated from the transparent GIF animations in `assets/gif/` using `scripts/build_cursors.py`.

```powershell
# Rebuild all 64x64, 48x48, and 32x32 .ani/.cur files and hotspot preview guide
uv run scripts/build_cursors.py

# Verify RIFF ACON headers, 32-bit BGRA frames, and hotspot coordinates
uv run scripts/build_cursors.py --check
```

---

## 📁 Repository Structure

```text
nemunemu-calico-cursor/
├── assets/
│   ├── gif/                     # Source 8-frame transparent GIFs (64x64 & 256x256 mascot)
│   ├── sprites/                 # 4x2 (8-frame) PNG sprite sheets
│   ├── preview/                 # Hotspot coordinate verification guide (hotspot-guide.png)
│   ├── icon.svg                 # Project icon (128x128)
│   └── header.svg               # Repository hero banner (800x240)
├── cursors/                     # Built 32-bit BGRA .ani and .cur files
│   ├── *.ani / *.cur            # Standard 64x64 cursors
│   ├── 48x48/                   # Medium 48x48 cursors
│   └── 32x32/                   # Compact 32x32 cursors
├── docs/                        # Bilingual VitePress documentation site (EN / JA)
├── scripts/
│   └── build_cursors.py         # RIFF ACON (.ani) & 32-bit BGRA (.cur) builder and verifier
├── install.ps1                  # One-command installer with automatic backup & live refresh
├── uninstall.ps1                # One-command uninstaller and backup restorer
├── install.inf                  # Windows Explorer right-click INF installer
└── LICENSE                      # MIT License
```

---

## 📄 License

Released under the [MIT License](./LICENSE). Copyright (c) 2026 Sunwood-ai-labs.
