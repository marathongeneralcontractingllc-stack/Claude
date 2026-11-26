#!/usr/bin/env python3
"""Print a Claude Desktop config (absolute paths) for the Marathon MCP servers.
Paste the output into claude_desktop_config.json (Settings > Developer > Edit Config)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, ".mcp.json")))
for s in cfg["mcpServers"].values():
    if s["command"].startswith("vendor/"): s["command"] = os.path.join(ROOT, s["command"])
    s["args"] = [os.path.join(ROOT, a) if a.startswith("vendor/") or a == "marathon" else (ROOT if a == "." else a) for a in s.get("args", [])]
    if "MEMORY_FILE_PATH" in s.get("env", {}): s["env"]["MEMORY_FILE_PATH"] = os.path.join(ROOT, "marathon/memory/marathon-memory.jsonl")
print(json.dumps(cfg, indent=2))
