# 🚀 Getting Started

**Nemunemu Calico Cursor** (`ねむねむ三毛ネコ カーソル`) can be installed on Windows 10 and Windows 11 in seconds using either the automated PowerShell installer or the classic `.inf` Explorer installer.

---

## ⚡ Method 1: One-Command PowerShell Installer (Recommended)

The `install.ps1` script performs four safe steps automatically:

1. Copies the selected cursor size files into `%LOCALAPPDATA%\Cursors\NemunemuCalico`.
2. Saves your current `HKCU:\Control Panel\Cursors` values to `%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json` (only if a backup does not already exist, preserving your original defaults).
3. Updates the user registry keys for `Arrow`, `Hand`, `IBeam`, `Wait`, and `AppStarting` and registers the **Nemunemu Calico** scheme.
4. Calls Win32 API `SystemParametersInfo(SPI_SETCURSORS)` so your new cursors appear **immediately without logging out or restarting**.

### Install Standard Size (`64×64`)

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### Choose a Smaller Size (`48×48` or `32×32`)

If you prefer a smaller cursor footprint or use 100% display scaling on a 1080p monitor, pass the `-Size` parameter:

```powershell
# Install medium 48x48 cursors
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48

# Install compact 32x32 cursors
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

Run `uninstall.ps1` at any time to restore the exact cursor settings backed up in `backup-cursors.json`, remove the **Nemunemu Calico** scheme entry, refresh the live Windows cursor state, and clean up `%LOCALAPPDATA%\Cursors\NemunemuCalico`:

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
