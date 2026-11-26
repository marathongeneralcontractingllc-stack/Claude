#!/usr/bin/env python3
"""Smoke-test every server in .mcp.json: start it, initialize, list tools, call one tool."""
import json, subprocess, sys, os, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, ".mcp.json")))["mcpServers"]
PROBES = {
  "marathon-files": ("list_allowed_directories", {}),
  "marathon-memory": ("search_nodes", {"query": "Snow"}),
  "sequential-thinking": ("sequentialthinking", {"thought": "test", "thoughtNumber": 1, "totalThoughts": 1, "nextThoughtNeeded": False}),
  "time": ("get_current_time", {"timezone": "America/New_York"}),
  "git": ("git_status", {"repo_path": ROOT}),
  "fetch": ("fetch", {"url": os.environ.get("FETCH_TEST_URL", "https://marathongeneralcontracting.com"), "max_length": 300}),
}
def rpc(p, i, method, params=None):
    msg = {"jsonrpc": "2.0", "method": method, **({"id": i} if i else {}), **({"params": params} if params is not None else {})}
    p.stdin.write(json.dumps(msg) + "\n"); p.stdin.flush()
    if not i: return None
    while True:
        line = p.stdout.readline()
        if not line: raise RuntimeError("server exited")
        r = json.loads(line)
        if r.get("id") == i: return r
fails = 0
for name, s in cfg.items():
    t0 = time.time()
    try:
        p = subprocess.Popen([s["command"], *s.get("args", [])], cwd=ROOT, env={**os.environ, **s.get("env", {})},
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        rpc(p, 1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "marathon-smoke", "version": "1"}})
        rpc(p, None, "notifications/initialized")
        tools = [t["name"] for t in rpc(p, 2, "tools/list", {})["result"]["tools"]]
        tool, args = PROBES[name]
        r = rpc(p, 3, "tools/call", {"name": tool, "arguments": args})
        ok = "result" in r and not r["result"].get("isError")
        snippet = r.get("result", {}).get("content", [{}])[0].get("text", str(r.get("error")))[:90].replace("\n", " ")
        print(f"{'PASS' if ok else 'FAIL'}  {name:20} {len(tools):2} tools  {time.time()-t0:4.1f}s  {tool}: {snippet}")
        fails += not ok
        p.terminate()
    except Exception as e:
        print(f"FAIL  {name:20} {e}"); fails += 1
sys.exit(1 if fails else 0)
