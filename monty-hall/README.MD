# Monty Hall Simulation

A small Monty Hall problem simulator with a Streamlit UI.

This project demonstrates the classic Monty Hall problem and provides a simple interactive Streamlit app to simulate two strategies:

- Switching strategy (contestant switches door after a goat is revealed)
- Staying strategy (contestant keeps their original choice)

Files
------
- `src/monty_hall.py` — core simulation logic
  - `montyhall(user_change_choice: bool) -> bool` — run a single trial; returns True if the final choice was the car.
  - `simulate(switch: bool, num_simulations: int) -> float` — run `num_simulations` trials using the switch/stay strategy and return the win fraction.
- `src/app.py` — Streamlit app

Requirements
------------
- Python 3.8+
- streamlit

Install
-------
Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit
```

If you prefer a requirements file, create `requirements.txt` with `streamlit` and run:

```bash
pip install -r requirements.txt
```

Run the Streamlit app
---------------------
From the project root run:

```bash
streamlit run src/app.py
```

Manual usage (Streamlit UI)
---------------------------
When the app opens in your browser you'll see:

- Title: "Monty Hall Problem Simulation"
- A numeric input labeled "Number of Simulations". Default behavior in this project:
  - Minimum: 100
  - Maximum: 100000
  - Default value: 10000
  - Step: 1000
  Use this field to set how many Monte Carlo trials to run when you click "Run Simulation".

- Two columns:
  - Left column header: "Switching Strategy"
  - Right column header: "Staying Strategy"

- Charts: each column contains a line chart that shows the running win rate as the simulation progresses:
  - "Switch Win Rate" (left)
  - "Stay Win Rate" (right)

- Button: "Run Simulation"
  - Click this to start the simulations. The app runs the number of trials set in the numeric input. Each trial calls the simulation code and the charts are updated with the current win rate.

After the run completes the app prints the final win rates for each strategy under the charts.

Expected results
----------------
With enough simulations you should see:

- Switching strategy win rate ≈ 2/3
- Staying strategy win rate ≈ 1/3

Programmatic API
-----------------
If you want to run simulations from Python code (outside Streamlit), use `src/monty_hall.py`:

```python
from src.monty_hall import montyhall, simulate

# single trial (True => switch, False => stay)
result = montyhall(True)  # returns True if win

# multiple trials (returns win_fraction)
win_fraction = simulate(True, 10000)
```

Notes
-----
- The simulation uses Python's `random` module. If you need deterministic runs for debugging, set `random.seed(...)` inside `src/monty_hall.py` before calling the functions.
- The Streamlit UI and the simulation functions are intentionally simple for clarity and learning.

License
-------
This repository is provided as-is for educational purposes.
