import random

def russian_roulette():
    print("Welcome to Russian Roulette!")
    print("There are 6 chambers, and 1 contains a bullet.")
    
    # Load the gun
    chambers = [0, 0, 0, 0, 0, 1]  # 0 means empty, 1 means bullet
    random.shuffle(chambers)  # Shuffle the chambers to randomize the bullet's position

    round_num = 1

    while True:
        input(f"Round {round_num}: Press Enter to pull the trigger...")
        
        # The player pulls the trigger
        shot = chambers.pop(0)  # The first chamber gets fired
        
        if shot == 1:
            print(f"Bang! You lost in round {round_num}.")
            break
        else:
            print("Click! You're safe.")
        
        # If there are still chambers left, continue the game
        if chambers:
            round_num += 1
        else:
            print("You've survived all rounds! You're lucky.")
            break

if __name__ == "__main__":
    russian_roulette()
