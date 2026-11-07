---
layout: home

hero:
  name: "Nemunemu Calico Cursor v2"
  text: "Sleepy Calico Cat & Mint Pointer"
  tagline: "An expressive 8-frame, 32-bit BGRA animated mouse cursor theme for Windows 10 & 11 with tight-cropped high-visibility sizes (128 / 96 / 64 / 48 / 32) and instant PowerShell setup."
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
    title: Expressive v2 8-Frame Animations
    details: Covers Normal Select (stretching & yawning), Link Select (waving paw), Text Select (climbing I-beam), and Busy / Working (rolling in a rotating ring).
  - icon: 🔎
    title: Automatic Large Cursor Display
    details: Tightly cropped around the 8-frame union bounding box and paired with Win32 SPI_SETCURSORSIZE (default 96×96, up to 128×128) so the calico cat appears large and crisp on screen.
  - icon: 🎯
    title: Pixel-Accurate Click Hotspots
    details: Every hotspot is strictly aligned to the functional arrow tip, finger tip, I-beam shaft center, or spinner center across all 5 resolution variants.
  - icon: ⚡
    title: Instant Apply & One-Command Restore
    details: Install immediately without rebooting via PowerShell and restore both your original cursor scheme and 32px OS cursor size anytime with uninstall.ps1.
---

## 🎨 Animated Cursor Preview

| Preview | Cursor Name | Windows Role | Files (`.ani` / `.cur`) | Hotspot (`128` / `96` Default / `64` / `48` / `32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(5, 8)` / **`(3, 6)`** / `(2, 4)` / `(2, 3)` / `(1, 2)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(39, 2)` / **`(29, 1)`** / `(19, 1)` / `(14, 1)` / `(10, 0)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(16, 60)` / **`(12, 45)`** / `(8, 30)` / `(6, 22)` / `(4, 15)` |
| ![Busy / Working](/assets/gif/04_busy_64.gif) | **Busy / Working** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani` | `(64, 64)` / **`(48, 48)`** / `(32, 32)` / `(24, 24)` / `(16, 16)` |

## 🚀 Quick Install

```powershell
# Apply default Large 96x96 cursors immediately (no reboot required)
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Or apply Extra-Large 128x128 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# Restore previous cursor scheme and original 32px size
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
