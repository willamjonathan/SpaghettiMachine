from vpython import *
import math

# Set up the scene
scene = canvas(width=1600, height=1000)

# buat yang map ini cmn bs vary mass ball sm height; gak pakai force


# creating object
# dia ditaruh di height:10 di atas slope
ball = sphere(pos=vector(-6.0, 15, 0), radius=0.5, color=color.red)


# creating map and obstacles!
wall1 = box(pos=vector(-7, -8, 0), size=vector(1, 54, 0), color=color.blue)
wall2 = box(pos=vector(8, -8, 0), size=vector(1, 46, 0), color=color.blue)

# tinggi ke atas trianglenya itu 9 kurleb, lebar = 12
slope1_angle = -30
slope1 = box(pos=vector(0, 0, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope1.rotate(angle=radians(slope1_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))

# tinggi ke bawah 9 dan kekiri 12; berarti posisi y ny itu 4.5 dari slope sblm
# tambahin 2, posisi x = -5.5
slope2_angle = 30
slope2 = box(pos=vector(-5, -10.5, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope2.rotate(angle=radians(slope2_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))

slope3_angle = -30
slope3 = box(pos=vector(12, -20, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope3.rotate(angle=radians(slope3_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))

slope4_angle = 30
slope4 = box(pos=vector(-16, -29.5, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope4.rotate(angle=radians(slope4_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))
# flat ground
ground = box(pos=vector(-15.5, -37.5, 0), size=vector(
    20, 0.5, 0.5), color=color.orange)
# hit finish line
end_box = box(pos=vector(-22.5, -36.5, 0), size=vector(
    4, 2, 0.5), color=color.red)
