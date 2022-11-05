import tkinter as tk


class Board:
    def __init__(self, root: tk.Tk, check_winner):
        self.root = root
        self.check_winner = check_winner


    def create_board(self) -> None:
        self.turn_label_text = tk.StringVar()

        turn_label = tk.Label(self.root, textvariable=self.turn_label_text, font=("", 20), pady=10)
        turn_label.pack()

        self.board = tk.Frame(self.root)
        self.board.pack()

        self.reset_board()


    def reset_board(self) -> None:
        self.turn = "X"
        self.win = False
        self.turn_label_text.set(f"Current Turn: X")
        self.count = 0
        self.create_buttons()

    
    def create_buttons(self) -> None:
        BUTTON_FONT = ("Arial Bold", 50)
        BUTTON_WIDTH, BUTTON_HEIGHT = 3, -2

        self.buttons = [
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[0])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[1])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[2])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[3])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[4])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[5])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[6])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[7])),
            tk.Button(self.board, command=lambda: self.handle_button(self.buttons[8]))
        ]

        # position buttons in 3x3 grid
        for i in range(1, 4):
            for j in range(1, 4):
                index = ((3*i)+j) - 4
                self.buttons[index].grid(row=i, column=j)
                self.buttons[index].configure(
                    text="",
                    font=BUTTON_FONT,
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    cursor="tcross",
                    fg="black",
                    bg="white",
                    relief="groove"
                )


    def handle_button(self, button: tk.Button) -> None:

        if not button["text"]:
            if self.turn == "X":
                button["text"] = "X"
                button["bg"] = "tomato"
                button["activebackground"] = "coral3"
                self.turn = "O"
            else:
                button["text"] = "O"
                button["bg"] = "cornflower blue"
                button["activebackground"] = "steel blue"
                self.turn = "X"

            self.turn_label_text.set(f"Current Turn: {self.turn}")
            button["fg"] = "white"
            button["activeforeground"] = "white"
            self.count += 1
            self.check_winner()