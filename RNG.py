
from tkinter import Tk, Label
import random


class Counter:
    def __init__(self, frame):
        self.value = ""
        self.color = "#ffffff"
        self.background = "#000000"
        self.label = Label(frame,
                           text=self.value,
                           font="Helvetica 100 bold",
                           height=2,
                           width=4,
                           fg=self.color,
                           bg=self.background)
        self.label.bind("<1>", self.clicked)

    def clicked(self, _):
        self.value = random.randint(0, 100)
        if self.value < 30:
            self.color = "#6da2c0"
        elif self.value < 60:
            self.color = "#8fbc8b"
        else:
            self.color = "#e9967a"
        self.label.config(text=self.value, fg=self.color)


if __name__ == "__main__":
    root = Tk()
    root.title("RNG")
    root.geometry("300x300")

    cnt = Counter(root)
    cnt.label.pack()
    cnt.label.mainloop()
