from vpython import *

# Create the ball
ball_radius = 1
ball_pos = vector(-40, 30, 0)  # normal position (-40, 30, 0)
ball_velocity = vector(
    7, -5, 0
)  # Adjust the x and y components of the velocity to increase the speed
ball = sphere(pos=ball_pos, radius=ball_radius, color=color.red)

# Create the track
track_length = 350
track_thickness = 2
track_height = 1.2
track = box(
    pos=vector(0, 0, 0),
    length=track_length,
    width=track_thickness,
    height=track_height,
    color=color.gray(0.8),
)

# Create the obstacles
obstacle1 = box(pos=vector(-20, 5, 0), length=8, width=8, height=2, color=color.blue)
obstacle2 = cone(pos=vector(0, 20, 0), radius=6, height=12, color=color.green)
obstacle3 = cylinder(pos=vector(30, 15, 0), radius=4, height=8, color=color.orange)
obstacle4 = compound(
    [
        box(pos=vector(45, 25, 2), length=10, width=2, height=6, color=color.magenta),
        box(pos=vector(45, 25, -2), length=10, width=2, height=6, color=color.magenta),
    ]
)
obstacle5 = sphere(pos=vector(60, 5, 0), radius=6, color=color.yellow)
obstacle6 = compound(
    [
        box(pos=vector(70, 25, 2), length=10, width=2, height=6, color=color.cyan),
        box(pos=vector(70, 25, -2), length=10, width=2, height=6, color=color.cyan),
    ]
)
obstacle7 = pyramid(pos=vector(90, 15, 0), size=vector(8, 8, 8), color=color.purple)
obstacle8 = compound(
    [
        cone(pos=vector(105, 25, 0), radius=6, height=12, color=color.white),
        box(pos=vector(105, 25, 0), length=6, width=12, height=2, color=color.white),
    ]
)

# Set up the animation
dt = 0.01
ball.velocity = ball_velocity
ball.acceleration = vector(0, -9.8, 0)  # Gravity

obstacles = [
    obstacle1,
    obstacle2,
    obstacle3,
    obstacle4,
    obstacle5,
    obstacle6,
    obstacle7,
    obstacle8,
]

while True:
    rate(100)
    ball.velocity += ball.acceleration * dt
    ball.pos += ball.velocity * dt

    # Check for collision with the track
    if ball.pos.y < ball_radius:
        ball.velocity.y = abs(ball.velocity.y)

    # Check for collisions with the obstacles
    for obstacle in obstacles:
        if (
            (obstacle.pos.y - obstacle.height / 2 - ball.radius)
            <= ball.pos.y
            <= (obstacle.pos.y + obstacle.height / 2 + ball.radius)
            and (obstacle.pos.x - obstacle.length / 2 - ball.radius)
            <= ball.pos.x
            <= (obstacle.pos.x + obstacle.length / 2 + ball.radius)
            and (obstacle.pos.z - obstacle.width / 2 - ball.radius)
            <= ball.pos.z
            <= (obstacle.pos.z + obstacle.width / 2 + ball.radius)
        ):
            ball.velocity.y = abs(ball.velocity.y)

    # Check if the ball reaches the final obstacle
    final_obstacle = obstacle8
    if (
        (final_obstacle.pos.y - final_obstacle.height / 2 - ball.radius)
        <= ball.pos.y
        <= (final_obstacle.pos.y + final_obstacle.height / 2 + ball.radius)
        and (final_obstacle.pos.x - final_obstacle.length / 2 - ball.radius)
        <= ball.pos.x
        <= (final_obstacle.pos.x + final_obstacle.length / 2 + ball.radius)
        and (final_obstacle.pos.z - final_obstacle.width / 2 - ball.radius)
        <= ball.pos.z
        <= (final_obstacle.pos.z + final_obstacle.width / 2 + ball.radius)
    ):
        ball.velocity = vector(0, 0, 0)  # Stop the ball
        break
