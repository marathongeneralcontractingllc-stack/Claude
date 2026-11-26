#!/usr/bin/env bash
# Marathon status line: model, folder, git branch, context used.
# A small version of the ideas in ccstatusline / Claude HUD (awesome-claude-code).
input=$(cat)
get() { printf '%s' "$input" | python3 -c "import json,sys
d=json.load(sys.stdin)
for k in sys.argv[1].split('.'):
    d=d.get(k,{}) if isinstance(d,dict) else {}
print(d if d!={} else '')" "$1" 2>/dev/null; }
model=$(get model.display_name)
dir=$(basename "$(get workspace.current_dir)")
pct=$(get context_window.used_percentage)
branch=$(git -C "$(get workspace.current_dir)" branch --show-current 2>/dev/null)
line="🏗  Marathon GC | ${model:-Claude} | ${dir}"
[ -n "$branch" ] && line="$line | ⎇ $branch"
[ -n "$pct" ] && line="$line | ctx ${pct%.*}%"
printf '%s' "$line"
