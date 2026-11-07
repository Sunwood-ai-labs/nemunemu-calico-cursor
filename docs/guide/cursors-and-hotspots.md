# 🎨 Cursors & Hotspots

Every cursor in **Nemunemu Calico Cursor** is an **8-frame (~160ms per frame / 10 jiffies)** animated loop encoded as a 32-bit BGRA Windows animated cursor (`.ani`), paired with a static frame-0 cursor (`.cur`).

---

## 🐾 Mascot & Cursor Lineup

![Nemunemu Calico Cat 256x256 Mascot](/assets/gif/04_calico_cat_256.gif)

### 1. Normal Select (`Arrow`)

- **Files**: `nemunemu_normal.ani` / `nemunemu_normal.cur`
- **Source GIF**: `assets/gif/01_normal_64.gif`
- **Sprite Sheet**: `assets/sprites/01_normal_sheet.png` (4×2 grid, 8 frames)
- **Design**: A mint arrow pointer in the upper-left with the sleepy calico cat dozing beside it.
- **Hotspots**:
  - `64×64`: `(11, 9)`
  - `48×48`: `(8, 7)`
  - `32×32`: `(6, 5)`

![Normal Select GIF](/assets/gif/01_normal_64.gif)

### 2. Link Select (`Hand`)

- **Files**: `nemunemu_link.ani` / `nemunemu_link.cur`
- **Source GIF**: `assets/gif/02_link_64.gif`
- **Sprite Sheet**: `assets/sprites/02_link_sheet.png` (4×2 grid, 8 frames)
- **Design**: A pointing index finger with a mint cuff accompanied by the sleepy calico cat.
- **Hotspots**:
  - `64×64`: `(21, 6)`
  - `48×48`: `(16, 5)`
  - `32×32`: `(11, 3)`

![Link Select GIF](/assets/gif/02_link_64.gif)

### 3. Text Select (`IBeam`)

- **Files**: `nemunemu_text.ani` / `nemunemu_text.cur`
- **Source GIF**: `assets/gif/03_text_64.gif`
- **Sprite Sheet**: `assets/sprites/03_text_sheet.png` (4×2 grid, 8 frames)
- **Design**: A mint I-beam text cursor on the left with the calico cat sitting quietly beside it. The click axis is strictly aligned to the vertical center of the I-beam bar for accurate text selection.
- **Hotspots**:
  - `64×64`: `(18, 32)`
  - `48×48`: `(14, 24)`
  - `32×32`: `(9, 16)`

![Text Select GIF](/assets/gif/03_text_64.gif)

### 4. Busy / Working (`Wait` & `AppStarting`)

- **Files**: `nemunemu_busy.ani`, `nemunemu_working.ani`, `nemunemu_busy.cur`, `nemunemu_working.cur`
- **Source GIF**: `assets/gif/04_busy_64.gif`
- **Sprite Sheet**: `assets/sprites/04_busy_sheet.png` (4×2 grid, 8 frames)
- **Design**: 8 mint capsules orbiting around the sleeping calico cat in a smooth 8-step cycle. Assigned to both `Wait` (Busy) and `AppStarting` (Working in Background).
- **Hotspots**:
  - `64×64`: `(32, 32)`
  - `48×48`: `(24, 24)`
  - `32×32`: `(16, 16)`

![Busy / Working GIF](/assets/gif/04_busy_64.gif)

---

## 🎯 Hotspot Coordinate Verification

The hotspot guide image (`assets/preview/hotspot-guide.png`) overlays red crosshairs at the exact `(X, Y)` click coordinates for every cursor role:

![Hotspot Verification Guide](/assets/preview/hotspot-guide.png)

| Role | Windows Registry Key | `64×64` Hotspot | `48×48` Hotspot | `32×32` Hotspot |
| :--- | :--- | :---: | :---: | :---: |
| **Normal Select** | `Arrow` | `(11, 9)` | `(8, 7)` | `(6, 5)` |
| **Link Select** | `Hand` | `(21, 6)` | `(16, 5)` | `(11, 3)` |
| **Text Select** | `IBeam` | `(18, 32)` | `(14, 24)` | `(9, 16)` |
| **Busy / Working** | `Wait`, `AppStarting` | `(32, 32)` | `(24, 24)` | `(16, 16)` |
