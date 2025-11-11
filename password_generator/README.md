git clone https://github.com/fereidoon/password_generator.git
# Password Generator

A comprehensive Python application that provides three types of password generators with both a library interface and an interactive Streamlit web UI:

- PIN passwords (customizable numeric PINs)
- Random passwords (configurable length, punctuation, digits)
- Memorable passwords (word-based passwords with custom separators and capitalization)

This project combines secure password generation algorithms with a user-friendly web interface, making it easy to generate different types of credentials based on your security needs.

## Features

- PinGenerator: create numeric PINs of arbitrary length
- RandomPasswordGenerator: create random strings from letters, digits and punctuation
- MemorablePasswordGenetator: create human-friendly passwords from word lists (NLTK words or custom vocabulary)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fereidoon/password_generator.git
cd password_generator
```

2. Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# If you plan to run the Streamlit UI, also install streamlit:
pip install streamlit
```

3. NLTK word corpus (only required for the memorable generator when using the default vocabulary):

```python
import nltk
nltk.download('words')
```

The repository includes `requirements.txt` (contains `nltk`). Add `streamlit` if you want to run the UI.

## Usage

All generators implement a `generate()` method. Import them from `src.PassGeneratorClass`.

### PIN Password Generator

```python
from src.PassGeneratorClass import PinGenerator

pin_gen = PinGenerator(length=6)
print(pin_gen.generate())  # e.g. 839201
```

### Random Password Generator

```python
from src.PassGeneratorClass import RandomPasswordGenerator

# length, include_punctuation, include_numbers
rand_gen = RandomPasswordGenerator(length=12, include_punctuation=True, include_numbers=True)
print(rand_gen.generate())
```

### Memorable Password Generator

```python
from src.PassGeneratorClass import MemorablePasswordGenetator

# number_of_words, seperator, capitilaze, vocabulary
mem_gen = MemorablePasswordGenetator(number_of_words=3, seperator='-', capitilaze=True)
print(mem_gen.generate())  # e.g. "garden-Tree-river"
```

Important Notes:
- The `MemorablePasswordGenetator` uses the NLTK words corpus by default if no `vocabulary` is provided
- First-time setup requires downloading the NLTK word list:
  ```python
  import nltk
  nltk.download('words')
  ```
- All generators are thread-safe and can be used in concurrent applications
- The Streamlit UI automatically handles NLTK word corpus initialization

## Streamlit Web Interface

The project includes an interactive web interface (`src/streamlit_ui_app.py`) that provides a user-friendly way to generate passwords. Features include:

- Clean, intuitive UI with method selection dropdown
- Visual banner and clear instructions
- Real-time password generation
- Method-specific controls:
  - PIN Generator: Length slider (4-12 digits)
  - Random Password: Length slider (8-32 characters), toggles for punctuation and numbers
  - Memorable Password: Word count slider (2-6 words), custom separator, random capitalization option

To run the web interface:

```bash
# Install dependencies (if not done already)
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run src/streamlit_ui_app.py
```

This will open your default browser to the password generator interface. The app provides immediate feedback and copies generated passwords in a formatted display.

## Project Structure

```
.
├─ README.md              # project documentation
├─ requirements.txt       # project dependencies (nltk, streamlit)
├─ src/
│  ├─ PassGeneratorClass.py  # core generator implementations
│  ├─ streamlit_ui_app.py    # web interface implementation
│  └─ image/
│      └─ banner.jpeg        # UI banner image
```

The project follows a clean, modular structure:
- Core password generation logic in `PassGeneratorClass.py`
- Web interface separated in `streamlit_ui_app.py`
- Dependencies clearly specified in `requirements.txt`

## About the author

With a Master's degree in Information Technology (specializing in Machine Learning) and over 20 years of experience as a Network Administrator, I bring deep expertise in network design, deployment, and operations. I am currently transitioning into software development as a Junior Python Developer and actively building practical skills in Python programming, automation, and machine learning.

I welcome collaborations and opportunities in Python development—especially projects related to network automation, system administration tooling, or machine learning applications. Let's connect and build useful, reliable tools together.

Skills:
- Network Administration & Management
- Python Programming
- Machine Learning
- IT Infrastructure & System Administration

Open to collaborations, mentorship, and freelance opportunities in the Python ecosystem.

## Contributing

Contributions, bug reports, and improvements are welcome. Please open an issue or submit a pull request.

## License

This project is provided under the MIT License.