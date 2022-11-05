import tkinter as tk
from tkinter import messagebox


class GameAI:

    def __init__(self, root: tk.Tk, reset_board):
        self.root = root
        self.reset_board = reset_board


    def create_option_menu(self):
        self.option_menu = tk.Frame(self.root)
        self.option_menu.pack(pady=20)

        self.ai_mode = tk.StringVar()
        self.ai_mode.set("None")
        self.prev_ai_mode = tk.StringVar()
        self.prev_ai_mode.set("None")

        ai_mode_label = tk.Label(self.option_menu, text="AI Mode:")
        ai_mode_label.grid(row=0, column=0, padx=10)

        ai_modes = ["None", "Easy AI", "Hard AI"]
        ai_mode_menu = tk.OptionMenu(self.option_menu, self.ai_mode, *ai_modes)
        ai_mode_menu.grid(row=0, column=1)

        submit_button = tk.Button(self.option_menu, text="Submit", padx=10, command=self.handle_submit)
        submit_button.grid(row=0, column=2)


    def handle_submit(self):
        if self.ai_mode.get() != self.prev_ai_mode.get():
            if messagebox.askyesno("Play Against AI?", "Would you like to reset the game and play with <AI Mode>?"):
                self.reset_board()
                self.prev_ai_mode.set(self.ai_mode.get())
                messagebox.showerror("WIP", "Heh, sorry, I haven't implemented this AI yet.")
            else:
                self.ai_mode.set("None")
                self.prev_ai_mode.set(self.ai_mode.get())