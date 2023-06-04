from vpython import *
import tkinter as tk


def start_simulation():
    global simulation_running
    simulation_running = True


def stop_simulation():
    global simulation_running
    simulation_running = False


def create_circle_button_with_triangle():
    window = tk.Tk()

    # Set up the VPython scene
    scene = canvas(title="Spaghetti Machine Simulation", width=800, height=600)

    # Create the track
    track_length = 100
    track_height = 10
    track_width = 1
    track = box(
        pos=vector(0, -track_height / 2, 0),
        size=vector(track_length, track_width, track_height),
        color=color.gray(0.7),
    )

    # Create start and stop buttons
    button_start = tk.Button(window, text="Start", command=start_simulation)
    button_start.pack()

    button_stop = tk.Button(window, text="Stop", command=stop_simulation)
    button_stop.pack()

    # Create the ball
    ball_radius = 0.5
    ball = sphere(
        pos=vector(-track_length / 2 + ball_radius, 0, 0),
        radius=ball_radius,
        color=color.red,
        make_trail=True,
    )

    # Create obstacles
    obstacle1 = box(
        pos=vector(-track_length / 4, -ball_radius, 0),
        size=vector(4, 2, 2),
        color=color.green,
    )
    obstacle2 = box(
        pos=vector(track_length / 4, -ball_radius, 0),
        size=vector(2, 2, 4),
        color=color.blue,
    )
    obstacle3 = box(
        pos=vector(track_length / 2 - 2, -ball_radius, 0),
        size=vector(2, 2, 4),
        color=color.orange,
    )
    obstacle4 = box(
        pos=vector(-track_length / 2 + 2, -ball_radius, 0),
        size=vector(2, 2, 4),
        color=color.yellow,
    )
    obstacle5 = box(
        pos=vector(-track_length / 2 + 6, -ball_radius, 0),
        size=vector(2, 2, 4),
        color=color.magenta,
    )

    # Main loop
    simulation_running = False
    while True:
        if simulation_running:
            rate(1000)
            ball.pos += ball.velocity

            # Check if the ball goes out of bounds
            if ball.pos.x > track_length / 2 - ball_radius:
                ball.pos.x = track_length / 2 - ball_radius
                ball.velocity = vector(0, 0, 0)  # Stop the ball

            # Calculate the ball's position along the track
            if -track_length / 2 <= ball.pos.x <= track_length / 2:
                ball.pos.y = (
                    track_height / 2
                    - ball_radius
                    - (ball.pos.x - (-track_length / 2))
                    * (track_height - ball_radius)
                    / track_length
                )
            else:
                ball.pos.y = -ball_radius

            # Check for collisions with obstacles
            if (
                ball.pos.y < obstacle1.pos.y + obstacle1.size.y / 2
                and ball.pos.x > obstacle1.pos.x - obstacle1.size.x / 2
                and ball.pos.x < obstacle1.pos.x + obstacle1.size.x / 2
            ):
                ball.color = obstacle1.color

            if (
                ball.pos.y < obstacle2.pos.y + obstacle2.size.y / 2
                and ball.pos.x > obstacle2.pos.x - obstacle2.size.x / 2
                and ball.pos.x < obstacle2.pos.x + obstacle2.size.x / 2
            ):
                ball.color = obstacle2.color

            if (
                ball.pos.y < obstacle3.pos.y + obstacle3.size.y / 2
                and ball.pos.x > obstacle3.pos.x - obstacle3.size.x / 2
                and ball.pos.x < obstacle3.pos.x + obstacle3.size.x / 2
            ):
                ball.color = obstacle3.color

            if (
                ball.pos.y < obstacle4.pos.y + obstacle4.size.y / 2
                and ball.pos.x > obstacle4.pos.x - obstacle4.size.x / 2
                and ball.pos.x < obstacle4.pos.x + obstacle4.size.x / 2
            ):
                ball.color = obstacle4.color

            if (
                ball.pos.y < obstacle5.pos.y + obstacle5.size.y / 2
                and ball.pos.x > obstacle5.pos.x - obstacle5.size.x / 2
                and ball.pos.x < obstacle5.pos.x + obstacle5.size.x / 2
            ):
                ball.color = obstacle5.color

        window.update()

    window.mainloop()


# Call the function to create the circle button with triangle
create_circle_button_with_triangle()
