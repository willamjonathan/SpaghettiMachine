from tkinter import *
from vpython import *

from unused.Map import Map
from unused.Ball import Ball
from unused.Force import Force
from MapForce import MapX

# Initialize Tkinter
root = Tk()
root.geometry("400x300")

# Create a frame for the VPython canvas
frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand=YES)


def open_Map():
    Map()


def open_Ball():
    Ball()


def open_Force():
    Force()


def MapXX():
    MapX()


# Create a VPython canvas
scene = canvas(width=800, height=600, background=color.black,
               center=vector(0, 0, 0), fov=0.5)

# Create a VPython object in the scene
# sphere(pos=vector(0, 0, 0), radius=0.5)


# Create the main screen frame
# main_screen = Frame(root, width=800, height=600, bg="blue")
# main_screen.place(x=10, y=10)

Force_btn = Button(root, text="Adjust Force", command=open_Force)
Force_btn.place(x=50, y=200)

Ball_btn = Button(root, text="Ball Type", command=open_Ball)
Ball_btn.place(x=150, y=200)

ChangeMap_btn = Button(root, text="Change Map", command=MapXX)
ChangeMap_btn.place(x=250, y=200)

# Main Tkinter loop
root.mainloop()
