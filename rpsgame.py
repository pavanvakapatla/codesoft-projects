import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(root, text="Your choice:")
        self.user_choice_label.grid(row=0, column=0, padx=10, pady=10)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")
        self.user_choice_menu = tk.OptionMenu(root, self.user_choice_var, "rock", "paper", "scissors")
        self.user_choice_menu.grid(row=0, column=1, padx=10, pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(root, text="Score - You: 0 | Computer: 0")
        self.score_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.play_again_button.grid_remove()

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        if 'win' in result:
            self.user_score += 1
        elif 'lose' in result:
            self.computer_score += 1

        self.update_score_label()

        self.play_button["state"] = "disabled"
        self.play_again_button.grid()
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "You lose!"

    def display_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def play_again(self):
        self.play_button["state"] = "active"
        self.play_again_button.grid_remove()
        self.result_label.config(text="")
        self.user_choice_var.set("rock")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
