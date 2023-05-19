from vpython import *
import math

# Set up the scene
scene = canvas(width=1600, height=1000)

# buat yang map ini cmn bs vary mass ball sm height; gak pakai force


# creating object
# dia ditaruh di height:10 di atas slope
ball = sphere(pos=vector(-6.0, 15, 0), radius=0.5, color=color.red)

cekposisi = box(pos=vector(-6, -37.5, 0),
                size=vector(1, 1, 0), color=color.yellow)


# creating map and obstacles!
wall1 = box(pos=vector(-7, -8, 0), size=vector(1, 54, 0), color=color.blue)
wall2 = box(pos=vector(8, -8, 0), size=vector(1, 46, 0), color=color.blue)

slope1_angle = -30
slope1 = box(pos=vector(0, 0, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
# slope1 = box(pos=vector(-1, 0, 0), size=vector(
#     13, 0.5, 0.5), color=color.orange)
slope1.rotate(angle=radians(slope1_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))
print(math.sin(-30)*slope1.pos.y + slope1.size.y + ball.size.y)
print(slope1.pos.y)

slope2_angle = 30
slope2 = box(pos=vector(-4.5, -10.5, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope2.rotate(angle=radians(slope2_angle), axis=vector(
    0, 0, 1), origin=vector(0, 0, 0))

slope3_angle = -30
slope3 = box(pos=vector(11, -20, 0), size=vector(
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

# NOTES
# SLOPE1 = (-6,3.5), (6,-4)
# SLOPE2 = (7,-8.5), (4.5,-15)
# SLOPE3 = (-6,-19.5), (6,-26)
# SLOPE4 = (7,-30), (6,-37)

# HEIGHT
# SLOPE 1 & 2 = 3.5
# SLOPE 2 & 3 = 5
# SLOPE 3 & 4 = 4


# Define initial variables
ball_velocity = vector(0, 0, 0)  # Initial velocity of the ball
gravity = vector(0, -9.8, 0)  # Acceleration due to gravity
dt = 0.01  # Time step for simulation
# Set initial time
t = 0


def potential_energy(m, g, h):
    pe = m*g*h
    return pe


def kinetic_energy(m, v):
    ke = 1/2*m*v*v
    return ke


def potential_to_velocity_vector(h):
    v = (math.sqrt(2*9.8 * h))*-1
    a = vector(0, v, 0)
    return a


def potential_to_velocity(h):
    v = (math.sqrt(2*9.8 * h))*-1
    return v


scene.camera.follow(ball)
camera_follow = True


def zoomIn_out(zoom):
    # Adjust the axis to point towards the ball
    scene.camera.axis = vector(0, 0, zoom)


def toggle_camera_follow():
    global camera_follow

    if camera_follow:
        scene.camera.follow(None)  # Stop following the ball
        camera_follow = False
        zoomIn_out(-500)
    else:
        scene.camera.follow(ball)  # Start following the ball
        camera_follow = True
        zoomIn_out(-115)


zoom_levels = [-115, -180, -250]  # Define different zoom levels
current_zoom = 0  # Initial zoom level index


def on_key_down(event):
    global current_zoom

    if event.key == " ":
        # Cycle through zoom levels
        current_zoom = (current_zoom + 1) % len(zoom_levels)
        zoomIn_out(zoom_levels[current_zoom])
    elif event.key == "b":
        toggle_camera_follow()


scene.bind("keydown", on_key_down)
# Create the pop-up text
popup_text = None

# Simulate the ball's motion
while True:
    rate(80)  # Limit the refresh rate of the scene

    # ball.pos += ball.velocity.y(potential_to_velocity(10)*-1) * dt

    # Update position
    ball.pos += ball_velocity * dt

    # print(potential_to_velocity(10))

    # Apply gravity
    ball_velocity += potential_to_velocity_vector(10) * dt

    # Check if the ball hits slope 1
    if ball.pos.y >= (slope1.pos.y + (slope1.size.x / 2 + 2*ball.radius)
                      * sin(radians(slope1_angle))) and ball.pos.y <= 4.5 and ball.pos.x <= slope1.pos.x + \
            (slope1.size.x / 2 + ball.radius) * cos(radians(slope1_angle)):
        # ball_velocity.x = potential_to_velocity(10) * math.cos(slope1_angle)
        # ball_velocity.y = potential_to_velocity(
        #     10) * math.sin(slope1_angle) - t*gravity
        # print(potential_to_velocity(10) * math.cos(radians(slope1_angle)) * -1)
        y_v = (potential_to_velocity(10) *
               math.sin(radians(-30)) - (t*9.8))
        x_v = (potential_to_velocity(10) * math.cos(radians(-30)))*-1
        ball_velocity.x = x_v
        ball_velocity.y = y_v

        ball.pos += ball_velocity * dt
        # print(ball.pos.x)
        # print(ball.pos.y)
        velocity_akhir = math.sqrt(math.pow((x_v), 2) + math.pow((y_v), 2))
        # print(velocity_akhir)

    # Hitung kecepatan akhir bola (vf) menggunakan persamaan
    # energi mekanik: vf = sqrt(v0^2 + 2 * g * h),
    # di mana h adalah ketinggian jatuh bola tegak lurus
    # (dihitung menggunakan langkah-langkah yang telah dijelaskan sebelumnya).

    if ball.pos.y <= - 3.6 and ball.pos.x > 6.9 and \
            ball.pos.y > -8.5 + ball.radius:
        ball_velocity.x = 0
        ball_velocity.y = -math.sqrt(
            math.pow(velocity_akhir, 2) + 2 * 9.8 * 3.5)
        velocity_akhir = ball_velocity.y
        # h = 3.5
        ball.pos += ball_velocity * dt
        # print((slope2.pos.y + (slope2.size.x / 2 - 2*ball.radius)
        #        * sin(radians(slope2_angle))))
        # print(velocity_akhir)

    # check if ball hits slope2

    if ball.pos.y >= (slope2.pos.y + (slope2.size.x / 2 - 2*ball.radius)
                      * sin(radians(slope2_angle))-0.5) and ball.pos.y <= -7.5 and ball.pos.x > -4.5:
        y2_v = (velocity_akhir *
                math.sin(radians(-30)) - (t*9.8)-4.5)
        x2_v = (velocity_akhir * math.cos(radians(-30)))
        ball_velocity.x = x2_v
        ball_velocity.y = y2_v
        ball.pos += ball_velocity * dt
        velocity_akhir2 = math.sqrt(math.pow((x2_v), 2) + math.pow((y2_v), 2))
        print(velocity_akhir2)

    # Check if the ball hits wall 1
    if ball.pos.x >= -6 - ball.radius and\
            ball.pos.y <= -13 and ball.pos.y >= -19.5:
        ball_velocity.x = 0
        ball_velocity.y = -math.sqrt(
            math.pow(velocity_akhir2, 2) + 2 * 9.8 * 3.5)
        velocity_akhir2 = ball_velocity.y
        # h = 3.5
        ball.pos += ball_velocity * dt

    if ball.pos.y >= (slope3.pos.y + (slope3.size.x / 2 + 2*ball.radius)
                      * sin(radians(slope3_angle))) and ball.pos.y <= -19.5 and ball.pos.x <= slope3.pos.x + \
            (slope3.size.x / 2 + ball.radius) * cos(radians(slope3_angle)):
        y3_v = (velocity_akhir2 *
                math.sin(radians(-30)) - (t*9.8)-4.5)
        x3_v = (velocity_akhir2 * math.cos(radians(-30)))
        ball_velocity.x = - x3_v
        ball_velocity.y = y3_v
        ball.pos += ball_velocity * dt
        velocity_akhir3 = math.sqrt(math.pow((x2_v), 2) + math.pow((y2_v), 2))

        # if ball.pos.y <= - 3.6 and ball.pos.x > 6.9 and \
        #     ball.pos.y > -8.5 + ball.radius:

        # # Check if the ball hits wall 1
        # if ball.pos.x >= 6 - ball.radius:
        #     ball_velocity.x = 0
        #     break

        # Check if the ball hits wall2
    if ball.pos.x >= wall2.pos.x - wall2.size.x / 2:
        ball_velocity = vector(0, 0, 0)  # Stop the ball's motion

     # Increment time
    t += dt

# Print a message when the ball hits the end box
print("Ball hit the end box!")
