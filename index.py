#!/usr/bin/env python3
import argparse
from dataclasses import dataclass

@dataclass
class MarketSnapshot:
    price: float
    cvd: float
    old: float

def analyze(snapshot: MarketSnapshot) -> dict:
    """
    Very simple heuristic:
    - Large positive CVD without price follow-through -> potential downside (sell bias)
    - Large negative CVD without price follow-through -> potential upside (buy bias)
    - OLD >> 0 above price -> potential short squeeze up
    - OLD >> 0 below price -> potential liquidity grab down
    Thresholds are illustrative and should be calibrated.
    """
    signal = "Neutral"
    reasons = []

    # Heuristic thresholds (tune to your own data scale)
    pos_cvd_th = 30_000_000
    neg_cvd_th = -30_000_000
    big_old_th = 1_000  # example scale

    if snapshot.cvd >= pos_cvd_th:
        reasons.append("CVD is strongly positive; watch for lack of price follow-through")
        signal = "Sell bias"
    elif snapshot.cvd <= neg_cvd_th:
        reasons.append("CVD is strongly negative; watch for lack of price follow-through")
        signal = "Buy bias"

    if snapshot.old >= big_old_th:
        reasons.append("Significant liquidity delta detected (OLD high)")
        if signal == "Neutral":
            signal = "Potential move"

    return {
        "price": snapshot.price,
        "cvd": snapshot.cvd,
        "old": snapshot.old,
        "signal": signal,
        "notes": reasons or ["No strong signals detected"]
    }

def main():
    parser = argparse.ArgumentParser(description="BTC Market Watcher (starter)")
    parser.add_argument("--price", type=float, required=True, help="Current BTC price")
    parser.add_argument("--cvd", type=float, required=True, help="Cumulative Volume Delta")
    parser.add_argument("--old", type=float, required=True, help="Orderbook Liquidity Delta (scale-specific)")
    args = parser.parse_args()

    snap = MarketSnapshot(price=args.price, cvd=args.cvd, old=args.old)
    result = analyze(snap)
    print("=== BTC Market Watcher (starter) ===")
    print(f"Price: {result['price']}")
    print(f"CVD:   {result['cvd']}")
    print(f"OLD:   {result['old']}")
    print(f"Signal: {result['signal']}")
    print("Notes:")
    for n in result["notes"]:
        print(f" - {n}")

if __name__ == "__main__":
    main()
