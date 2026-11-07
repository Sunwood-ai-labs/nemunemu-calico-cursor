<#
.SYNOPSIS
    Installs and immediately activates the "Nemunemu Calico" (ねむねむ三毛ネコ) Windows mouse cursor scheme.
.DESCRIPTION
    Copies the selected cursor size (64, 48, or 32) to %LOCALAPPDATA%\Cursors\NemunemuCalico,
    backs up the existing HKCU:\Control Panel\Cursors registry configuration on first run,
    registers the scheme, updates active cursor paths, and invokes Win32 SystemParametersInfo
    (SPI_SETCURSORS) so the new cursors take effect immediately without signing out.
.PARAMETER Size
    Cursor pixel size to install: 64 (default), 48, or 32.
#>
[CmdletBinding()]
param(
    [ValidateSet(64, 48, 32)]
    [int]$Size = 64
)

$ErrorActionPreference = "Stop"

$SchemeName = -join @(
    [char]0x306D, [char]0x3080, [char]0x306D, [char]0x3080,
    [char]0x4E09, [char]0x6BDB, [char]0x30CD, [char]0x30B3
) + " (Nemunemu Calico)"

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceDir = switch ($Size) {
    64 { Join-Path $RepoRoot "cursors" }
    48 { Join-Path $RepoRoot "cursors\48x48" }
    32 { Join-Path $RepoRoot "cursors\32x32" }
}

if (-not (Test-Path $SourceDir)) {
    throw "Source cursor directory not found: $SourceDir. Run 'uv run scripts/build_cursors.py' first."
}

$InstallDir = Join-Path $env:LOCALAPPDATA "Cursors\NemunemuCalico"
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null

$CursorsRegPath = "HKCU:\Control Panel\Cursors"
$SchemesRegPath = "HKCU:\Control Panel\Cursors\Schemes"
$BackupFile = Join-Path $InstallDir "backup-cursors.json"

# 1. Back up current cursor settings on first run (never overwrite an existing backup)
if (-not (Test-Path $BackupFile)) {
    $regItem = Get-Item -Path $CursorsRegPath
    $backupData = [ordered]@{
        DefaultValue = $regItem.GetValue("", "")
        Values       = [ordered]@{}
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
Write-Host "[Copy] Installed ${Size}x${Size} cursors to: $InstallDir" -ForegroundColor Green

# 3. Register scheme under HKCU:\Control Panel\Cursors\Schemes
if (-not (Test-Path $SchemesRegPath)) {
    New-Item -Path $SchemesRegPath -Force | Out-Null
}

$NormalPath  = Join-Path $InstallDir "nemunemu_normal.ani"
$LinkPath    = Join-Path $InstallDir "nemunemu_link.ani"
$TextPath    = Join-Path $InstallDir "nemunemu_text.ani"
$BusyPath    = Join-Path $InstallDir "nemunemu_busy.ani"
$WorkingPath = Join-Path $InstallDir "nemunemu_working.ani"

# Standard Windows scheme order:
# Arrow,Help,AppStarting,Wait,Crosshair,IBeam,NWPen,No,SizeNS,SizeWE,SizeNWSE,SizeNESW,SizeAll,UpArrow,Hand,Pin,Person
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

# 4. Update active HKCU:\Control Panel\Cursors entries
Set-ItemProperty -Path $CursorsRegPath -Name "(default)" -Value $SchemeName
New-ItemProperty -Path $CursorsRegPath -Name "Scheme Source" -Value 1 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Arrow" -Value $NormalPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Hand" -Value $LinkPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "IBeam" -Value $TextPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "Wait" -Value $BusyPath -PropertyType ExpandString -Force | Out-Null
New-ItemProperty -Path $CursorsRegPath -Name "AppStarting" -Value $WorkingPath -PropertyType ExpandString -Force | Out-Null

# 5. Notify Windows immediately via Win32 SystemParametersInfo (SPI_SETCURSORS = 0x0057)
if (-not ("Win32CursorNative" -as [type])) {
    Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public static class Win32CursorNative {
    public const uint SPI_SETCURSORS = 0x0057;
    public const uint SPIF_UPDATEINIFILE = 0x01;
    public const uint SPIF_SENDCHANGE = 0x02;

    [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
    public static extern bool SystemParametersInfo(
        uint uiAction,
        uint uiParam,
        IntPtr pvParam,
        uint fWinIni
    );
}
"@
}

$ok = [Win32CursorNative]::SystemParametersInfo(
    [Win32CursorNative]::SPI_SETCURSORS,
    0,
    [IntPtr]::Zero,
    ([Win32CursorNative]::SPIF_UPDATEINIFILE -bor [Win32CursorNative]::SPIF_SENDCHANGE)
)
if (-not $ok) {
    $ok = [Win32CursorNative]::SystemParametersInfo(
        [Win32CursorNative]::SPI_SETCURSORS,
        0,
        [IntPtr]::Zero,
        [Win32CursorNative]::SPIF_SENDCHANGE
    )
}

if (-not $ok) {
    Write-Warning "SystemParametersInfo returned false, but registry values were updated."
} else {
    Write-Host "[Active] Applied '$SchemeName' (${Size}x${Size}) immediately via SPI_SETCURSORS!" -ForegroundColor Green
}
