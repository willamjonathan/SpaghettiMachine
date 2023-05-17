from vpython import *
import math

# Set up the scene
scene = canvas(width=1000, height=1000)

# Create objects
ground = box(pos=vector(-3.5, -0.5, 0),
             size=vector(6, 1, 10), color=color.green)
ball = sphere(pos=vector(-3, 2, 0), radius=0.5, color=color.red)
# Obstacles
box_angle = -30

# box2 = box(pos=vector(-2, 0.5, 0), size=vector(1, 0.1, 3), color=color.yellow)


box2 = box(pos=vector(2, -4, 0), size=vector(1, 11, 3), color=color.orange)
box3 = box(pos=vector(4, -12, 0), size=vector(8, 1, 3), color=color.yellow)
box4 = box(pos=vector(0, -6, 0), size=vector(1, 12, 3), color=color.yellow)
box5 = box(pos=vector(12, -14, 0), size=vector(9, 1, 3), color=color.green)
box5.rotate(angle=radians(box_angle), axis=vector(
    0, 0, 1), origin=vector(11, -13, 0))
# sin30*9 = depan (box 6); y sekarang di 4.5+14
x_box5_cos30 = (math.sqrt(3)/2) * 9
x_box5 = x_box5_cos30+11
# 18.794228634059948

box5 = box(pos=vector(x_box5, -16.5, 0),
           size=vector(8, 1, 3), color=color.green)


# slope_ground = box(pos=vector(2, -0.5, 0),
#                    size=vector(1, 0.1, 2), color=color.orange)

# Set initial velocity
ball.velocity = vector(1, 0, 0)  # Move to the right

# Define the force of gravity
g = vector(0, -9.8, 0)

# Time step
dt = 0.01

# Simulation loop
while True:
    rate(100)

    # # Update position
    # ball.pos += ball.velocity * dt

    # # Apply force
    # ball.velocity += g * dt

    # # Check if ball hits the box2
    # if ball.pos.y < box2.pos.y + box2.size.y and ball.velocity.y < 0:
    #     ball.velocity.y = 0  # Apply an upward impulse to the ball
    #     #  ball.pos  # Place box3 at the position of the ball

    # # Check if ball hits the slope
    # if ball.pos.x >= slope.pos.x and ball.pos.z >= slope.pos.z and \
    #         ball.pos.x <= slope.pos.x + slope.size.x and ball.pos.z <= slope.pos.z + slope.size.z:
    #     ball.velocity.y = -10  # Apply a downward impulse to the ball
