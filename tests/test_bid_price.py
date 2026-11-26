"""Tests for tools/bid_price.py. Numbers here are made-up test values."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import bid_price  # noqa: E402
from bid_price import Line, price_bid  # noqa: E402


def make(kind, cost, market_low=None, trade="t"):
    return Line(trade=trade, kind=kind, cost=cost, market_low=market_low)


def test_self_uses_markup_when_above_market_low():
    r = price_bid([make("self", 1000, 1100)], 0.30, 0.10, 0.10)
    assert r["lines"][0]["price"] == 1300
    assert r["lines"][0]["rule"].startswith("cost +")


def test_self_uses_market_low_when_higher():
    r = price_bid([make("self", 1000, 1500)], 0.30, 0.10, 0.10)
    assert r["lines"][0]["price"] == 1500
    assert r["lines"][0]["rule"] == "market low"


def test_sub_markup():
    r = price_bid([make("sub", 2000)], 0.30, 0.10, 0.05)
    assert r["lines"][0]["price"] == 2200
    assert r["floor_uplift"] == 0


def test_margin_floor_raises_total():
    # Sub-heavy bid: 10% markup gives ~9.1% margin, under a 20% floor.
    r = price_bid([make("sub", 10000)], 0.30, 0.10, 0.20)
    assert r["bid_total"] == 12500
    assert r["floor_uplift"] == 1500
    assert abs(r["final_margin"] - 0.20) < 1e-9


def test_escalation_flag_over_25k():
    r = price_bid([make("sub", 30000)], 0.30, 0.10, 0.05)
    assert any("escalate" in f for f in r["flags"])


def test_csv_loading_and_cli(tmp_path, capsys):
    p = tmp_path / "lines.csv"
    p.write_text("trade,kind,cost,market_low\nDemo,self,\"$1,000\",\nPaint,sub,500,\n")
    code = bid_price.main([str(p), "--self-markup", "0.3", "--sub-markup", "0.1", "--margin-floor", "0.1"])
    assert code == 0
    out = capsys.readouterr().out
    assert "BID TOTAL" in out and "1,850.00" in out


def test_bad_kind_rejected(tmp_path, capsys):
    p = tmp_path / "bad.csv"
    p.write_text("trade,kind,cost,market_low\nX,other,1,\n")
    assert bid_price.main([str(p), "--self-markup", "0", "--sub-markup", "0", "--margin-floor", "0"]) == 2
