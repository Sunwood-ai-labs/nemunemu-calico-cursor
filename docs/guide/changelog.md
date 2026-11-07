# Release Notes (Changelog)

All notable releases and updates for **Nemunemu Calico Cat Cursor**.

---

## v3.0.0 — Full 10-Role Animated Cursor Set (120 Binaries)

### ✨ 6 New Dedicated Animated Cursor Roles
In `v3.0.0`, the cursor theme expands from 4 designs (5 roles) to **10 unique 8-frame animated cursor designs covering all 10 primary Windows system cursor roles**:

| # | Role | Registry Key | System ID | Preview | Description |
| :-: | :--- | :--- | :--- | :-: | :--- |
| **01** | **Normal Select** | `Arrow` | `OCR_NORMAL` (`32512`) | <img src="/assets/gif/01_normal_64.gif" width="48" /> | Mint arrow pointer + sleepy calico cat |
| **02** | **Link Select** | `Hand` | `OCR_HAND` (`32649`) | <img src="/assets/gif/02_link_64.gif" width="48" /> | Orange paw hand + peeking calico cat |
| **03** | **Text Select (Updated)** | `IBeam` | `OCR_IBEAM` (`32513`) | <img src="/assets/gif/03_text_64.gif" width="48" /> | Terracotta I-beam + sleeping cat (redrawn mouth expression) |
| **04** | **Busy / Wait** | `Wait` | `OCR_WAIT` (`32514`) | <img src="/assets/gif/04_busy_64.gif" width="48" /> | Rotating mint dashed ring + calico cat |
| **05** | **Working in Background (New)** | `AppStarting` | `OCR_APPSTARTING` (`32650`) | <img src="/assets/gif/05_working_64.gif" width="48" /> | Mint arrow + mini rotating ring + calico cat |
| **06** | **Precision Select (New)** | `Crosshair` | `OCR_CROSS` (`32515`) | <img src="/assets/gif/06_precision_64.gif" width="48" /> | Cat-eared crosshair + swaying tail |
| **07** | **Unavailable (New)** | `No` | `OCR_NO` (`32648`) | <img src="/assets/gif/07_unavailable_64.gif" width="48" /> | Coral forbidden sign + head-tilting calico cat |
| **08** | **Vertical Resize (New)** | `SizeNS` | `OCR_SIZENS` (`32645`) | <img src="/assets/gif/08_vertical_64.gif" width="48" /> | Vertical double arrow + stretching calico cat |
| **09** | **Horizontal Resize (New)** | `SizeWE` | `OCR_SIZEWE` (`32644`) | <img src="/assets/gif/09_horizontal_64.gif" width="48" /> | Horizontal double arrow + swaying calico cat |
| **10** | **Move (New)** | `SizeAll` | `OCR_SIZEALL` (`32646`) | <img src="/assets/gif/10_move_64.gif" width="48" /> | Four-way cross arrow + sleeping calico cat |

### 🔧 Build Pipeline & Installer Improvements
- **Integer-Cell Sprite Sheet Normalization**: Automatically normalizes `1774×887` sprite sheets (`03`, `06`–`10`) to `1776×888` (`444×444` per cell) using `LANCZOS` resampling prior to slicing, eliminating 1px frame jitter.
- **120 Verified Cursor Binaries**: Generates and validates 10 roles × (`.ani` + `.cur`) × 5 size tiers (`32x32`, `48x48`, `64x64`, `96x96`, `128x128` + root `96x96` defaults) via Win32 `LoadCursorFromFileW`.
- **Full 10-Role Live Injection**: `install.ps1`, `uninstall.ps1`, and `install.inf` now register and live-inject all 10 roles without requiring sign-out.

---

## v2.0.0 — Dynamic 8-Frame Sprites, Tight Cropping & Win32 Live Injection

- **Dynamic 8-Frame Artwork**: Upgraded all animations with larger motion amplitude (popping sleep bubbles, swaying body, wagging tail, rotating ring).
- **Tight Bounding-Box Cropping (`4%` margin)**: Maximized visible character size within each cursor canvas while keeping hotspot coordinates locked.
- **5 Multi-Size Tiers (`32x32` to `128x128`)**: Set `96x96` as the default tier with `-Size` support in `install.ps1`.
- **Win32 `LoadImageW` + `SetSystemCursor` Injection & DWM Scale Reset**: Fixed `32×32` screenshot downscaling and prevented `3×` DWM double-scaling (`288px` overflow during `Win+Shift+S`).

---

## v1.0.0 — Initial Release

- Initial release with 4 animated cursor designs (`Normal`, `Link`, `Text`, `Busy`) mapped across 5 Windows system roles.
- Pure-Python RIFF `ACON` (`.ani`) and `.cur` builder (`scripts/build_cursors.py`) with automated Win32 validation.
- PowerShell installer (`install.ps1`), uninstaller with JSON backup (`uninstall.ps1`), and `.inf` installer (`install.inf`).
