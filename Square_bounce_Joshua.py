from vpython import *

# Create the ball
ball_radius = 1
ball_pos = vector  # normal position (-45, 40, 0)
ball_velocity = vector(
    5, -5, 0
)  # Adjust the x and y components of the velocity to increase the speed
ball = sphere(pos=ball_pos, radius=ball_radius, color=color.red)

# Create the track
track_length = 500
track_thickness = 1.8
track_height = 0.5
track = box(
    pos=vector(0, 0, 0),
    length=track_length,
    width=track_thickness,
    height=track_height,
    color=color.gray(0.8),
)

# Create the obstacles
obstacle1 = box(pos=vector(-30, 20, 0), length=10, width=2, height=6, color=color.blue)
obstacle2 = box(pos=vector(0, 10, 0), length=8, width=2, height=6, color=color.green)
obstacle3 = box(pos=vector(30, 15, 0), length=12, width=2, height=6, color=color.orange)
obstacle4 = box(
    pos=vector(60, 25, 0), length=10, width=2, height=6, color=color.magenta
)
obstacle5 = box(pos=vector(80, 15, 0), length=8, width=2, height=6, color=color.yellow)
obstacle6 = box(pos=vector(110, 20, 0), length=10, width=2, height=6, color=color.cyan)
obstacle7 = box(
    pos=vector(140, 30, 0), length=12, width=2, height=6, color=color.purple
)

# Set up the animation
dt = 0.01
ball.velocity = ball_velocity
ball.acceleration = vector(0, -9.8, 0)  # Gravity

while True:
    rate(100)
    ball.velocity += ball.acceleration * dt
    ball.pos += ball.velocity * dt

    # Check for collision with the track
    if ball.pos.y < ball_radius:
        ball.velocity.y = abs(ball.velocity.y)

    # Check for collisions with the obstacles
    obstacles = [
        obstacle1,
        obstacle2,
        obstacle3,
        obstacle4,
        obstacle5,
        obstacle6,
        obstacle7,
    ]
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
            # Calculate the reflection direction
            normal = vector(0, 1, 0)  # Assuming obstacles are oriented vertically
            incident = ball.velocity
            reflected = incident - 2 * dot(incident, normal) * normal

            ball.velocity = (
                reflected  # Update the ball's velocity with the reflection direction
            )

    # Check if the ball reaches the final obstacle
    last_obstacle = obstacles[-1]
    if (
        (last_obstacle.pos.y - last_obstacle.height / 2 - ball.radius)
        <= ball.pos.y
        <= (last_obstacle.pos.y + last_obstacle.height / 2 + ball.radius)
        and (last_obstacle.pos.x - last_obstacle.length / 2 - ball.radius)
        <= ball.pos.x
        <= (last_obstacle.pos.x + last_obstacle.length / 2 + ball.radius)
        and (last_obstacle.pos.z - last_obstacle.width / 2 - ball.radius)
        <= ball.pos.z
        <= (last_obstacle.pos.z + last_obstacle.width / 2 + ball.radius)
    ):
        ball.velocity = vector(0, 0, 0)  # Stop the ball
        break
