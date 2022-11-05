import tkinter as tk
from tkinter import messagebox, ttk


class MenuGUI:
    def __init__(self, root: tk.Tk, reset_board):
        self.root = root
        self.reset_board = reset_board


    def create_menu(self) -> None:
        self.option_menu = tk.Frame(self.root)
        self.option_menu.pack(pady=20)

        self.menu_bar = tk.Menu(self.root, relief="groove")

        game_menu = tk.Menu(self.menu_bar, tearoff=0)
        game_menu.add_command(label="Reset", command=self.handle_reset)

        self.menu_bar.add_cascade(menu=game_menu, label="Game")

        self.root.config(menu=self.menu_bar)

        self.ai_mode = tk.StringVar()
        self.prev_ai_mode = tk.StringVar()
        self.ai_mode.set("None")
        self.prev_ai_mode.set("None")

        ai_mode_label = tk.Label(self.option_menu, text="AI Mode:")
        ai_mode_label.grid(row=0, column=0, padx=5)

        ai_modes = ["None", "Easy AI", "Hard AI"]
        ai_mode_menu_button = ttk.Menubutton(self.option_menu, textvariable=self.ai_mode)
        ai_mode_menu = tk.Menu(ai_mode_menu_button, tearoff=0)

        for mode in ai_modes:
            ai_mode_menu.add_radiobutton(label=mode, value=mode, variable=self.ai_mode)

        ai_mode_menu_button["menu"] = ai_mode_menu
        ai_mode_menu_button.grid(row=0, column=1)

        submit_button = ttk.Button(self.option_menu, text="Submit", command=self.handle_submit)
        submit_button.grid(row=0, column=2)


    def handle_submit(self) -> None:
        if self.ai_mode.get() != self.prev_ai_mode.get():
            if messagebox.askyesno("Play Against AI?", f"Would you like to reset the game and play with {self.ai_mode.get()}?"):
                self.reset_board()
                self.prev_ai_mode.set(self.ai_mode.get())
                messagebox.showerror("WIP", "Heh, sorry, I haven't implemented this AI yet.")
            else:
                self.ai_mode.set("None")
                self.prev_ai_mode.set(self.ai_mode.get())


    def handle_reset(self) -> None:
        if messagebox.askyesno("Reset Game?", "This would reset the game, are you sure?"):
            self.reset_board()