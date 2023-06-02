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


def Force():
    def increment():
        value.set(value.get() + 1)

    def decrement():
        value.set(value.get() - 1)
    # Create the Tkinter window
    root = Tk()
    root.geometry("600x400")
    value = IntVar()
    value.set(25)  # Set initial value to 0

    # # Create a square frame
    # square_frame = Frame(root, width=200, height=200, bd=1, relief="solid")
    # square_frame.place(x=200, y=120)

    # Create a label to display the number inside the square
    label = Label(root, textvariable=value, font=("Helvetica", 60))
    label.place(x=200, y=120)

    # # Create an increment button
    # increment_button = Button(root, text="Increment", command=increment)
    # increment_button.pack(pady=5)

    ball_change = CircleButton(
        root, radius=35, color='green', command=increment)
    ball_change.place(x=450, y=100)

    # Add = Label(ball_change, text="+", font=("Helvetica", 10))
    # Add.pack(expand=True)

    ball_change2 = CircleButton(
        root, radius=35, color='red', command=decrement)
    ball_change2.place(x=450, y=200)

    # Substract = Label(ball_change2, text="-", font=("Helvetica", 10))
    # Substract.pack(expand=True)

    # # Create a decrement button
    # decrement_button = Button(root, text="Decrement", command=decrement)
    # decrement_button.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()


# Force()
