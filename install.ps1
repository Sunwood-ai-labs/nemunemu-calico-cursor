<#
.SYNOPSIS
    Installs and immediately activates the "Nemunemu Calico" (ねむねむ三毛ネコ) v2 Windows mouse cursor scheme.
.DESCRIPTION
    Copies the selected cursor size (128, 96, 64, 48, or 32; default: 96) to
    %LOCALAPPDATA%\Cursors\NemunemuCalico, backs up the existing HKCU:\Control Panel\Cursors
    settings on first run, keeps Windows DWM pointer magnification at 1.0x (SPI_SETCURSORSIZE = 32,
    CursorBaseSize = 32, Accessibility\CursorSize = 1) to prevent double-scaling (e.g. 96px x 3 = 288px),
    and injects full-resolution ($Size x $Size) animated HCURSORs via LoadImageW(LR_LOADFROMFILE) +
    SetSystemCursor so on-screen display and screenshot capture match 1:1 at $Size x $Size.
.PARAMETER Size
    Cursor pixel size to install and display: 128, 96 (default), 64, 48, or 32.
#>
[CmdletBinding()]
param(
    [ValidateSet(128, 96, 64, 48, 32)]
    [int]$Size = 96
)

$ErrorActionPreference = "Stop"

$SchemeName = -join @(
    [char]0x306D, [char]0x3080, [char]0x306D, [char]0x3080,
    [char]0x4E09, [char]0x6BDB, [char]0x30CD, [char]0x30B3
) + " (Nemunemu Calico)"

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceDir = switch ($Size) {
    128 { Join-Path $RepoRoot "cursors\128x128" }
    96  { Join-Path $RepoRoot "cursors" }
    64  { Join-Path $RepoRoot "cursors\64x64" }
    48  { Join-Path $RepoRoot "cursors\48x48" }
    32  { Join-Path $RepoRoot "cursors\32x32" }
}

if (-not (Test-Path $SourceDir)) {
    throw "Source cursor directory not found: $SourceDir. Run 'uv run scripts/build_cursors.py' first."
}

$InstallDir = Join-Path $env:LOCALAPPDATA "Cursors\NemunemuCalico"
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null

$CursorsRegPath = "HKCU:\Control Panel\Cursors"
$SchemesRegPath = "HKCU:\Control Panel\Cursors\Schemes"
$AccessRegPath  = "HKCU:\Software\Microsoft\Accessibility"
$BackupFile     = Join-Path $InstallDir "backup-cursors.json"

