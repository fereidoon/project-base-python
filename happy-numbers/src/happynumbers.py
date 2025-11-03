def happy_number(n):
    """Return True if n is a happy number, False otherwise.
    Requires n to be a positive integer.
    """
    # Reject non-integers and booleans
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(x) ** 2 for x in str(n))
    if n == 1:
        print("this number is happy")
        return True
    else:
        print("this number is not happy")
        return False

if __name__ == "__main__":
    # Example usage
    print(happy_number(19))  # Should print "this number is happy" and return True
    print(happy_number(32))  # Should print "this number is not happy" and return False