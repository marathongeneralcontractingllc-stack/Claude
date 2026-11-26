# Marathon GC - Claude Desktop MCP installer (Windows)
# Right-click this file > "Run with PowerShell".
# Optional: set your Google Maps key first in the same window:
#   $env:GOOGLE_MAPS_API_KEY = "your-key"

$ErrorActionPreference = "Stop"

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "Node.js is not installed. Installing Node.js LTS with winget..."
    winget install -e --id OpenJS.NodeJS.LTS --accept-source-agreements --accept-package-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

$major = [int]((node --version).TrimStart("v").Split(".")[0])
if ($major -lt 20) {
    Write-Host "Node.js $major is too old. Install Node 20 or newer from https://nodejs.org and run this again."
    exit 1
}

node "$PSScriptRoot\merge-config.js"

Write-Host "Done. Quit Claude Desktop from the system tray (not just the window) and reopen it."
Read-Host "Press Enter to close"
