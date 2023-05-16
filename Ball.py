from tkinter import *
from tkinter import ttk
from vpython import *

# Initialize Tkinter

from tkinter import *


class CircleButton(Canvas):
    def __init__(self, master=None, radius=25, color='gray', command=None, **kwargs):
        super().__init__(master, width=2*radius, height=2*radius, **kwargs)
        self.radius = radius
        self.color = color
        self.command = command
        self.bind('<Button-1>', self.on_click)
        self.draw_circle()

    def draw_circle(self):
        self.delete('all')
        self.create_oval(0, 0, 2*self.radius, 2*self.radius, fill=self.color)

    def on_click(self, event):
        if self.command:
            self.command()


class Circle(Canvas):
    def __init__(self, master=None, radius=25, color='gray', command=None, **kwargs):
        super().__init__(master, width=2*radius, height=2*radius, **kwargs)
        self.radius = radius
        self.color = color
        self.command = command
        self.draw_circle()

    def draw_circle(self):
        self.delete('all')
        self.create_oval(0, 0, 2*self.radius, 2*self.radius, fill=self.color)


def Ball():
    root = Tk()
    root.geometry("600x400")

    Title = Label(root, text="Adjust Ball", font=("Helvetica", 24))
    Title.place(x=200, y=20)

    ball_change = CircleButton(
        root, radius=35, color='green', command=root.quit)
    ball_change.place(x=450, y=100)

    ball_change2 = CircleButton(
        root, radius=35, color='red', command=root.quit)
    ball_change2.place(x=450, y=200)

    Ball = Circle(root, radius=80, color='white')
    Ball.place(x=200, y=120)

    # Main Tkinter loop
    root.mainloop()
