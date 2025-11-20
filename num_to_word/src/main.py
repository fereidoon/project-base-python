from src.constant import UNDER_TWENTY, teen_words, above_one_hundred


def number_to_words(n):
    if 0 <= n < 20:
        return UNDER_TWENTY[n]
    elif 20 <= n < 100:
        return teen_words[(n // 10)] + ('' if n % 10 == 0 else ' ' + UNDER_TWENTY[n % 10])
    elif n >= 100:
        for key in sorted(above_one_hundred.keys(), reverse=True):
            if n >= key:
                return number_to_words(n // key) + ' ' + above_one_hundred[key] + ('' if n % key == 0 else ' ' + number_to_words(n % key))

if __name__ == "__main__":
    print(number_to_words(6045000))  # Example usage
    print(number_to_words(1234567890))  # Example usage
    print(number_to_words(19))  # Example usage
    print(number_to_words(85))  # Example usage
    print(number_to_words(300))  # Example usage
    print(number_to_words(1001))  # Example usage
    print(number_to_words(1000000))  # Example usage
    assert number_to_words(1234567890) == "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"
    assert number_to_words(19) == "nineteen"
    assert number_to_words(85) == "eighty five"
    assert number_to_words(300) == "three hundred"
    assert number_to_words(1001) == "one thousand one"
    assert number_to_words(1000000) == "one million"
    print("All test cases passed!")