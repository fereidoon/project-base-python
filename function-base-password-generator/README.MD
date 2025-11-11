# Function-based Password Generator

Small utility project providing simple password and PIN generation helpers.

## Files

- `src/password_generator.py` — implements:
  - `pin_generator`
  - `password_generator`
  - `memorable_password_genetator`

## Setup

1. Create a virtual environment (recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```
2. Install dependencies:
   ```sh
   pip install -r requirments.txt
   ```
3. Download the NLTK words corpus (required for memorable passwords):
   ```sh
   python -m nltk.downloader words
   ```

## Streamlit UI

- A simple web UI is provided at `src/streamlit-ui-app.py` which wraps the password generators in an interactive interface.
- Install Streamlit (if not already installed):
  ```sh
  pip install streamlit
  ```
  If you want Streamlit to be part of the project dependencies, add `streamlit` to `requirments.txt`.
- Run the app locally:
  ```sh
  streamlit run src/streamlit-ui-app.py
  ```
- UI features:
  - PIN Generator: choose length (4–12) and generate numeric PINs.
  - Random Password Generator: choose length (8–24) and toggle punctuation and numbers.
  - Memorable Password Generator: choose number of words, separator, and optional random capitalization (uses the NLTK `words` corpus).
  - The app displays a banner image located at `src/image/banner.jpeg` — make sure this file exists if you change the working directory.

## Usage examples

- Run the CLI script:
  ```sh
  python src/password_generator.py
  ```
- Import functions in your code:
  ```py
  from src.password_generator import pin_generator, password_generator, memorable_password_genetator

  print(pin_generator(6))
  print(password_generator(12, punctuation=True, numbers=True))
  print(memorable_password_genetator(4, seperator='_', capitilaze=False))
  ```

## Notes

- The NLTK `words` corpus can be large; running the downloader once per environment is sufficient.
- If you prefer to include Streamlit in the project's requirements, add `streamlit` to `requirments.txt`.
- The function names and parameter names in `src/password_generator.py` are used as-is; review for spelling if you want different names (for example `memorable_password_genetator` contains a typo).

---

## About the author

With a Master's degree in Information Technology and over 20 years of experience as a Network Administrator, the author brings deep expertise in network design, deployment, and operations. They are currently transitioning into software development as a Junior Python Developer and actively building practical skills in Python programming, automation, and machine learning.

The author welcomes collaborations and opportunities in Python development—especially projects related to network automation, system administration tooling, or machine learning applications. Let's connect and build useful, reliable tools together.

Skills:

- Network Administration & Management
- Python Programming
- Machine Learning
- IT Infrastructure & System Administration
- Open to collaborations, mentorship, and freelance opportunities in the Python ecosystem

Feel free to reach out via email at [ferydoon@gmail.com]

