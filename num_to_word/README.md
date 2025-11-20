# Number to Words Converter

A Python project that converts numbers into their English word representations.

## Overview

This project provides a function that takes a numerical value and returns its English word equivalent. For example:
- `6045000` → "six million forty five thousand"
- `1234567890` → "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"
- `19` → "nineteen"

## Project Structure

```
num_to_word/
├── README.md
├── src/
│   ├── constant.py      # Constants: UNDER_TWENTY, teen_words, above_one_hundred
│   ├── main.py          # Main function: number_to_words()
│   └── __pycache__/     # Python cache
```

## Files Description

### `src/constant.py`
Contains three constants used for the conversion:
- **UNDER_TWENTY**: List of words for numbers 0-19
  - `['zero', 'one', 'two', 'three', ..., 'nineteen']`
- **teen_words**: List for tens place (20, 30, 40, ..., 90)
  - `['', '', 'twenty', 'thirty', 'forty', ..., 'ninety']`
- **above_one_hundred**: Dictionary for larger scale units
  - `{100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}`

### `src/main.py`
Contains the `number_to_words(n)` function that:
1. Handles numbers 0-19 using UNDER_TWENTY list
2. Handles numbers 20-99 by combining tens and ones
3. Handles numbers ≥100 recursively using above_one_hundred dictionary
4. Includes test cases and assertions for validation

## Usage

```python
from src.main import number_to_words

# Convert single numbers
print(number_to_words(6045000))      # six million forty five thousand
print(number_to_words(1234567890))   # one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety
print(number_to_words(85))           # eighty five
print(number_to_words(1001))         # one thousand one
```

## Running the Project

```bash
python src/main.py
```

This will:
- Print example conversions for various numbers
- Run assertion tests to verify correctness
- Display "All test cases passed!" if successful

## Test Cases

The project includes the following test cases:
- `number_to_words(1234567890)` → "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"
- `number_to_words(19)` → "nineteen"
- `number_to_words(85)` → "eighty five"
- `number_to_words(300)` → "three hundred"
- `number_to_words(1001)` → "one thousand one"
- `number_to_words(1000000)` → "one million"

## Algorithm

The `number_to_words()` function uses a recursive approach:

1. **Base case (0-19)**: Return the word directly from UNDER_TWENTY
2. **Tens (20-99)**: Combine tens word with ones digit
3. **Hundreds and above**: 
   - Find the largest scale unit less than or equal to the number
   - Recursively convert the quotient and add the scale name
   - If remainder exists, recursively convert and append it

## Requirements

- Python 3.x
- No external dependencies required

## Author

Project created for number-to-word conversion demonstration.