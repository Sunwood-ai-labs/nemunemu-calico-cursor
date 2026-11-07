---
layout: home

hero:
  name: "Nemunemu Calico Cursor v3"
  text: "Sleepy Calico Cat & Mint Pointer"
  tagline: "An expressive 8-frame, 32-bit BGRA animated mouse cursor theme for Windows 10 & 11 covering all 10 everyday cursor roles with tight-cropped high-visibility sizes (128 / 96 / 64 / 48 / 32) and instant PowerShell setup."
  image:
    src: /assets/gif/04_calico_cat_256.gif
    alt: Nemunemu Calico Cat Mascot
  actions:
    - theme: brand
      text: Getting Started
      link: /guide/getting-started
    - theme: alt
      text: Cursors & Hotspots
      link: /guide/cursors-and-hotspots
    - theme: alt
      text: View on GitHub
      link: https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor

features:
  - icon: 🐾
    title: 10 Dedicated v3 8-Frame Animations
    details: Covers all 10 primary everyday Windows roles (Arrow, Hand, IBeam, Wait, AppStarting, Crosshair, No, SizeNS, SizeWE, SizeAll) with separate Busy vs. Working designs and a refined IBeam cat expression.
  - icon: 🔎
    title: Automatic Large Cursor Display
    details: Tightly cropped around the 8-frame union bounding box and paired with Win32 SPI_SETCURSORSIZE (default 96×96, up to 128×128) so the calico cat appears large and crisp on screen.
  - icon: 🎯
    title: Pixel-Accurate Click Hotspots
    details: Every hotspot is strictly aligned to the functional arrow tip, finger tip, I-beam shaft, crosshair reticle, resize shaft, or spinner center across all 5 resolution variants (120 verified files).
  - icon: ⚡
    title: Instant Apply & One-Command Restore
    details: Install immediately without rebooting via PowerShell and restore both your original cursor scheme and 32px OS cursor size anytime with uninstall.ps1.
---

## 🎨 Animated Cursor Preview (10 Designs · 10 Roles)

| Preview | Cursor Name | Windows Role | Files (`.ani` / `.cur`) | Hotspot (`128` / `96` Default / `64` / `48` / `32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(5, 8)` / **`(3, 6)`** / `(2, 4)` / `(2, 3)` / `(1, 2)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(39, 2)` / **`(29, 1)`** / `(19, 1)` / `(14, 1)` / `(10, 0)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(16, 60)` / **`(12, 45)`** / `(8, 30)` / `(6, 22)` / `(4, 15)` |
| ![Busy](/assets/gif/04_busy_64.gif) | **Busy** | `Wait` | `nemunemu_busy.ani`<br>`nemunemu_busy.cur` | `(64, 64)` / **`(48, 48)`** / `(32, 32)` / `(24, 24)` / `(16, 16)` |
| ![Working](/assets/gif/05_working_64.gif) | **Working** | `AppStarting` | `nemunemu_working.ani`<br>`nemunemu_working.cur` | `(4, 24)` / **`(3, 18)`** / `(2, 12)` / `(2, 9)` / `(1, 6)` |
| ![Precision Select](/assets/gif/06_precision_64.gif) | **Precision Select** | `Crosshair` | `nemunemu_precision.ani`<br>`nemunemu_precision.cur` | `(35, 38)` / **`(26, 29)`** / `(18, 19)` / `(13, 14)` / `(9, 10)` |
| ![Unavailable](/assets/gif/07_unavailable_64.gif) | **Unavailable** | `No` | `nemunemu_unavailable.ani`<br>`nemunemu_unavailable.cur` | `(40, 41)` / **`(30, 31)`** / `(20, 21)` / `(15, 15)` / `(10, 10)` |
| ![Vertical Resize](/assets/gif/08_vertical_64.gif) | **Vertical Resize** | `SizeNS` | `nemunemu_vertical.ani`<br>`nemunemu_vertical.cur` | `(21, 63)` / **`(16, 47)`** / `(11, 32)` / `(8, 24)` / `(5, 16)` |
| ![Horizontal Resize](/assets/gif/09_horizontal_64.gif) | **Horizontal Resize** | `SizeWE` | `nemunemu_horizontal.ani`<br>`nemunemu_horizontal.cur` | `(64, 25)` / **`(48, 19)`** / `(32, 13)` / `(24, 10)` / `(16, 6)` |
| ![Move](/assets/gif/10_move_64.gif) | **Move** | `SizeAll` | `nemunemu_move.ani`<br>`nemunemu_move.cur` | `(42, 41)` / **`(32, 31)`** / `(21, 21)` / `(16, 15)` / `(11, 10)` |

## 🚀 Quick Install

```powershell
# Apply default Large 96x96 cursors immediately (no reboot required)
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Or apply Extra-Large 128x128 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# Restore previous cursor scheme and original 32px size
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
