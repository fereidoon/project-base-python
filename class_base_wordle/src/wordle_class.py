import sys
from utils.util import green_message, warning_message, wrong_message,render_guess_feedback
import random


class wordle:
    def __init__(self, max_attempts=7,file_path='data/words_frequency.txt', world_length=5, limit=100):     
        self.max_attempts = max_attempts
        self.file_path = file_path
        self.world_list = []
        self.words =[]
        self.world_length = world_length
        self.limit = limit     

    def return_world_list(self,limt =100,world_length =5):
        self.world_length = world_length
        self.limit = limt        
        with open(self.file_path) as file:
            for raw_line in file:
                word,freq_str =raw_line.strip().split()
                self.words.append((word,int(freq_str)))
            self.words_sorted = sorted(self.words, key=lambda item: item[1], reverse=True)
        
        for word, freq in self.words_sorted:
            clean_word = word.rstrip(",.;:")
            if len(clean_word) == self.world_length:
                self.world_list.append(clean_word)
                if len(self.world_list) == self.limit:
                    break
        return self.world_list
    
    def select_random_word(self):
        random.seed(42)       
        return random.choice(self.world_list)
    
    
    def play_game(self):
        count = self.max_attempts
        selected_word = self.select_random_word()
        print(f'Welcome to Wordle! You have {self.max_attempts} attempts to guess the 5-letter word.')
        while count > 0:
            user_guess = input(f"Enter your guess (q to quit, {count} attempts remaining): ").strip().lower()
            if user_guess == 'q':
                print('Goodbye!')
                break
            if len(user_guess) != 5:
                print('Please enter exactly 5 letters.')
                continue 
            if user_guess == selected_word:
                print('Congratulations! You guessed the word correctly!')
                break
            render_guess_feedback(user_guess, selected_word)
            # Newline after colored output
            count -= 1
            if count == 0:
                print(f'Sorry, you ran out of attempts. The word was: {selected_word}')
                print('Better luck next time!')
                break