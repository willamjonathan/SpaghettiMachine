from vpython import *

# Set up the scene
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

# Define the start_simulation() and stop_simulation() functions
simulation_running = False


def start_simulation():
    global simulation_running
    simulation_running = True


def stop_simulation():
    global simulation_running
    simulation_running = False


# Create start and stop buttons
button_start = button(bind=start_simulation, text="Start", pos=scene.title_anchor)
button_stop = button(bind=stop_simulation, text="Stop", pos=scene.title_anchor)

# Create the ball
ball_radius = 0.5
ball = sphere(
    pos=vector(-track_length / 2 + ball_radius, 0, 0),
    radius=ball_radius,
    color=color.red,
    make_trail=True,
)

# Create speed slider
speed_slider = slider(
    bind=lambda: set_speed(speed_slider.value),
    min=0.1,
    max=2,
    step=0.1,
    value=1,
    left=scene.title_anchor + vector(0, -100, 0),
    width=200,
    length=100,
)


# Set the ball's speed based on the slider value
def set_speed(value):
    ball.velocity = vector(value, 0, 0)


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

# Add decorations
decoration1 = cylinder(
    pos=vector(-track_length / 4, -ball_radius - 0.5, -3),
    axis=vector(0, 3, 0),
    radius=0.1,
    color=color.white,
)
decoration2 = box(
    pos=vector(track_length / 4, -ball_radius - 1, 0),
    size=vector(2, 0.1, 2),
    color=color.white,
)
decoration3 = sphere(
    pos=vector(track_length / 2 - 5, -ball_radius - 0.5, 0),
    radius=0.5,
    color=color.white,
)

# Add a gap obstacle
gap_pos = vector(track_length / 2 - 5, -ball_radius, 0)
gap_width = 3
gap_height = 2
gap = box(pos=gap_pos, size=vector(gap_width, gap_height, 4), color=color.cyan)

normal_friction = 0.5  # Normal friction coefficient
slippery_friction = 0.1  # Low friction coefficient (slippery)
sticky_friction = 1.0  # High friction coefficient (sticky)

normal_surface = box(
    pos=vector(0, -ball_radius - 1, 0),
    size=vector(track_length, 0.1, track_height),
    color=color.white,
)
normal_surface.friction = normal_friction

slippery_surface = box(
    pos=vector(track_length / 4, -ball_radius - 1, 0),
    size=vector(track_length / 2, 0.1, track_height),
    color=color.white,
)
slippery_surface.friction = slippery_friction

sticky_surface = box(
    pos=vector(-track_length / 4, -ball_radius - 1, 0),
    size=vector(track_length / 2, 0.1, track_height),
    color=color.white,
)
sticky_surface.friction = sticky_friction


def rotate_scene():
    scene.append_to_caption("\nDrag the mouse to rotate the scene.\n")


scene.bind("mousedown", rotate_scene)


def release_spaghetti():
    pass  # Placeholder for spaghetti release mechanism


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

        if (
            ball.pos.y < gap_pos.y + gap_height + ball_radius
            and ball.pos.x > gap_pos.x - gap_width / 2
            and ball.pos.x < gap_pos.x + gap_width / 2
        ):
            ball.pos.y = gap_pos.y + gap_height + ball_radius

        if ball.pos.y < -ball_radius:
            ball.pos.y = -ball_radius

        if (
            ball.pos.x > sticky_surface.pos.x
            and ball.pos.x < sticky_surface.pos.x + sticky_surface.size.x
        ):
            ball.friction = sticky_surface.friction
        elif (
            ball.pos.x > slippery_surface.pos.x
            and ball.pos.x < slippery_surface.pos.x + slippery_surface.size.x
        ):
            ball.friction = slippery_surface.friction
        else:
            ball.friction = normal_surface.friction

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
    else:
        rate(1)
