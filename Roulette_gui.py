import tkinter as tk
import random
import pygame 

class RussianRouletteGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Roulette Game")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Game variables
        self.chambers = [0, 0, 0, 0, 0, 1]  # 1 is the bullet, 0 is empty chamber
        random.shuffle(self.chambers)
        
        self.round_num = 1
        self.game_over = False

        # GUI Components
        self.label = tk.Label(self.root, text="Welcome to Russian Roulette!\nPress 'Pull Trigger' to start!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.round_label = tk.Label(self.root, text=f"Round {self.round_num}", font=("Helvetica", 14))
        self.round_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.pull_button = tk.Button(self.root, text="Pull Trigger", font=("Helvetica", 14), command=self.pull_trigger)
        self.pull_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Helvetica", 14), command=self.root.quit)
        self.quit_button.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Helvetica", 14), command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state="disabled")  # Initially disabled


    def pull_trigger(self):
        if self.game_over:
            self.play_again_button.config(state="normal")  # Enable the play again button

        shot = self.chambers.pop(0)  # Fire the first chamber

        if shot == 1:
            self.result_label.config(text="Bang! You lost!")
            self.label.config(text="Game Over!")
            self.pull_button.config(state="disabled")  # Disable the button
            self.game_over = True
            pygame.mixer.music.load('gunshot.mp3')  # Load the gunshot sound
            pygame.mixer.music.play()  # Play the gunshot sound
        else:
            self.result_label.config(text="Click! You're safe.")
            self.round_num += 1
            self.round_label.config(text=f"Round {self.round_num}")
            if not self.chambers:
                self.result_label.config(text="You've survived all rounds! You're lucky.")
                self.label.config(text="Game Over!")
                self.pull_button.config(state="disabled")  # Disable the button
                self.game_over = True
        if self.game_over:
            self.play_again_button.config(state="normal")  # Enable the play again button


    def reset_game(self):
            self.chambers = [0, 0, 0, 0, 0, 1]
            random.shuffle(self.chambers)
            self.round_num = 1
            self.game_over = False

            self.label.config(text="Welcome to Russian Roulette!\nPress 'Pull Trigger' to start!")
            self.round_label.config(text=f"Round {self.round_num}")
            self.result_label.config(text="")
            self.pull_button.config(state="normal")
            self.play_again_button.config(state="disabled")

# Set up the main window
root = tk.Tk()
game = RussianRouletteGame(root)
root.mainloop()
