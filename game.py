import tkinter as tk
from tkinter import messagebox

from board import Board
from menu import MenuGUI


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Isaglish - Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.root.iconphoto(False, tk.PhotoImage(file="./logo_black.png"))

        self.board = Board(self.root, self.check_winner)
        self.menu = MenuGUI(self.root, reset_board=self.board.reset_board)

        self.board.create_board()
        self.menu.create_menu()


    def check_winner(self) -> None:
        buttons = self.board.buttons

        # checks horizontally or rows
        for i in range(0, 9, 3):
            self.check_all(i, buttons, "X", 0, 1, 2)
            self.check_all(i, buttons, "O", 0, 1, 2)

        # checks vertically or columns
        for i in range(0, 3):
            self.check_all(i, buttons, "X", 0, 3, 6)
            self.check_all(i, buttons, "O", 0, 3, 6)

        # checks diagonally
        for i in range(0, 1):
            for j in range(0, 2):
                self.check_all(i, buttons, "X", 2*j, 4, 8-(2*j))
                self.check_all(i, buttons, "O", 2*j, 4, 8-(2*j))

        if self.board.count == 9:
            self.end_game("The game is a tie!")


    def check_all(self, index: int, buttons: list[tk.Button], turn: str, offset1: int, offset2: int, offset3: int) -> None:
        if (buttons[index+offset1]["text"] == turn and
            buttons[index+offset2]["text"] == turn and
            buttons[index+offset3]["text"] == turn):
            self.end_game(f"{turn} has won the game!")


    def end_game(self, text: str) -> None:
        self.board.turn_label_text.set(text)
        self.board.win = True
        if messagebox.askyesno("Game Over!", f"{self.board.turn_label_text.get()} Would you like to play again?"):
            self.board.reset_board()
        else:
            exit()


if __name__ == "__main__":
    game = Game()
    game.root.mainloop()