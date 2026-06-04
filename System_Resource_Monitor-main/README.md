# System Resource Monitor

A lightweight Streamlit app to monitor system performance in real time with animated charts and alerts.

## Features

- Live CPU usage (%), memory usage (%), and disk usage (%)
- Animated CPU/Memory usage chart (20-point rolling window)
- High usage alerts (`> 80%`) for CPU and memory
- Top processes table with CPU/memory and thread counts
- Page replacement simulator (FIFO and LRU) for virtual memory teaching/demo
- Auto-refresh every 2 seconds using `st.rerun()`

## Tech stack

- Python 3.12
- [Streamlit](https://streamlit.io)
- [psutil](https://github.com/giampaolo/psutil)
- pandas
- matplotlib (optional, for plot layer legacy)

## Getting started

1. Clone the repo:

```bash
git clone https://github.com/BhargavDevi/System_Resource_Monitor.git
cd System_Resource_Monitor
```

2. Create and activate virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, run:

```bash
pip install streamlit psutil pandas matplotlib
```

4. Run app:

```bash
streamlit run app.py
```

5. Open browser url shown by Streamlit (usually http://localhost:8501)

## Usage

- Watch live CPU/Memory graph and metrics update every 2 seconds
- Check `High CPU` / `High Memory` alerts
- Explore top processes by CPU usage
- Use the Page Replacement section:
  - Enter page references (space-separated)
  - Set frame count
  - See FIFO/LRU page faults

## File structure

- `app.py` – main Streamlit app
- `README.md` – project documentation
- `requirements.txt` – Python dependencies (recommended)

##  Optional improvements

- Add `plotly` interactive charts
- Add multi-core CPU line series per logical core
- Add historical data persistence (CSV/DB)
- Add GPU monitoring (if available)

##  Notes

- Access to some process/memory details may require elevated permissions on some OSes.
- On macOS, Streamlit hot reload may require running from a writable folder.

---

Made by [BhargavDevi](https://github.com/BhargavDevi)