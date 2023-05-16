from tkinter import *
from tkinter import ttk
from vpython import *

# Initialize Tkinter


def Map():
    root = Tk()
    root.geometry("600x400")

    mybutton1 = ttk.Button(root, text="Map 1")
    mybutton1.place(x=75, y=200)

    mybutton2 = ttk.Button(root, text="Map 2")
    mybutton2.place(x=275, y=200)

    mybutton3 = ttk.Button(root, text="Map 3")
    mybutton3.place(x=475, y=200)

    startbutton = ttk.Button(
        root, text=" Start")
    startbutton.place(x=275, y=300)
    # Main Tkinter loop
    root.mainloop()
