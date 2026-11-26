#!/usr/bin/env node
// Marathon GC: adds the Marathon MCP servers to Claude Desktop's config.
// Safe to run more than once. Backs up the existing config first and never
// removes servers you already have.
//
// Usage: node merge-config.js            (core servers, no keys needed)
//        GOOGLE_MAPS_API_KEY=... node merge-config.js   (also adds Google Maps)

const fs = require("fs");
const os = require("os");
const path = require("path");

const isWin = process.platform === "win32";
const home = os.homedir();

const configPath = isWin
  ? path.join(process.env.APPDATA || path.join(home, "AppData", "Roaming"), "Claude", "claude_desktop_config.json")
  : process.platform === "darwin"
    ? path.join(home, "Library", "Application Support", "Claude", "claude_desktop_config.json")
    : path.join(home, ".config", "Claude", "claude_desktop_config.json");

// Marathon work folder Claude may read and write. Nothing outside it.
const marathonDir = path.join(home, "Documents", "Marathon");
for (const sub of ["Bids", "Plans", "Job Photos", "Contracts", "Marketing"]) {
  fs.mkdirSync(path.join(marathonDir, sub), { recursive: true });
}

// On Windows, Claude Desktop starts npx more reliably through cmd /c.
function npx(pkg, extra = []) {
  return isWin
    ? { command: "cmd", args: ["/c", "npx", "-y", pkg, ...extra] }
    : { command: "npx", args: ["-y", pkg, ...extra] };
}

const servers = {
  "marathon-files": npx("@modelcontextprotocol/server-filesystem", [marathonDir]),
  "nws-weather": npx("@thx93/mcp-weather-server"),
  "plan-takeoff": npx("opentakeoff-mcp"),
  "lien-guides": npx("liendeadline-mcp"),
  "browser": npx("@playwright/mcp"),
};

if (process.env.GOOGLE_MAPS_API_KEY) {
  servers["google-maps"] = {
    ...npx("@cablate/mcp-google-map"),
    env: { GOOGLE_MAPS_API_KEY: process.env.GOOGLE_MAPS_API_KEY },
  };
}

let config = {};
if (fs.existsSync(configPath)) {
  const raw = fs.readFileSync(configPath, "utf8");
  const stamp = new Date().toISOString().replace(/[:.]/g, "-");
  fs.copyFileSync(configPath, `${configPath}.backup-${stamp}`);
  try {
    config = raw.trim() ? JSON.parse(raw) : {};
  } catch (e) {
    console.error(`Your existing config is not valid JSON, so nothing was changed:\n  ${configPath}\nFix or delete it, then run this again.`);
    process.exit(1);
  }
} else {
  fs.mkdirSync(path.dirname(configPath), { recursive: true });
}

config.mcpServers = config.mcpServers || {};
const added = [], kept = [];
for (const [name, def] of Object.entries(servers)) {
  if (config.mcpServers[name]) kept.push(name);
  else { config.mcpServers[name] = def; added.push(name); }
}

fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");

console.log(`\nClaude Desktop config: ${configPath}`);
console.log(`Marathon folder:       ${marathonDir}`);
if (added.length) console.log(`Added:   ${added.join(", ")}`);
if (kept.length) console.log(`Already there (left as is): ${kept.join(", ")}`);
if (!process.env.GOOGLE_MAPS_API_KEY) console.log("Google Maps skipped (no GOOGLE_MAPS_API_KEY set). See README to add it later.");
console.log("\nNow fully quit Claude Desktop and open it again.\n");
