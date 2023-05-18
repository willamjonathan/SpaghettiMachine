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

box2 = box(pos=vector(2, -4, 0), size=vector(1, 11, 3), color=color.orange)
box3 = box(pos=vector(4, -12, 0), size=vector(8, 1, 3), color=color.green)
box4 = box(pos=vector(0, -6, 0), size=vector(1, 12, 3), color=color.orange)
box5 = box(pos=vector(12, -14, 0), size=vector(9, 1, 3), color=color.yellow)
box5.rotate(angle=radians(box_angle), axis=vector(
    0, 0, 1), origin=vector(11, -13, 0))

x_box6_cos30 = (math.sqrt(3)/2) * 9
x_box6 = x_box6_cos30+11

box6 = box(pos=vector(x_box6, -16.5, 0),
           size=vector(8, 1, 3), color=color.green)

box7 = box(pos=vector(25, -24.5, 0), size=vector(1, 28, 3), color=color.orange)
box8 = box(pos=vector(22, -24.5, 0), size=vector(1, 16, 3), color=color.orange)

box8 = box(pos=vector(5, -38.5, 0), size=vector(40, 1, 3), color=color.green)

box9 = box(pos=vector(-5, -37.5, 0), size=vector(2, 2, 2), color=color.red)

# Set initial velocity
ball.velocity = vector(1, -1, 0)  # Move to the right

# Define the force of gravity
g = vector(0, -9.8, 0)

# Time step
dt = 0.01

# Simulation loop
while True:
    rate(100)

    # Update position
    ball.pos += ball.velocity * dt

    # Apply gravity
    ball.velocity += g * dt

    if ball.pos.y < ground.pos.y + ground.size.y and ball.velocity.y < 0:
        ball.velocity.y = 0
        # Move only in X direction
        ball.pos += ball.velocity * dt

    # Check if ball hits box2
    if ball.pos.x >= box2.pos.x - box2.size.x and ball.pos.y >= box2.pos.y - box2.size.y and ball.pos.x <= box2.pos.x + box2.size.x and ball.pos.y >= box3.pos.y + box3.size.y:
        ball.velocity.y = -1  # Make the ball fall
        ball.velocity.x = 0
        # Move only in X direction
        ball.pos += ball.velocity * dt

# Check if ball hits box3
    if ball.pos.x >= box3.pos.x - box3.size.x/2 and ball.pos.y <= box3.pos.y + box3.size.y:
        ball.velocity.y = 0  # Stop the ball in the Y direction
        ball.velocity.x = 1
        # Move only in X direction
        ball.pos += ball.velocity * dt

# Check if ball passes through box3 and hits box5
    if ball.pos.x >= box5.pos.x - box5.size.x/2 and ball.pos.y >= box5.pos.y - box5.size.y/2:
        slope_angle = math.radians(box_angle)
        # Set the ball's velocity for the slope
        ball.velocity.y = math.sin(slope_angle)-0.8

        ball.pos += ball.velocity * dt
