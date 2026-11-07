<#
.SYNOPSIS
    Uninstalls the "Nemunemu Calico" (ねむねむ三毛ネコ) cursor scheme and restores previous Windows cursors.
.DESCRIPTION
    Restores HKCU:\Control Panel\Cursors from %LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json
    if available, or resets to the Windows Default Aero cursor scheme, removes the custom scheme registration,
    and invokes Win32 SystemParametersInfo (SPI_SETCURSORS) to apply the restoration immediately.
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

$InstallDir = Join-Path $env:LOCALAPPDATA "Cursors\NemunemuCalico"
$BackupFile = Join-Path $InstallDir "backup-cursors.json"
$CursorsRegPath = "HKCU:\Control Panel\Cursors"
$SchemesRegPath = "HKCU:\Control Panel\Cursors\Schemes"

if (Test-Path $BackupFile) {
    $backup = Get-Content -Path $BackupFile -Raw -Encoding UTF8 | ConvertFrom-Json
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
    Write-Host "[Restore] Restored original cursor configuration from: $BackupFile" -ForegroundColor Cyan
} else {
    Set-ItemProperty -Path $CursorsRegPath -Name "(default)" -Value $DefaultWinScheme
    New-ItemProperty -Path $CursorsRegPath -Name "Scheme Source" -Value 2 -PropertyType DWord -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Arrow" -Value "C:\WINDOWS\cursors\aero_arrow.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Hand" -Value "C:\WINDOWS\cursors\aero_link.cur" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "IBeam" -Value "" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "Wait" -Value "C:\WINDOWS\cursors\aero_busy.ani" -PropertyType ExpandString -Force | Out-Null
    New-ItemProperty -Path $CursorsRegPath -Name "AppStarting" -Value "C:\WINDOWS\cursors\aero_working.ani" -PropertyType ExpandString -Force | Out-Null
    Write-Host "[Restore] Reset cursor configuration to Windows Default (Aero)." -ForegroundColor Cyan
}

if (Test-Path $SchemesRegPath) {
    Remove-ItemProperty -Path $SchemesRegPath -Name $SchemeName -ErrorAction SilentlyContinue
}

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
    [void][Win32CursorNative]::SystemParametersInfo(
        [Win32CursorNative]::SPI_SETCURSORS,
        0,
        [IntPtr]::Zero,
        [Win32CursorNative]::SPIF_SENDCHANGE
    )
}

if (-not $KeepFiles -and (Test-Path $InstallDir)) {
    Remove-Item -Path $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "[Cleanup] Removed installed cursor directory: $InstallDir" -ForegroundColor Green
}

Write-Host "[Done] Original Windows mouse cursors have been restored immediately." -ForegroundColor Green
