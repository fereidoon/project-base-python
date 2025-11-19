
# Currency Converter

Simple Python project that fetches exchange rates from ExchangeRate-API and provides a small Streamlit UI to convert between currencies.

**What it does:**
- Fetches exchange rates from `https://v6.exchangerate-api.com`.
- Lists supported currency codes and names.
- Converts an amount from one currency to another and shows how long ago the rate was updated (e.g., "19 hours ago").

**Files:**
- `src/main.py`: core functions for calling the API, converting values, and computing relative times.
- `src/app.py`: Streamlit app entrypoint.
- `src/test.ipynb`: notebook examples and quick testing cells.

**Requirements:**
- Python 3.8+
- `requests` and `streamlit` (install via `pip`)

**Install dependencies:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```bash
pip install requests streamlit
```

**Set your API key**
- The project uses ExchangeRate-API. Set your API key in the environment (replace `YOUR_KEY`):
```bash
export EXCHANGERATE_API_KEY=YOUR_KEY
```
Or edit the code where `api_key` is defined in `src/main.py` / `src/test.ipynb` (not recommended for production).

**Run the Streamlit app:**
```bash
cd src
streamlit run app.py
# Currency Converter

Small Python project that fetches exchange rates from ExchangeRate-API and provides:
- a simple CLI converter (`src/main.py`) and
- a Streamlit UI (`src/app.py`).

Features
- Fetches exchange rates using ExchangeRate-API's standard endpoint.
- Lists supported currency codes and names (via the `codes` endpoint).
- Converts amounts and displays how long ago the rates were updated (e.g., "19 hours ago").

Repository layout
- `src/main.py` — core functions (API calls, conversion logic, relative time helper).
- `src/app.py` — Streamlit application.
- `src/test.ipynb` — notebook with quick API experiments and examples.

Prerequisites
- Python 3.8 or later
- Network access to `https://v6.exchangerate-api.com`

Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you prefer installing manually:
```bash
pip install requests streamlit python-dotenv
```

Configuration — API key
1. Sign up at ExchangeRate-API and obtain an API key.
2. Set the environment variable (recommended):

Linux / macOS
```bash
export EXCHANGERATE_API_KEY="YOUR_KEY_HERE"
```

Windows PowerShell
```powershell
$env:EXCHANGERATE_API_KEY = "YOUR_KEY_HERE"
```

Note: The code currently contains a placeholder API key in a few example cells — it's best not to commit real API keys to source control.

Run the Streamlit app
```bash
cd src
streamlit run app.py
```

CLI usage (quick test)
```bash
python src/main.py
```


