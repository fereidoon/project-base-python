
import random
class Rock_Papaer_Scissors:
    def __init__(self):
        self.choice = ['rock','paper','scissors']
    
    def get_player_choise(self):
        user_choise = input('please input your choise:')
        if user_choise.lower() in self.choice:
            return user_choise
        print(f'invalid choise please enter your choise from{self.choice}')
        return self.get_player_choise()    
    
    def get_computer_choice(self):
        return random.choice(self.choice)
        

    def get_winner(self,user_choise,computer_choise):
        if user_choise == computer_choise:
             return 'its a tie'
        win_combinations = [('rock','scissors'),('paper','rock'),('scissors','paper')]
        for win_combination in win_combinations:
            if (win_combination[0] == user_choise) and (win_combination[1] == computer_choise):
                return "congratulation you won"
                
        return "sorry computer won"

    
    def play(self):
        user_choise = self.get_player_choise()
        computer_choise = self.get_computer_choice()
        print(f'your choise: {user_choise} and compueter choise is {computer_choise}')
        print(self.get_winner(user_choise,computer_choise))
        
        