# tic-tac-to

A small Python project containing a Tic-Tac-Toe example. This repository contains a minimal script in `src/main.py` and a notebook `src/test.ipynb` for experimentation.

## What this is

This is a lightweight starter project for experimenting with a Tic-Tac-Toe implementation in Python. It intentionally keeps dependencies minimal so you can run it quickly.

## Requirements

- Python 3.8 or newer
- Streamlit (see "How to run" for installation)

## Project structure

- `src/`
  - `main.py` - core Tic-Tac-Toe game logic
  - `app.py` - Streamlit web UI for playing the game
  - `test.ipynb` - notebook for experiments and manual testing
- `requirements.txt` - Python dependencies (streamlit)

## How to run

### Setup (first time only)

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Streamlit UI

From the repository root, run:

```bash
streamlit run src/app.py
```

This opens an interactive web app where you can click on board cells to play the game.

### Run the command-line version

If you want to play in the terminal instead (if a CLI script exists):

```bash
python3 src/main.py
```

## Expected behavior

The `src/main.py` script is the entry point. It should run without external dependencies. If it requires input or has additional documentation, check the top of the file for usage instructions.

## Development

- Edit code in `src/`.
- Add small unit tests (for example using pytest) under a `tests/` folder.

## Contributing

Contributions are welcome. Open an issue first if the change is non-trivial. Keep changes small and well-documented.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


