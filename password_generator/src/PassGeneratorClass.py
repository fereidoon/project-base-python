from abc import ABC, abstractmethod
import random
import string
import nltk

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self,length: int = 4):
        self.length = length
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self,length: int = 8,include_punctuation: bool = False,include_numbers: bool = False):
        self.length = length
        self.include_punctuation = include_punctuation
        self.include_numbers = include_numbers
        self.charachters = string.ascii_letters
    def generate(self):
        if self.include_punctuation:
            self.charachters += string.punctuation
        if self.include_numbers:
            self.charachters += string.digits
        return ''.join([random.choice(self.charachters) for _ in range(self.length)])


class MemorablePasswordGenetator(PasswordGenerator):
    def __init__(self,number_of_words: int = 4,seperator: str ="_",capitilaze: bool = False, vocabulary: list = None):
        self.number_of_words = number_of_words
        self.seperator = seperator
        self.capitilaze = capitilaze
        self.vocabulary = vocabulary
        if vocabulary == None:
            self.vocabulary = nltk.corpus.words.words()
    def generate(self):
        password_word = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        print(password_word)
        if self.capitilaze:
            password_word = [word.upper() if random.choice([True,False]) else word.lower() for word in password_word]
        return self.seperator.join(password_word)  
