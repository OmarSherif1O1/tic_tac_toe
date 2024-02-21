import tkinter as tk
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [" "] * 9

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text="", width=10, height=4, font=("Helvetica", 20),
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [2, 4, 6]]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_board(self):
        self.current_player = "X"
        self.board = [" "] * 9
        for button in self.buttons:
            button.config(text="")


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
