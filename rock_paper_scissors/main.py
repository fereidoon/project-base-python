from src.rock_paper_scissors import Rock_Papaer_Scissors

if __name__ == '__main__':
    game = Rock_Papaer_Scissors()
    while True:
        game.play()
        continue_game = input('do you whant to play again ? enter q for exit or any key to continue')
        if continue_game.lower() == 'q':
            break
    