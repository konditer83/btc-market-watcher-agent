# BTC Market Watcher Agent (Starter)

This is a **starter repository** for an agent that analyzes Bitcoin price with **CVD** (Cumulative Volume Delta) and **OLD** (Orderbook Liquidity Delta) and emits simple bias signals.

> ⚠️ **Important:** `agent.json` here is a **placeholder manifest** to help you get started.
> The exact format required by **Recall.xyz** may differ. Adjust the manifest and entry point according to Recall's latest docs.

## What’s inside
- `agent.json` — starter manifest (placeholder).
- `src/index.py` — simple CLI script that computes a bias from inputs.
- `README.md` — this file.
- `.gitignore` — standard Python ignores.
- `LICENSE` — MIT.

## Quick start (local)
1. Ensure you have **Python 3.10+**.
2. Run:
   ```bash
   python src/index.py --price 110300 --cvd -84000 --old 300
   ```
3. You should see a short analysis and a signal.

## Suggested next steps
- Replace the placeholder logic with real data fetching (e.g., from your paid dashboards or APIs).
- Update `agent.json` to match the **Recall.xyz** expected format (entry file, runtime, environment variables, schedule, etc.).
- Add error handling, logging, and tests.
