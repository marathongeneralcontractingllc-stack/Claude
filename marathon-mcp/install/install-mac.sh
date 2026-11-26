#!/bin/bash
# Marathon GC - Claude Desktop MCP installer (Mac)
# In Terminal:  bash install-mac.sh
# Optional:     GOOGLE_MAPS_API_KEY=your-key bash install-mac.sh
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "Installing Node.js with Homebrew..."
    brew install node
  else
    echo "Node.js is not installed. Get the LTS installer from https://nodejs.org, then run this again."
    exit 1
  fi
fi

major=$(node --version | sed 's/^v//' | cut -d. -f1)
if [ "$major" -lt 20 ]; then
  echo "Node.js $major is too old. Install Node 20 or newer from https://nodejs.org and run this again."
  exit 1
fi

node merge-config.js
echo "Done. Quit Claude Desktop (Cmd+Q) and reopen it."
