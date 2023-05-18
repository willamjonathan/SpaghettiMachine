# Set initial velocity
# Velocity when force is given; moving X direction
ball.velocityX = vector(1, 0, 0)  # Move to the right
# Velocity when ball falls;
ball.velocityY = vector(0, -1, 0)


# Define the force of gravity
g = vector(0, -9.8, 0)

# Time step
dt = 0.01

# Simulation loop
while True:
    rate(100)

    # Update position
    ball.pos += ball.velocityX * dt + ball.velocityY * dt

    # Apply gravity
    ball.velocityY += g * dt

    if ball.pos.y < ground.pos.y + ground.size.y and ball.velocityY < 0:
        ball.velocityY = 0

    # Move only in X direction
    ball.pos += ball.velocityX * dt