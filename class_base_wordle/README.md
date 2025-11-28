# Class-Based Wordle

Small word-guessing game inspired by the original Wordle. The core gameplay
loops live in `src/wordle_class.py`, and `src/run.py` wires everything up so
you can launch the interactive terminal experience.

## Project Layout

- `src/wordle_class.py` – game orchestration (word selection, attempt loop,
  feedback flow).
- `src/run.py` – entry point for running the CLI version.
- `utils/util.py` – helper utilities such as the colored feedback renderer.
- `data/words_frequency.txt` – word list with frequency scores used to build
  the candidate pool.
- `requirements.txt` – Python package dependencies.

## Requirements

- Python 3.10+
- Pip + `venv`

Install the Python dependencies once your virtual environment is activated:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows PowerShell
pip install -r requirements.txt
```

## Running the Game

Generate the word pool, pick a random target, and start guessing:

```bash
python -m src.run
```

Alternatively, you can run it directly:

```bash
python src/run.py
```

Gameplay basics:

1. You have seven attempts to guess the five-letter target word.
2. Each guess prints colored tiles (green = correct spot, gray = correct letter
   wrong spot, red = not in the word).
3. Type `q` anytime to quit early.

## Customizing the Experience

- **Attempts:** pass a different `max_attempts` when instantiating `wordle`.
- **Word length or pool size:** call `return_world_list(limt, world_length)`
  before `play_game`.
- **Word list:** swap `data/words_frequency.txt` with any file that contains
  `<word> <frequency>` per line; higher frequency entries are prioritized.

Example snippet:

```python
from src.wordle_class import wordle

game = wordle(max_attempts=10, world_length=6)
game.return_world_list(limit=200, world_length=6)
game.play_game()
```

## Troubleshooting

- Ensure the word list file path is valid if you move files around.
- Terminal colors rely on `termcolor`; if colors do not appear, confirm your
  terminal supports ANSI escape codes.

