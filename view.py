from tkinter import ttk
import tkinter as tk
from functools import partial


class View(tk.Tk):
    # stylesheet
    PADDING = 10
    MAX_BUTTONS = 4

    button_titles = [
        "C", "+/-", "%", "/",
        7, 8, 9, "*",
        4, 5, 6, "-",
        1, 2, 3, "+",
        0, ".", "="
    ]

    def __init__(self, controller):
        super(View, self).__init__()
        self.controller = controller

        self.entry_val = tk.StringVar()
        self.entry_val.set('0')

        self._make_frame()
        self._make_entry()
        self._make_buttons()

    def main(self):
        self.title("Hesap Makinesi")
        self.mainloop()

    def _make_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PADDING, pady=self.PADDING)

    def _make_entry(self):
        entry = ttk.Entry(self.main_frame, textvariable=self.entry_val, justify="right", state="readonly")
        entry.pack(fill="x")

    def _make_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack()

        buttons_max = 0
        row_frame = ttk.Frame(button_frame)
        row_frame.pack()

        for title in self.button_titles:
            if buttons_max == self.MAX_BUTTONS:
                buttons_max = 0
                row_frame = ttk.Frame(button_frame)
                row_frame.pack()

            btn = ttk.Button(row_frame, text=title, command=partial(self.controller.on_button_click, title))
            btn.pack(side="left")

            buttons_max += 1
