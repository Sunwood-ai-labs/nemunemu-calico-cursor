# 🚀 Getting Started

**Nemunemu Calico Cursor v3** (`ねむねむ三毛ネコ カーソル`) can be installed on Windows 10 and Windows 11 in seconds using either the automated PowerShell installer or the classic `.inf` Explorer installer.

---

## ⚡ Method 1: One-Command PowerShell Installer (Recommended)

The `install.ps1` script performs five safe steps automatically:

1. Copies all 10 cursor role files for the selected size (`128`, `96` default, `64`, `48`, or `32`) into `%LOCALAPPDATA%\Cursors\NemunemuCalico`.
2. Saves your current `HKCU:\Control Panel\Cursors` values and your original `CursorBaseSize` / `Accessibility\CursorSize` to `%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json` (preserving your original defaults).
3. Updates the user registry keys for all 10 primary Windows cursor roles (`Arrow`, `Hand`, `IBeam`, `Wait`, `AppStarting`, `Crosshair`, `No`, `SizeNS`, `SizeWE`, and `SizeAll`) and registers the **Nemunemu Calico** scheme.
4. Updates `CursorBaseSize` and `Accessibility\CursorSize` and invokes Win32 API `SystemParametersInfo(SPI_SETCURSORSIZE)` so Windows renders the cursor at its full target pixel size instead of shrinking it to `32×32`.
5. Calls Win32 API `SystemParametersInfo(SPI_SETCURSORS)` so your new cursors appear **immediately without logging out or restarting**.

### Install Default Large Size (`96×96`)

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### Choose Extra-Large (`128×128`) or Smaller Variants (`64×64` / `48×48` / `32×32`)

Pass the `-Size` parameter to pick your preferred cursor display size:

```powershell
# Install Extra-Large 128x128 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# Install Medium 64x64 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 64

# Install Compact 48x48 or 32x32 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

---

## 🖱️ Method 2: GUI Install via `install.inf`

If you prefer registering the cursor scheme through Windows File Explorer:

1. Locate `install.inf` in the root of the repository.
2. Right-click `install.inf` and select **Install** (`インストール`).
3. Press `Win + R`, type `main.cpl`, and press **Enter** to open **Mouse Properties**.
4. Switch to the **Pointers** tab, select **Nemunemu Calico** under **Scheme**, and click **Apply**.

---

## 🔄 Uninstalling & Restoring Your Previous Cursors

Run `uninstall.ps1` at any time to restore the exact cursor settings and original `32px` cursor size backed up in `backup-cursors.json`, remove the **Nemunemu Calico** scheme entry, refresh the live Windows cursor state, and clean up `%LOCALAPPDATA%\Cursors\NemunemuCalico`:

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
