# 🎨 Cursors & Hotspots

Every cursor in **Nemunemu Calico Cursor v3** is an **8-frame (~160ms per frame / 10 jiffies)** animated loop extracted from high-resolution 4×2 sprite sheets (`1776×888`, `444×444` per cell), tightly cropped around the 8-frame union bounding box, and encoded as a 32-bit BGRA Windows animated cursor (`.ani`) paired with a static frame-0 cursor (`.cur`).

Out of the 17 standard Windows cursor roles, **v3** provides 10 dedicated custom animations covering all 10 primary roles encountered in everyday use (`Arrow`, `Hand`, `IBeam`, `Wait`, `AppStarting`, `Crosshair`, `No`, `SizeNS`, `SizeWE`, and `SizeAll`), including separate animations for `Wait` vs. `AppStarting` and a refined mouth expression for `IBeam`.

---

## 🐾 Mascot & 10-Role Cursor Lineup

![Nemunemu Calico Cat 256x256 Mascot](/assets/gif/04_calico_cat_256.gif)

### 1. Normal Select (`Arrow`)

- **Files**: `nemunemu_normal.ani` / `nemunemu_normal.cur`
- **Preview GIF**: `assets/gif/01_normal_64.gif`
- **Sprite Sheet**: `assets/sprites/01_normal_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A mint arrow pointer in the upper-left while the sleepy calico cat stretches its paws and yawns beside it.
- **Hotspots**:
  - `128×128`: `(5, 8)`
  - `96×96` (Default): `(3, 6)`
  - `64×64`: `(2, 4)`
  - `48×48`: `(2, 3)`
  - `32×32`: `(1, 2)`

![Normal Select GIF](/assets/gif/01_normal_64.gif)

### 2. Link Select (`Hand`)

- **Files**: `nemunemu_link.ani` / `nemunemu_link.cur`
- **Preview GIF**: `assets/gif/02_link_64.gif`
- **Sprite Sheet**: `assets/sprites/02_link_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A pointing index finger with a mint cuff while the calico cat wakes up and waves its paw.
- **Hotspots**:
  - `128×128`: `(39, 2)`
  - `96×96` (Default): `(29, 1)`
  - `64×64`: `(19, 1)`
  - `48×48`: `(14, 1)`
  - `32×32`: `(10, 0)`

![Link Select GIF](/assets/gif/02_link_64.gif)

### 3. Text Select (`IBeam`)

- **Files**: `nemunemu_text.ani` / `nemunemu_text.cur`
- **Preview GIF**: `assets/gif/03_text_64.gif`
- **Sprite Sheet**: `assets/sprites/03_text_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A mint I-beam text cursor on the left while the calico cat stretches vertically along the shaft with a refined v3 mouth expression. The click axis is strictly aligned to the vertical center of the I-beam bar for accurate text selection.
- **Hotspots**:
  - `128×128`: `(16, 60)`
  - `96×96` (Default): `(12, 45)`
  - `64×64`: `(8, 30)`
  - `48×48`: `(6, 22)`
  - `32×32`: `(4, 15)`

![Text Select GIF](/assets/gif/03_text_64.gif)

### 4. Busy (`Wait`)

- **Files**: `nemunemu_busy.ani` / `nemunemu_busy.cur`
- **Preview GIF**: `assets/gif/04_busy_64.gif`
- **Sprite Sheet**: `assets/sprites/04_busy_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: Dedicated full-screen wait cursor where the calico cat rolls and stretches inside an 8-segment rotating mint capsule ring.
- **Hotspots**:
  - `128×128`: `(64, 64)`
  - `96×96` (Default): `(48, 48)`
  - `64×64`: `(32, 32)`
  - `48×48`: `(24, 24)`
  - `32×32`: `(16, 16)`

![Busy GIF](/assets/gif/04_busy_64.gif)

### 5. Working in Background (`AppStarting`)

- **Files**: `nemunemu_working.ani` / `nemunemu_working.cur`
- **Preview GIF**: `assets/gif/05_working_64.gif`
- **Sprite Sheet**: `assets/sprites/05_working_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: Newly separated from `Wait` in v3 — combines an active upper-left mint arrow pointer (with the hotspot at the arrow tip so you can keep clicking accurately) and a mini rotating ring with the sleepy calico cat.
- **Hotspots**:
  - `128×128`: `(4, 24)`
  - `96×96` (Default): `(3, 18)`
  - `64×64`: `(2, 12)`
  - `48×48`: `(2, 9)`
  - `32×32`: `(1, 6)`

![Working GIF](/assets/gif/05_working_64.gif)

### 6. Precision Select (`Crosshair`)

- **Files**: `nemunemu_precision.ani` / `nemunemu_precision.cur`
- **Preview GIF**: `assets/gif/06_precision_64.gif`
- **Sprite Sheet**: `assets/sprites/06_precision_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A crisp mint crosshair reticle with the calico cat peeking beside it. The hotspot sits at the exact intersection of the crosshair lines for pixel-accurate screen capture and drawing tools.
- **Hotspots**:
  - `128×128`: `(35, 38)`
  - `96×96` (Default): `(26, 29)`
  - `64×64`: `(18, 19)`
  - `48×48`: `(13, 14)`
  - `32×32`: `(9, 10)`

