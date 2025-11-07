import random

def montyhall(user_change_choice: bool) -> bool:
    doors = ['goat','car','goat']
    random.shuffle(doors)
    user_choice = random.choice(range(3))
    reveal_doors_candidate = [ i for i in range(3) if i != user_choice and doors[i] != 'car']
    reveald_door = random.choice(reveal_doors_candidate)

    if user_change_choice:
        # User decides to change their choice
        final_choice = [i for i in range(3) if i != user_choice and i != reveald_door][0]        
    else:
        # User sticks with their original choice
        final_choice = user_choice
    if doors[final_choice] == 'car':
        return True
    else:
        return False
def simulate(switch: bool, num_simulations: int) -> float:
    wins = 0
    for _ in range(num_simulations):
        if montyhall(switch):
            wins += 1
    return wins / num_simulations
if __name__ == "__main__":
    for change_choice in [True, False]:
        wins = 0
        trials = 1000000
        for _ in range(trials):
            if montyhall(change_choice):
                wins += 1
        print(f"User change choice: {change_choice}, Win rate: {wins/trials:.2f}")


