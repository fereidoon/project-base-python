# Happy Numbers

Small demo showing a function to check whether a number is a "happy number".

A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. Numbers for which this process ends in 1 are happy numbers.

## Function

`happy_number(n)` (provided in `test.ipynb`)

- Inputs: `n` — must be a positive integer. Booleans are rejected.
- Behavior: raises `TypeError` if `n` is not an `int` (or is a `bool`), raises `ValueError` if `n < 1`.
- Returns: `True` if `n` is happy, `False` otherwise. The function also prints a short message: "this number is happy" or "this number is not happy".

Contract summary:

- Inputs: int (n >= 1)
- Outputs: bool (True when happy)
- Errors: TypeError or ValueError for invalid input

## Examples (in the notebook)

Run these in `test.ipynb` or a Python REPL after loading the function:

```python
happy_number(19)   # prints 'this number is happy' and returns True
happy_number(32)   # prints 'this number is not happy' and returns False
happy_number(1)    # prints 'this number is happy' and returns True
```

Invalid inputs:

```python
happy_number(3.0)  # raises TypeError
happy_number(True) # raises TypeError (bools are rejected)
```
