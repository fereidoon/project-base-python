import random
from termcolor import colored


def read_select_word(file_name,target_length = 5,limit = 100):
    words =[]
    with open(file_name) as file:
        for raw_line in file:
            word,freq_str =raw_line.strip().split()
            words.append((word,int(freq_str)))
    words_sorted = sorted(words, key=lambda item: item[1], reverse=True)
    words_list = []
    for word, freq in words_sorted:
        clean_word = word.rstrip(",.;:")  # extend list if other punctuation appears
        if len(clean_word) == target_length:
            words_list.append(clean_word)
            if len(words_list) == limit:
                break
    return words_list


def green_message(message, *, end=""):
    # Use full-width spacing to make text appear larger
    spaced_message = " ".join(message)
    msg = colored(spaced_message, "white", "on_green")
    print(msg, end=end)


def warning_message(message, *, end=""):
    # Use full-width spacing to make text appear larger
    spaced_message = " ".join(message)
    msg = colored(spaced_message, 'white', 'on_grey')
    print(msg, end=end)


def wrong_message(message, *, end=""):
    # Use full-width spacing to make text appear larger
    spaced_message = " ".join(message)
    msg = colored(spaced_message, 'white', 'on_red')
    print(msg, end=end)


def select_random_word(words_list, *, seed=None):
    """Pick a deterministic random word when seed is provided."""
    rng = random.Random(seed)
    return rng.choice(words_list)


def render_guess_feedback(user_guess, target_word):
    """Print color-coded hints for the current guess."""
    for user_char, target_char in zip(user_guess, target_word):
        if user_char == target_char:
            green_message(user_char)
        elif user_char in target_word:
            warning_message(user_char)
        else:
            wrong_message(user_char)
    print()

