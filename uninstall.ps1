<#
.SYNOPSIS
    Uninstalls the "Nemunemu Calico" (ねむねむ三毛ネコ) cursor scheme and restores previous Windows cursors and size.
.DESCRIPTION
    Restores HKCU:\Control Panel\Cursors and CursorBaseSize / Accessibility\CursorSize from
    %LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json if available, or resets to
    Windows Default (32px), removes the custom scheme registration, and invokes Win32
    SystemParametersInfo (SPI_SETCURSORSIZE + SPI_SETCURSORS) to apply immediately.
#>
[CmdletBinding()]
param(
    [switch]$KeepFiles
)

$ErrorActionPreference = "Stop"

$SchemeName = -join @(
    [char]0x306D, [char]0x3080, [char]0x306D, [char]0x3080,
    [char]0x4E09, [char]0x6BDB, [char]0x30CD, [char]0x30B3
) + " (Nemunemu Calico)"

$DefaultWinScheme = "Windows " + (-join @([char]0x6A19, [char]0x6E96))

$InstallDir     = Join-Path $env:LOCALAPPDATA "Cursors\NemunemuCalico"
$BackupFile     = Join-Path $InstallDir "backup-cursors.json"
$CursorsRegPath = "HKCU:\Control Panel\Cursors"
$SchemesRegPath = "HKCU:\Control Panel\Cursors\Schemes"
$AccessRegPath  = "HKCU:\Software\Microsoft\Accessibility"

$RestoreBaseSize   = 32
$RestoreAccessSize = 1

if (Test-Path $BackupFile) {
    $backup = Get-Content -Path $BackupFile -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($null -ne $backup.OriginalCursorBaseSize) {
        $RestoreBaseSize = [int]$backup.OriginalCursorBaseSize
    }
    if ($null -ne $backup.OriginalAccessibilityCursorSize) {
        $RestoreAccessSize = [int]$backup.OriginalAccessibilityCursorSize
    }
    Set-ItemProperty -Path $CursorsRegPath -Name "(default)" -Value ([string]$backup.DefaultValue)
    foreach ($prop in $backup.Values.PSObject.Properties) {
        $name = $prop.Name
        $val = $prop.Value
        if ($val -is [int] -or $val -is [long]) {
            New-ItemProperty -Path $CursorsRegPath -Name $name -Value ([int]$val) -PropertyType DWord -Force | Out-Null
        } else {
            New-ItemProperty -Path $CursorsRegPath -Name $name -Value ([string]$val) -PropertyType ExpandString -Force | Out-Null
        }
    }
    New-ItemProperty -Path $CursorsRegPath -Name "CursorBaseSize" -Value $RestoreBaseSize -PropertyType DWord -Force | Out-Null
    Write-Host "[Restore] Restored original cursor configuration from: $BackupFile" -ForegroundColor Cyan
} else {
    Set-ItemProperty -Path $CursorsRegPath -Name "(default)" -Value $DefaultWinScheme
    New-ItemProperty -Path $CursorsRegPath -Name "Scheme Source" -Value 2 -PropertyType DWord -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "CursorBaseSize" -Value 32 -PropertyType DWord -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Arrow" -Value "C:\WINDOWS\cursors\aero_arrow.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Hand" -Value "C:\WINDOWS\cursors\aero_link.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "IBeam" -Value "" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Wait" -Value "C:\WINDOWS\cursors\aero_busy.ani" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "AppStarting" -Value "C:\WINDOWS\cursors\aero_working.ani" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Crosshair" -Value "" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "No" -Value "C:\WINDOWS\cursors\aero_unavail.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "SizeNS" -Value "C:\WINDOWS\cursors\aero_ns.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "SizeWE" -Value "C:\WINDOWS\cursors\aero_ew.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "SizeAll" -Value "C:\WINDOWS\cursors\aero_move.cur" -PropertyType ExpandString -Force | Out-Null
    Write-Host "[Restore] Reset cursor configuration to Windows Default (Aero, 32px)." -ForegroundColor Cyan
}

if (Test-Path $AccessRegPath) {
    New-ItemProperty -Path $AccessRegPath -Name "CursorSize" -Value $RestoreAccessSize -PropertyType DWord -Force | Out-Null
}

if (Test-Path $SchemesRegPath) {
    Remove-ItemProperty -Path $SchemesRegPath -Name $SchemeName -ErrorAction SilentlyContinue
}

if (-not ("Win32CursorNativeV2" -as [type])) {
    Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public static class Win32CursorNativeV2 {
    public const uint SPI_SETCURSORS = 0x0057;
    public const uint SPI_SETCURSORSIZE = 0x2029;
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

$sizeOk = [Win32CursorNativeV2]::SystemParametersInfo(
    [Win32CursorNativeV2]::SPI_SETCURSORSIZE,
    0,
    [IntPtr]$RestoreBaseSize,
    ([Win32CursorNativeV2]::SPIF_UPDATEINIFILE -bor [Win32CursorNativeV2]::SPIF_SENDCHANGE)
)
if (-not $sizeOk) {
    [void][Win32CursorNativeV2]::SystemParametersInfo(
        [Win32CursorNativeV2]::SPI_SETCURSORSIZE,
        0,
        [IntPtr]$RestoreBaseSize,
        [Win32CursorNativeV2]::SPIF_SENDCHANGE
    )
}

$curOk = [Win32CursorNativeV2]::SystemParametersInfo(
    [Win32CursorNativeV2]::SPI_SETCURSORS,
    0,
    [IntPtr]::Zero,
    ([Win32CursorNativeV2]::SPIF_UPDATEINIFILE -bor [Win32CursorNativeV2]::SPIF_SENDCHANGE)
)
if (-not $curOk) {
    [void][Win32CursorNativeV2]::SystemParametersInfo(
        [Win32CursorNativeV2]::SPI_SETCURSORS,
        0,
        [IntPtr]::Zero,
        [Win32CursorNativeV2]::SPIF_SENDCHANGE
    )
}

if (-not $KeepFiles -and (Test-Path $InstallDir)) {
    Remove-Item -Path $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "[Cleanup] Removed installed cursor directory: $InstallDir" -ForegroundColor Green
}

Write-Host "[Done] Original Windows mouse cursors and size (${RestoreBaseSize}px) have been restored immediately." -ForegroundColor Green
