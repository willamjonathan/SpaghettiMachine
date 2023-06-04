from tkinter import *
from tkinter import ttk
from vpython import *
from MapForce import MapX


# Initialize Tkinter

def MapXX():
    MapX


def Map():
    root = Tk()
    root.geometry("600x400")
    # Create a frame for the VPython canvas
    frame = Frame(root)
    frame.pack(side=LEFT, fill=BOTH, expand=YES)

    scene = canvas(width=800, height=600, background=color.white,
                   center=vector(0, 0, 0), fov=0.5)

    mybutton1 = Button(root, text="Map 1", command=MapX)
    mybutton1.place(x=75, y=200)

    mybutton2 = Button(root, text="Map 2")
    mybutton2.place(x=275, y=200)

    mybutton3 = Button(root, text="Map 3")
    mybutton3.place(x=475, y=200)

    startbutton = Button(
        root, text=" Start")
    startbutton.place(x=275, y=300)
    # Main Tkinter loop
    root.mainloop()


Map()
