import tkinter as tk

from ai import GameAI
from board import Board


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Isaglish - Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.root.iconphoto(False, tk.PhotoImage(file="./logo_black.png"))

        self.board = Board(self.root, self.check_winner)
        self.board.create_board()

        self.game_ai = GameAI(self.root, reset_board=self.board.reset_board)
        self.game_ai.create_option_menu()


    def check_winner(self):
        self.check_row()  # horizontal
        self.check_column()  # vertical
        self.check_diagonal()


    def check_row(self):
        pass


    def check_column(self):
        pass


    def check_diagonal(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.root.mainloop()