![Precision Select GIF](/assets/gif/06_precision_64.gif)

### 7. Unavailable (`No`)

- **Files**: `nemunemu_unavailable.ani` / `nemunemu_unavailable.cur`
- **Preview GIF**: `assets/gif/07_unavailable_64.gif`
- **Sprite Sheet**: `assets/sprites/07_unavailable_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A prohibition circle-and-slash badge paired with the sleepy calico cat reacting to invalid drop targets or disabled controls.
- **Hotspots**:
  - `128×128`: `(40, 41)`
  - `96×96` (Default): `(30, 31)`
  - `64×64`: `(20, 21)`
  - `48×48`: `(15, 15)`
  - `32×32`: `(10, 10)`

![Unavailable GIF](/assets/gif/07_unavailable_64.gif)

### 8. Vertical Resize (`SizeNS`)

- **Files**: `nemunemu_vertical.ani` / `nemunemu_vertical.cur`
- **Preview GIF**: `assets/gif/08_vertical_64.gif`
- **Sprite Sheet**: `assets/sprites/08_vertical_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A mint double-headed vertical resize arrow (`↕`) with the calico cat stretching up and down along the vertical shaft.
- **Hotspots**:
  - `128×128`: `(21, 63)`
  - `96×96` (Default): `(16, 47)`
  - `64×64`: `(11, 32)`
  - `48×48`: `(8, 24)`
  - `32×32`: `(5, 16)`

![Vertical Resize GIF](/assets/gif/08_vertical_64.gif)

### 9. Horizontal Resize (`SizeWE`)

- **Files**: `nemunemu_horizontal.ani` / `nemunemu_horizontal.cur`
- **Preview GIF**: `assets/gif/09_horizontal_64.gif`
- **Sprite Sheet**: `assets/sprites/09_horizontal_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A mint double-headed horizontal resize arrow (`↔`) with the calico cat sprawling and swaying left-to-right on top of the bar.
- **Hotspots**:
  - `128×128`: `(64, 25)`
  - `96×96` (Default): `(48, 19)`
  - `64×64`: `(32, 13)`
  - `48×48`: `(24, 10)`
  - `32×32`: `(16, 6)`

![Horizontal Resize GIF](/assets/gif/09_horizontal_64.gif)

### 10. Move (`SizeAll`)

- **Files**: `nemunemu_move.ani` / `nemunemu_move.cur`
- **Preview GIF**: `assets/gif/10_move_64.gif`
- **Sprite Sheet**: `assets/sprites/10_move_sheet.png` (4×2 grid, 8 frames)
- **v3 Animation**: A four-way mint move cross arrow (`✥`) paired with the calico cat clinging playfully beside the center intersection.
- **Hotspots**:
  - `128×128`: `(42, 41)`
  - `96×96` (Default): `(32, 31)`
  - `64×64`: `(21, 21)`
  - `48×48`: `(16, 15)`
  - `32×32`: `(11, 10)`

![Move GIF](/assets/gif/10_move_64.gif)

---

## 🎯 Hotspot Coordinate Verification

The hotspot guide image (`assets/preview/hotspot-guide.png`) overlays red crosshairs at the exact `(X, Y)` click coordinates for all 10 cursor roles:

![Hotspot Verification Guide](/assets/preview/hotspot-guide.png)

| Role | Windows Registry Key | `128×128` | `96×96` (Default) | `64×64` | `48×48` | `32×32` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Normal Select** | `Arrow` | `(5, 8)` | **`(3, 6)`** | `(2, 4)` | `(2, 3)` | `(1, 2)` |
| **Link Select** | `Hand` | `(39, 2)` | **`(29, 1)`** | `(19, 1)` | `(14, 1)` | `(10, 0)` |
| **Text Select** | `IBeam` | `(16, 60)` | **`(12, 45)`** | `(8, 30)` | `(6, 22)` | `(4, 15)` |
| **Busy** | `Wait` | `(64, 64)` | **`(48, 48)`** | `(32, 32)` | `(24, 24)` | `(16, 16)` |
| **Working** | `AppStarting` | `(4, 24)` | **`(3, 18)`** | `(2, 12)` | `(2, 9)` | `(1, 6)` |
| **Precision Select** | `Crosshair` | `(35, 38)` | **`(26, 29)`** | `(18, 19)` | `(13, 14)` | `(9, 10)` |
| **Unavailable** | `No` | `(40, 41)` | **`(30, 31)`** | `(20, 21)` | `(15, 15)` | `(10, 10)` |
| **Vertical Resize** | `SizeNS` | `(21, 63)` | **`(16, 47)`** | `(11, 32)` | `(8, 24)` | `(5, 16)` |
| **Horizontal Resize** | `SizeWE` | `(64, 25)` | **`(48, 19)`** | `(32, 13)` | `(24, 10)` | `(16, 6)` |
| **Move** | `SizeAll` | `(42, 41)` | **`(32, 31)`** | `(21, 21)` | `(16, 15)` | `(11, 10)` |
