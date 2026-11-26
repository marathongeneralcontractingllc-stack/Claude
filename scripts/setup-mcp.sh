#!/usr/bin/env bash
# Installs and builds the official MCP reference servers for Marathon GC.
# Re-runnable: pulls the pinned commit, builds TypeScript servers, syncs Python venvs,
# and pre-installs Readability.js so the fetch server never installs at runtime.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/vendor/mcp-servers"
PIN="${MCP_SERVERS_REF:-c799c8552b0f27b7a33a7b9233773da144dddcf5}"

need() { command -v "$1" >/dev/null || { echo "Missing $1 — install it first." >&2; exit 1; }; }
need git; need node; need npm; need uv

if [ ! -d "$DEST/.git" ]; then
  git clone https://github.com/modelcontextprotocol/servers.git "$DEST"
fi
git -C "$DEST" fetch --depth 1 origin "$PIN" 2>/dev/null || git -C "$DEST" fetch origin
git -C "$DEST" checkout -q "$PIN"

echo "==> Building TypeScript servers (filesystem, memory, sequential-thinking, everything)"
(cd "$DEST" && npm ci --no-audit --no-fund && npm run build)

echo "==> Syncing Python servers (fetch, git, time)"
for s in fetch git time; do (cd "$DEST/src/$s" && uv sync --frozen --no-dev); done

echo "==> Pre-installing Readability.js for higher-quality page extraction"
RJS="$("$DEST/src/fetch/.venv/bin/python" -c 'import os,readabilipy;print(os.path.join(os.path.dirname(readabilipy.__file__),"javascript"))')"
(cd "$RJS" && npm install --no-audit --no-fund)

mkdir -p "$ROOT/marathon/memory"
echo "==> Done. Run scripts/test-mcp.sh to verify every server."
