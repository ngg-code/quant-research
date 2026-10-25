# quant-research

A Python research library for systematic equity strategies, built project by project:
data pipeline, backtests, factor models and an AI signal.

## Projects
| # | Project | Status |
|---|---------|--------|
| 1 | Data pipeline and benchmark (Capital IQ, Ken French, FRED) | In progress |

## Data
Licensed data (S&P Capital IQ) is **not** included in this repo.
Raw exports go in `data/raw/`, which Git ignores. See `docs/data_access.md`.

## Setup
    python3 -m venv .venv && source .venv/bin/activate
    pip install -e ".[dev]"
    pytest

## Layout
    src/qresearch/   library code (data, metrics)
    tests/           pytest tests
    notebooks/       analysis notebooks
    configs/         settings (tickers, dates, paths)
    docs/            data notes and research log