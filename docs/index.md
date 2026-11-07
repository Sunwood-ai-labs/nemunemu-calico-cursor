---
layout: home

hero:
  name: "Nemunemu Calico Cursor"
  text: "Sleepy Calico Cat & Mint Pointer"
  tagline: "An 8-frame, 32-bit BGRA animated mouse cursor theme for Windows 10 & 11 with pixel-accurate hotspots and instant PowerShell setup."
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
    title: 4 Animated Designs · 5 Windows Roles
    details: Covers Normal Select (Arrow), Link Select (Hand), Text Select (IBeam), and Busy / Working (Wait & AppStarting) with smooth 8-frame (~160ms) loops.
  - icon: 🎯
    title: Pixel-Accurate Click Hotspots
    details: Every hotspot is strictly aligned to the functional arrow tip, finger tip, I-beam center, or spinner center so the sleepy calico cat never gets in the way of clicking.
  - icon: 📐
    title: 3 Size Variants (64×64, 48×48, 32×32)
    details: Built in 32-bit BGRA with full alpha transparency across standard 64×64, medium 48×48, and compact 32×32 resolutions for any monitor DPI.
  - icon: ⚡
    title: Instant Apply & One-Command Restore
    details: Install immediately without rebooting via PowerShell and Win32 SystemParametersInfo, with automatic backup to backup-cursors.json.
---

## 🎨 Animated Cursor Preview

| Preview | Cursor Name | Windows Role | Files (`.ani` / `.cur`) | Hotspot (`64×64` / `48×48` / `32×32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(11, 9)` / `(8, 7)` / `(6, 5)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(21, 6)` / `(16, 5)` / `(11, 3)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(18, 32)` / `(14, 24)` / `(9, 16)` |
| ![Busy / Working](/assets/gif/04_busy_64.gif) | **Busy / Working** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani` | `(32, 32)` / `(24, 24)` / `(16, 16)` |

## 🚀 Quick Install

```powershell
# Apply standard 64x64 cursors immediately (no reboot required)
powershell -ExecutionPolicy Bypass -File .\install.ps1

# Restore previous cursor scheme
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
