import string
import nltk
import random
def pin_generator(length :int = 4):
    if not isinstance(length, int) or length <= 0:
        raise ValueError('Please Enter Correct Length')
    return ''.join([random.choice(string.digits) for _ in range(length)])

def password_generator(length: int = 8,punctuation: bool = True,numbers: bool = True) -> str:
    chars=string.ascii_letters
    if punctuation:
        chars += string.punctuation
    if numbers:
        chars += string.digits
    return ''.join([random.choice(chars) for _ in range(length)])
    
def memorable_password_genetator(number_of_words :int = 4,seperator :str ='_',capitilaze :bool =False,vocabulary : list = None):
    if vocabulary == None:
        vocabulary =nltk.corpus.words.words()
    pass_word = [random.choice(vocabulary) for _ in range(number_of_words)]
    if capitilaze:
        pass_word = [word.upper() if random.choice([True,False]) else word.lower() for word in pass_word]
    return seperator.join(pass_word)
     
      
if __name__ == "__main__":
        print(pin_generator(6))
        print(password_generator(12,True,True))
        print(memorable_password_genetator(5,'-',True)) 
