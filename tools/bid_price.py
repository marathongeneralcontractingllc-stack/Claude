#!/usr/bin/env python3
"""Price a commercial trade bid using Marathon's markup rules.

No rates or percentages are stored here (this repo is public). Pass them in
from Marathon Brain, Section 4:

  --self-markup   markup on self-performed cost, e.g. 0.25 for cost + 25%
  --sub-markup    markup on firm written sub quotes, e.g. 0.15
  --margin-floor  minimum gross margin on the total bid, e.g. 0.20

Line items come from a CSV with columns:
  trade, kind, cost, market_low
where kind is "self" or "sub". For self-performed lines, market_low is the
local market-low price for that scope (optional); the line price is
max(cost * (1 + self_markup), market_low). For sub lines, cost must be the
firm written sub quote; price = cost * (1 + sub_markup).

If the blended gross margin is below the floor, the total is raised to
total_cost / (1 - margin_floor) and the difference is reported.

Usage:
  python3 tools/bid_price.py lines.csv --self-markup 0.25 --sub-markup 0.15 \
      --margin-floor 0.20 [--json]
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, asdict


@dataclass
class Line:
    trade: str
    kind: str
    cost: float
    market_low: float | None
    price: float = 0.0
    rule: str = ""


def _money(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip().replace("$", "").replace(",", "")
    return float(value) if value else None


def load_lines(path: str) -> list[Line]:
    lines: list[Line] = []
    with open(path, newline="") as handle:
        for n, row in enumerate(csv.DictReader(handle), start=2):
            kind = (row.get("kind") or "").strip().lower()
            if kind not in ("self", "sub"):
                raise ValueError(f"row {n}: kind must be 'self' or 'sub', got {kind!r}")
            cost = _money(row.get("cost"))
            if cost is None or cost < 0:
                raise ValueError(f"row {n}: cost is missing or negative")
            lines.append(Line(
                trade=(row.get("trade") or "").strip() or f"line {n}",
                kind=kind,
                cost=cost,
                market_low=_money(row.get("market_low")),
            ))
    if not lines:
        raise ValueError("no line items found")
    return lines


def price_bid(lines: list[Line], self_markup: float, sub_markup: float,
              margin_floor: float) -> dict:
    if not 0 <= margin_floor < 1:
        raise ValueError("margin floor must be between 0 and 1")
    for line in lines:
        if line.kind == "self":
            marked_up = line.cost * (1 + self_markup)
            if line.market_low is not None and line.market_low > marked_up:
                line.price, line.rule = line.market_low, "market low"
            else:
                line.price, line.rule = marked_up, f"cost + {self_markup:.0%}"
        else:
            line.price, line.rule = line.cost * (1 + sub_markup), f"sub quote + {sub_markup:.0%}"
        line.price = round(line.price, 2)

    total_cost = round(sum(l.cost for l in lines), 2)
    line_total = round(sum(l.price for l in lines), 2)
    margin = (line_total - total_cost) / line_total if line_total else 0.0

    bid_total, floor_uplift = line_total, 0.0
    if margin < margin_floor:
        bid_total = math.ceil(total_cost / (1 - margin_floor) * 100) / 100
        floor_uplift = round(bid_total - line_total, 2)
    final_margin = (bid_total - total_cost) / bid_total if bid_total else 0.0

    flags = []
    if any(l.kind == "sub" and l.cost == 0 for l in lines):
        flags.append("A sub line has $0 cost: get a firm written quote first.")
    if floor_uplift:
        flags.append(f"Blended margin {margin:.1%} was under the {margin_floor:.0%} floor; "
                     f"total raised by ${floor_uplift:,.2f}.")
    if bid_total > 25000:
        flags.append("Bid is over $25,000: escalate to Nick before it goes out.")

    return {
        "lines": [asdict(l) for l in lines],
        "total_cost": total_cost,
        "line_total": line_total,
        "blended_margin": round(margin, 4),
        "floor_uplift": floor_uplift,
        "bid_total": round(bid_total, 2),
        "final_margin": round(final_margin, 4),
        "flags": flags,
    }


def render(result: dict) -> str:
    out = [f"{'Trade':<28}{'Kind':<6}{'Cost':>14}{'Price':>14}  Rule"]
    for l in result["lines"]:
        out.append(f"{l['trade'][:27]:<28}{l['kind']:<6}{l['cost']:>14,.2f}{l['price']:>14,.2f}  {l['rule']}")
    out.append("")
    out.append(f"Total cost      ${result['total_cost']:>14,.2f}")
    out.append(f"Lines total     ${result['line_total']:>14,.2f}  (margin {result['blended_margin']:.1%})")
    if result["floor_uplift"]:
        out.append(f"Floor uplift    ${result['floor_uplift']:>14,.2f}")
    out.append(f"BID TOTAL       ${result['bid_total']:>14,.2f}  (margin {result['final_margin']:.1%})")
    for flag in result["flags"]:
        out.append(f"! {flag}")
    out.append("Draft for Nick's review. Not a price until Nick approves it.")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("csv")
    parser.add_argument("--self-markup", type=float, required=True)
    parser.add_argument("--sub-markup", type=float, required=True)
    parser.add_argument("--margin-floor", type=float, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = price_bid(load_lines(args.csv), args.self_markup, args.sub_markup, args.margin_floor)
    except (ValueError, OSError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.json else render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