# 1. Back up current cursor settings on first run (never overwrite an existing backup)
if (-not (Test-Path $BackupFile)) {
    $regItem = Get-Item -Path $CursorsRegPath
    $origBaseSize = 32
    try {
        $val = (Get-ItemProperty -Path $CursorsRegPath -Name "CursorBaseSize" -ErrorAction SilentlyContinue).CursorBaseSize
        if ($null -ne $val) { $origBaseSize = [int]$val }
    } catch {}

    $origAccessSize = 1
    try {
        if (Test-Path $AccessRegPath) {
            $aval = (Get-ItemProperty -Path $AccessRegPath -Name "CursorSize" -ErrorAction SilentlyContinue).CursorSize
            if ($null -ne $aval) { $origAccessSize = [int]$aval }
        }
    } catch {}

    $backupData = [ordered]@{
        DefaultValue                    = $regItem.GetValue("", "")
        OriginalCursorBaseSize          = $origBaseSize
        OriginalAccessibilityCursorSize = $origAccessSize
        Values                          = [ordered]@{}
    }
    foreach ($prop in $regItem.GetValueNames()) {
        if ($prop -ne "") {
            $backupData.Values[$prop] = $regItem.GetValue($prop, "", [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
        }
    }
    $backupData | ConvertTo-Json -Depth 4 | Set-Content -Path $BackupFile -Encoding UTF8
    Write-Host "[Backup] Saved original cursor settings to: $BackupFile" -ForegroundColor Cyan
} else {
    Write-Host "[Backup] Existing backup preserved at: $BackupFile" -ForegroundColor DarkGray
}

# 2. Copy .ani and .cur files for the chosen size into $InstallDir
$CursorStems = @(
    "nemunemu_normal",
    "nemunemu_link",
    "nemunemu_text",
    "nemunemu_busy",
    "nemunemu_working"
)

foreach ($stem in $CursorStems) {
    foreach ($ext in @(".ani", ".cur")) {
        $srcFile = Join-Path $SourceDir ($stem + $ext)
        if (-not (Test-Path $srcFile)) {
            throw "Missing required cursor file: $srcFile"
        }
        Copy-Item -Path $srcFile -Destination (Join-Path $InstallDir ($stem + $ext)) -Force
    }
}
Write-Host "[Copy] Installed ${Size}x${Size} v2 cursors to: $InstallDir" -ForegroundColor Green

# 3. Register scheme under HKCU:\Control Panel\Cursors\Schemes
if (-not (Test-Path $SchemesRegPath)) {
    New-Item -Path $SchemesRegPath -Force | Out-Null
}

$NormalPath  = Join-Path $InstallDir "nemunemu_normal.ani"
$LinkPath    = Join-Path $InstallDir "nemunemu_link.ani"
$TextPath    = Join-Path $InstallDir "nemunemu_text.ani"
$BusyPath    = Join-Path $InstallDir "nemunemu_busy.ani"
$WorkingPath = Join-Path $InstallDir "nemunemu_working.ani"

$SchemeValue = @(
    $NormalPath,
    "%SystemRoot%\cursors\aero_helpsel.cur",
    $WorkingPath,
    $BusyPath,
    "",
    $TextPath,
    "%SystemRoot%\cursors\aero_pen.cur",
    "%SystemRoot%\cursors\aero_unavail.cur",
    "%SystemRoot%\cursors\aero_ns.cur",
    "%SystemRoot%\cursors\aero_ew.cur",
    "%SystemRoot%\cursors\aero_nwse.cur",
    "%SystemRoot%\cursors\aero_nesw.cur",
    "%SystemRoot%\cursors\aero_move.cur",
    "%SystemRoot%\cursors\aero_up.cur",
    $LinkPath,
    "%SystemRoot%\cursors\aero_pin.cur",
    "%SystemRoot%\cursors\aero_person.cur"
) -join ","

New-ItemProperty -Path $SchemesRegPath -Name $SchemeName -Value $SchemeValue -PropertyType ExpandString -Force | Out-Null

# 4. Update active HKCU:\Control Panel\Cursors entries and keep DWM magnification at 1.0x (32 / Slider=1)
Set-ItemProperty -Path $CursorsRegPath -Name "(default)" -Value $SchemeName
New-ItemProperty -Path $CursorsRegPath -Name "Scheme Source" -Value 1 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "CursorBaseSize" -Value 32 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Arrow" -Value $NormalPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Hand" -Value $LinkPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "IBeam" -Value $TextPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Wait" -Value $BusyPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "AppStarting" -Value $WorkingPath -PropertyType ExpandString -Force | Out-Null

if (-not (Test-Path $AccessRegPath)) {
    New-Item -Path $AccessRegPath -Force | Out-Null
}
New-ItemProperty -Path $AccessRegPath -Name "CursorSize" -Value 1 -PropertyType DWord -Force | Out-Null

# 5. Reset DWM pointer magnification to 1.0x (SPI_SETCURSORSIZE = 32), reload scheme, and inject $Size x $Size HCURSORs
if (-not ("Win32CursorNativeV4" -as [type])) {
    Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public static class Win32CursorNativeV4 {
    public const uint SPI_SETCURSORS = 0x0057;
    public const uint SPI_SETCURSORSIZE = 0x2029;
    public const uint SPIF_UPDATEINIFILE = 0x01;
    public const uint SPIF_SENDCHANGE = 0x02;
    public const uint IMAGE_CURSOR = 2;
    public const uint LR_LOADFROMFILE = 0x00000010;

    [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern bool SystemParametersInfo(
        uint uiAction,
        uint uiParam,
        IntPtr pvParam,
        uint fWinIni
    );

    [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern IntPtr LoadImage(
        IntPtr hInst,
        string lpszName,
        uint uType,
        int cxDesired,
        int cyDesired,
        uint fuLoad
    );

    [DllImport("user32.dll", SetLastError = true)]
    public static extern bool SetSystemCursor(
        IntPtr hcur,
        uint id
    );
}
"@
}

# Ensure DWM pointer multiplier is 1.0x (32) so a 96x96 HCURSOR is NOT multiplied by 3x into 288x288!
$sizeOk = [Win32CursorNativeV4]::SystemParametersInfo(
    [Win32CursorNativeV4]::SPI_SETCURSORSIZE,
    0,
    [IntPtr]32,
    ([Win32CursorNativeV4]::SPIF_UPDATEINIFILE -bor [Win32CursorNativeV4]::SPIF_SENDCHANGE)
)
if (-not $sizeOk) {
    [void][Win32CursorNativeV4]::SystemParametersInfo(
        [Win32CursorNativeV4]::SPI_SETCURSORSIZE,
        0,
        [IntPtr]32,
        [Win32CursorNativeV4]::SPIF_SENDCHANGE
    )
}

$curOk = [Win32CursorNativeV4]::SystemParametersInfo(
    [Win32CursorNativeV4]::SPI_SETCURSORS,
    0,
    [IntPtr]::Zero,
    ([Win32CursorNativeV4]::SPIF_UPDATEINIFILE -bor [Win32CursorNativeV4]::SPIF_SENDCHANGE)
)
if (-not $curOk) {
    [void][Win32CursorNativeV4]::SystemParametersInfo(
        [Win32CursorNativeV4]::SPI_SETCURSORS,
        0,
        [IntPtr]::Zero,
        [Win32CursorNativeV4]::SPIF_SENDCHANGE
    )
}

# Inject native $Size x $Size HCURSORs so screen display and screenshot capture match 1:1
$RoleMap = @(
    @{ Id = [uint32]32512; Path = $NormalPath },   # OCR_NORMAL (Arrow)
    @{ Id = [uint32]32649; Path = $LinkPath },     # OCR_HAND (Hand)
    @{ Id = [uint32]32513; Path = $TextPath },     # OCR_IBEAM (IBeam)
    @{ Id = [uint32]32514; Path = $BusyPath },     # OCR_WAIT (Wait)
    @{ Id = [uint32]32650; Path = $WorkingPath }   # OCR_APPSTARTING (AppStarting)
)

foreach ($entry in $RoleMap) {
    $hCur = [Win32CursorNativeV4]::LoadImage(
        [IntPtr]::Zero,
        $entry.Path,
        [Win32CursorNativeV4]::IMAGE_CURSOR,
        $Size,
        $Size,
        [Win32CursorNativeV4]::LR_LOADFROMFILE
    )
    if ($hCur -ne [IntPtr]::Zero) {
        [void][Win32CursorNativeV4]::SetSystemCursor($hCur, $entry.Id)
    }
}

Write-Host "[Active] Applied '$SchemeName' v2 at 1:1 native ${Size}x${Size} (DWM scale=1.0x, HCURSOR=${Size}x${Size})!" -ForegroundColor Green
