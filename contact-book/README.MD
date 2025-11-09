
# Contact Book — Simple Streamlit CRUD

A minimal contact-book web app built with Streamlit. It demonstrates a tiny CRUD (Create, Read, Update, Delete) UI that uses a local Python class (`ContactBook`) defined in `src/main.py`.

## What this repository contains

- `src/app.py` — Streamlit UI (entrypoint for the app)
- `src/main.py` — ContactBook implementation (data model / logic)

## Requirements

- Python 3.8+
- streamlit

You can install Streamlit into a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install streamlit
```

If you prefer a requirements file, create `requirements.txt` with:

```
streamlit
```
and then run `pip install -r requirements.txt`.

## How to run

There are three reliable ways to run the app depending on how you prefer to structure imports:

1) Recommended (keep code as-is, run from `src`):

```bash
cd src
streamlit run app.py
```

This runs the app with the `src` directory as the script's working directory, so `from main import ContactBook` will work if you change the import accordingly (see troubleshooting below).

2) Keep `app.py` in `src` and use `PYTHONPATH` (no code changes):

```bash
cd /home/test/project-base-python/contact-book
PYTHONPATH=. streamlit run src/app.py
```

This adds the project root to Python's import path so `from src.main import ContactBook` resolves.

3) Move `app.py` to project root (recommended for clarity):

```
mv src/app.py ./app.py
# then run from project root
streamlit run app.py
```

When `app.py` is at project root, `from src.main import ContactBook` will import `src/main.py` reliably.

## Why Streamlit may appear to "hang" on import

When you run `streamlit run src/app.py`, the Python process that Streamlit starts sets the script's directory as the first entry in `sys.path`. That means:

- If you execute `src/app.py` directly, Python's import search path may not include the project root.
- Importing `from src.main import ContactBook` expects `src` to be discoverable as a top-level package on `sys.path`. If it's not present, the import can fail or the Streamlit server may appear unresponsive while it tries to import modules.

Common fixes:

- Add an explicit `src/__init__.py` to make `src` a package and run with `PYTHONPATH` or move `app.py` to project root.
- Use `PYTHONPATH=. streamlit run src/app.py` from the project root so Python can find `src`.
- Alternatively, run the app from inside the `src` directory and change the import to `from main import ContactBook`.
- As a simple workaround, you can prepend the project root to `sys.path` at the top of `src/app.py` (not recommended for long-term projects):

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # project root
```

## Troubleshooting checklist

- If the web UI doesn't load, check the terminal that started Streamlit for import errors or tracebacks.
- If you see `ModuleNotFoundError: No module named 'src'`:
	- Try `PYTHONPATH=. streamlit run src/app.py`, or
	- Move `app.py` to the project root and run `streamlit run app.py`, or
	- Add `src/__init__.py` and run with the project root on `PYTHONPATH`.
- If Streamlit is updated or behaves differently, ensure you're using a compatible Streamlit version.

## Quick example

From the project root, the simplest reliable command that requires no code edits is:

```bash
PYTHONPATH=. streamlit run src/app.py
```

This will start the Streamlit server and ensure `from src.main import ContactBook` resolves correctly.