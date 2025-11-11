# Rock Paper Scissors

This repository contains a small Rock–Paper–Scissors game that can be run two ways:

- As a simple command-line game using the included `main.py` script.
- As a Streamlit web UI using `src/streamlit_app.py`.

Prerequisites
-------------

Python 3.8+ and pip are required. Install the dependencies from the project root:

```fish
pip install -r requirements.txt
```

Run the CLI game
----------------

Start the interactive command-line game from the project root:

```fish
python main.py
```

Follow the on-screen prompts to play; enter `q` when asked to quit.

Run the Streamlit app
---------------------

Start the Streamlit UI from the project root:

```fish
streamlit run src/streamlit_app.py
```

The Streamlit app provides a simple UI to choose rock, paper or scissors and plays against the computer.

Notes
-----

- The CLI entrypoint is `main.py`.
- These commands are shown for the fish shell; they work the same in bash/zsh.
