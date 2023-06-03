from vpython import *
import math


# Set up the scene
scene = canvas(width=1600, height=1000)

# buat yang map ini cmn bs vary mass ball sm height; gak pakai force

h = 15  # heightnya 10 ini soalnya slope kan jadi miring
b = 10  # heightnya 5 ini

# dia ditaruh di height:10 di atas slope

willjospecial =8000
ball = sphere(pos=vector(-6.0+willjospecial, 15, 0), radius=0.5, color=color.green)

# creating object
cekposisi = box(pos=vector(-6+willjospecial, -37.5, 0),
                size=vector(1, 1, 0), color=color.yellow)


# creating map and obstacles!
# wall1 = box(pos=vector(-7, -6, 0), size=vector(1, 54, 0), color=color.blue)
# wall2 = box(pos=vector(8, -12, 0), size=vector(1, 40, 0), color=color.blue)

# walls
wall_a = box(pos=vector(8+willjospecial, -6, 0), size=vector(1, 6, 0), color=color.white)
wall_b = box(pos=vector(-7+willjospecial,-16 , 0), size=vector(1, 6, 0), color=color.white)
wall_c = box(pos=vector(8+willjospecial,-27 , 0), size=vector(1, 6, 0), color=color.white)

slope1_angle = -30
slope1 = box(pos=vector(0+willjospecial, 0, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
# slope1 = box(pos=vector(-1, 0, 0), size=vector(
#     13, 0.5, 0.5), color=color.orange)
slope1.rotate(angle=radians(slope1_angle), axis=vector(
    0, 0, 1), origin=vector(0+willjospecial, 0, 0))
# print(math.sin(-30)*slope1.pos.y + slope1.size.y + ball.size.y)
# print(slope1.pos.y)

slope2_angle = 30
slope2 = box(pos=vector(-4.5+willjospecial, -10.5, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope2.rotate(angle=radians(slope2_angle), axis=vector(
    0, 0, 1), origin=vector(0+willjospecial, 0, 0))

slope3_angle = -30
slope3 = box(pos=vector(11+willjospecial, -20, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope3.rotate(angle=radians(slope3_angle), axis=vector(
    0, 0, 1), origin=vector(0+willjospecial, 0, 0))

slope4_angle = 30
slope4 = box(pos=vector(-16+willjospecial, -29.5, 0), size=vector(
    15, 0.5, 0.5), color=color.orange)
slope4.rotate(angle=radians(slope4_angle), axis=vector(
    0, 0, 1), origin=vector(0+willjospecial, 0, 0))
# flat ground
ground = box(pos=vector(-15.5+willjospecial, -37.5, 0), size=vector(
    20, 0.5, 0.5), color=color.orange)
# hit finish line
end_box = box(pos=vector(-22.5+willjospecial, -36.5, 0), size=vector(
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


gravitasi = 9.8
# global variables
paused = False
# timer 
def start_timer():
    global time_elapsed
    time_elapsed = 0

# To pause
def toggle_pause():
    global paused
    paused = not paused

def restart():
    global ball_velocity, t
    ball.pos = vector(-6.0+willjospecial, 15, 0)
    ball_velocity = vector(0, 0, 0)
    t = 0

def gravity_increase():
    global gravitasi
    gravitasi = gravitasi + 1

def gravity_decrease():
    global gravitasi

    gravitasi = gravitasi - 1

def gravity_sun():
    global gravitasi 
    gravitasi = 274 #kurang lebih 28kali bumi

def gravity_earth():
    global gravitasi
    gravitasi = 9.8

def gravity_moon():
    global gravitasi 
    gravitasi = 0.16 * 9.8


button_stop = button(bind=toggle_pause,pos = scene.title_anchor,text='Stop')
button_reset = button(bind=restart,pos = scene.title_anchor,text='Reset')
button_gravity_up = button(bind=gravity_increase,pos = scene.title_anchor,text='Increase Gravity')
button_gravity_down = button(bind=gravity_decrease,pos = scene.title_anchor,text='Decrease Gravity')
button_gravity_earth = button(bind=gravity_earth,pos = scene.title_anchor,text='Earth Gravity')
button_gravity_moon = button(bind=gravity_moon,pos = scene.title_anchor,text='Moon Gravity')
button_gravity_sun = button(bind=gravity_sun,pos = scene.title_anchor,text='Sun Gravity')

def potential_energy(m, g, h):
    pe = m*gravitasi*h
    return pe


def kinetic_energy(m, v):
    ke = 1/2*m*v*v
    return ke


def potential_to_velocity_vector(h):
    v = (math.sqrt(2*gravitasi * h))*-1
    a = vector(0, v, 0)
    return a


def potential_to_velocity(h):
    v = (math.sqrt(2*gravitasi * h))*-1
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
start_timer()
velocity_akhir3=0
def WillJo1():
    global ball, ball_velocity
    global paused
    global time_elapsed
    global t
    global velocity_akhir, velocity_akhir2, velocity_akhir3, velocity_akhir4
    while True:
        rate(80)  # Limit the refresh rate of the scene
        time_elapsed += 1/80

        if paused:
            continue
        # Update position
        ball.pos += ball_velocity * dt
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

            # kondisi sun; gravitasi sun ga jalan
            if (gravitasi == 274):
                    y_v = (potential_to_velocity(10) *
                math.sin(radians(-30)) + 10)
                    x_v = (potential_to_velocity(10) * math.sin(radians(-30)))
            else:
                print(ball.pos)
                y_v = (potential_to_velocity(10) *
                math.sin(radians(-30)) - (t*gravitasi))
                x_v = (potential_to_velocity(10) * math.cos(radians(-30)))*-1
            # y_v = (potential_to_velocity(10) *
            #        math.sin(radians(-30)) - (t*gravitasi))
            # x_v = (potential_to_velocity(10) * math.cos(radians(-30)))*-1    
            ball_velocity.x = x_v
            ball_velocity.y = y_v
            ball.pos += ball_velocity * dt
            velocity_akhir = math.sqrt(math.pow((x_v), 2) + math.pow((y_v), 2))

        # Hitung kecepatan akhir bola (vf) menggunakan persamaan
        # energi mekanik: vf = sqrt(v0^2 + 2 * g * h),
        # di mana h adalah ketinggian jatuh bola tegak lurus
        # (dihitung menggunakan langkah-langkah yang telah dijelaskan sebelumnya).

        if ball.pos.y <= - 3.6 and ball.pos.x > 6.9+willjospecial and \
                ball.pos.y > -8.5 + ball.radius and ball.pos.x < 7.4+willjospecial:
        # if ball.pos.y <= wall_a.pos.y + wall_a.size.y/2-ball.radius and ball.pos.x > 6.9 and \
        #         ball.pos.y > wall_a.pos.y - wall_a.size.y/2+2*ball.radius:
            ball_velocity.x = 0
            ball_velocity.y = -math.sqrt(
                math.pow(velocity_akhir, 2) + 2 * gravitasi * 3.5)
            velocity_akhir = ball_velocity.y
            print(wall_a.pos.y + wall_a.size.y/2-ball.radius)
            print(wall_a.pos.y - wall_a.size.y/2+2*ball.radius)
            # print(wall_a.pos.y + wall_a.size.y/2)
            print(wall_b.pos.y - wall_b.size.y/2- 0.5)
            print(wall_b.pos.y + wall_b.size.y/2)
            print(ball.pos)
            # print(wall_c.pos.y + wall_c.size.y/2)
            # h = 3.5
            ball.pos += ball_velocity * dt
            # print((slope2.pos.y + (slope2.size.x / 2 - 2*ball.radius)
            #        * sin(radians(slope2_angle))))
            # print(velocity_akhir)

        # check if ball hits slope2

        if ball.pos.y >= (slope2.pos.y + (slope2.size.x / 2 - 2*ball.radius)
                            * sin(radians(slope2_angle))-0.5) and ball.pos.y <= -7.5 and ball.pos.x > -4.5+willjospecial:
            if (gravitasi == 274):
                y2_v = 2*(velocity_akhir *
                    math.sin(radians(-30)) - (t*gravitasi)-4.5)
                x2_v = 2*(velocity_akhir * math.cos(radians(-30)))
            else:
                y2_v = (velocity_akhir *
                    math.sin(radians(-30)) - (t*gravitasi)-4.5)
                x2_v = (velocity_akhir * math.cos(radians(-30)))
            ball_velocity.x = x2_v
            ball_velocity.y = y2_v
            ball.pos += ball_velocity * dt
            velocity_akhir2 = math.sqrt(math.pow((x2_v), 2) + math.pow((y2_v), 2))
            # print(velocity_akhir2)

        # Check if the ball hits wall 1 after finish slope 2
        # if ball.pos.x >= -6 - ball.radius and\
        #         ball.pos.y <=  wall_b.pos.y + wall_b.size.y/2 and ball.pos.y >= wall_b.pos.y - wall_b.size.y/2 - 0.5:
            # Check if the ball hits wall 1 after finish slope 2
        if ball.pos.x >= -6+willjospecial - ball.radius and\
                ball.pos.y <= -13 and ball.pos.y >= -19.5 and ball.pos.x < 7.4+willjospecial:
            # wall_b.pos.y + wall_b.size.y/2 = -13
            # -19.5 yang satu lg
            ball_velocity.x = 0
            ball_velocity.y = -math.sqrt(
                math.pow(velocity_akhir2, 2) + 2 * 9.8 * 3.5)
            velocity_akhir2 = ball_velocity.y
            # h = 3.5
            ball.pos += ball_velocity * dt

        # ball hits slope3?
        if ball.pos.y >= (slope3.pos.y + (slope3.size.x / 2 + 2*ball.radius)
                            * sin(radians(slope3_angle))) and ball.pos.y <= -19.5 and ball.pos.x <= slope3.pos.x + \
                (slope3.size.x / 2 + ball.radius) * cos(radians(slope3_angle)):
            y3_v = (velocity_akhir2 *
                    math.sin(radians(-30)) - (t*9.8)-5.5)
            x3_v = (velocity_akhir2 * math.cos(radians(-30)))
            ball_velocity.x = - x3_v
            ball_velocity.y = y3_v
            ball.pos += ball_velocity * dt
            # print(ball.pos.x)
            # print(ball.pos.y)
            velocity_akhir3 = math.sqrt(math.pow((x2_v), 2) + math.pow((y2_v), 2))

        # ball finish slope 3 hits wall 2
        if ball.pos.y <= wall_c.pos.y + wall_c.size.y/2 and ball.pos.x > 6.9+willjospecial and \
                ball.pos.y > wall_c.pos.y - wall_c.size.y/2:
            ball_velocity.x = 0
            ball_velocity.y = -math.sqrt(
                math.pow(velocity_akhir3, 2) + 2 * 9.8 * 7)
            velocity_akhir3 = ball_velocity.y
            print(ball.pos)
            # h = 7 = (30.5-23.6)
            ball.pos += ball_velocity * dt

    # Slope 4 - still progress
        if ball.pos.y >= (slope4.pos.y + (slope4.size.x / 2 - 2*ball.radius)
                            * sin(radians(slope4_angle))-0.5) and ball.pos.y <= -29.5 and ball.pos.x > -4.5+willjospecial:
            y4_v = (velocity_akhir3 *
                    math.sin(radians(-30)) - (t*gravitasi)-7.5)
            x4_v = (velocity_akhir3 * math.cos(radians(-30)))
            ball_velocity.x = x4_v
            ball_velocity.y = y4_v
            ball.pos += ball_velocity * dt
            velocity_akhir4 = math.sqrt(math.pow((x2_v), 2) + math.pow((y2_v), 2))
            # print(velocity_akhir2)
            
    # ground
        if ball.pos.x <= -6+willjospecial and ball.pos.y <= -36.5 and ball.pos.y >= -38.5:
            ball_velocity.y = 0
            ball_velocity.x = -velocity_akhir4
            ball.pos += ball_velocity * dt

        if ball.pos.x <= -20.5+willjospecial and ball.pos.y <= -36.5 and ball.pos.y >= -38.5:
            ball_velocity = vector(0,0,0)
            print("ball hit the end box!")
            label_text = " GOOD GAME!" + " Time elapsed: {} seconds".format(time_elapsed)
            label(pos=vector(-22.5+willjospecial, -39, 0), text=label_text, color=color.white, height=20)
            ball.pos.x = -20.5+willjospecial
            time_elapsed=0
            paused = True
            
        # Increment time
        t += dt

WillJo1()