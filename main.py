from vpython import *
#Web VPython 3.2
from vpython import *
import random

scene.background = vector(135/255, 206/255, 250/255)
#BACKGROUND
background = box(pos = vector(0,-100,-8),length = 250,width = 10, height = 350) 
wood_texture = textures.wood
background.texture = wood_texture

#FLOOR NOW
floor = box(pos = vector(0,-270,-8), length = 250, width = 150, height = 15)
floor.texture = textures.stucco

#Kiri buat jadi box
kiri = box(pos = vector(-135,-100,-8), length = 25, width = 150, height = 350)

#kanan buat jadi box
kanan = box(pos = vector(135,-100,-8), length = 25, width = 150, height = 350)

#tutupan atasnya
atas = box(pos = vector(0,80,-8), length = 250, width = 150, height = 15)

atas.opacity = 0.4
##############

#tilted 30degree box
box_length = 6
box_width = 1.5
box_height = 8
box_thickness = 5
box_angle = 30  # Tilt angle of the box in degrees

side1 = box(pos=vector(0, box_height/2 + 1, 0), length=box_length, width=box_thickness, height=box_width, color=color.blue)
side1.rotate(angle=radians(box_angle), axis=vector(0, 0, 1), origin=vector(0, 0, 0))

# Create the second box
box2_length = 8
box2_width = 1
box2_height = 4
box2_thickness = 3
box2_pos = vector(-58, -20, 0)

side2 = box(pos=box2_pos, length=box2_length, width=box2_thickness, height=box2_height, color=color.green)

# Create the third box
box3_length = 8
box3_width = 1
box3_height = 4
box3_thickness = 3
box3_pos = vector(80, -35, 0)

side3 = box(pos=box3_pos, length=box3_length, width=box3_thickness, height=box3_height, color=color.orange)

# Create the vertical bouncing box
bounce_box_length = 1
bounce_box_width = 1
bounce_box_height = 8
bounce_box_thickness = 3
bounce_box_pos = vector(-107, 7, 0)

bounce_box = box(pos=bounce_box_pos, length=bounce_box_length, width=bounce_box_thickness, height=bounce_box_height, color=color.yellow)

# Bounce to left
new_bounce_box_length = 1
new_bounce_box_width = 1
new_bounce_box_height = 150
new_bounce_box_thickness = 3
new_bounce_box_pos = vector(-40, -150, 0)

new_bounce_box = box(pos=new_bounce_box_pos, length=new_bounce_box_length, width=new_bounce_box_thickness, height=new_bounce_box_height, color=color.yellow)

# Bounce so it go again and again
new_bounce_box_1_length = 1
new_bounce_box_1_width = 1
new_bounce_box_1_height = 150
new_bounce_box_1_thickness = 3
new_bounce_box_1_pos = vector(-50, -150, 0)

new_bounce_box_1 = box(pos=new_bounce_box_1_pos, length=new_bounce_box_1_length, width=new_bounce_box_1_thickness, height=new_bounce_box_1_height, color=color.red)

# Kayak Pin 
push_object_length = 10
push_object_width = 10
push_object_height = 1
push_object_pos = vector(-45, -225, 0)

push_object = box(pos=push_object_pos, length=push_object_length, width=push_object_width, height=push_object_height, color=color.magenta)

sliding_object_length = 40
sliding_object_width = 20
sliding_object_height = 1.5
sliding_object_pos = vector(-50,10,0)

slide1 = box(pos=sliding_object_pos, length=sliding_object_length, width= sliding_object_width, height=sliding_object_height, color=color.blue)
slide1.rotate(angle=radians(25), axis=vector(0, 0, -1), origin=vector(0, 0, 0))

# Create the ball
ball_radius = 1
#ball_pos = vector(-55, 50, 0)
ball_pos = vector(-2, 25, 0) #this is ball pos without sliding object
ball_velocity = vector(0, -1, 0)
ball = sphere(pos=ball_pos, radius=ball_radius, color=color.red)

scene.camera.follow(ball)
camera_follow = True
def zoomIn_out(zoom):
    scene.camera.axis = vector(0, 0, zoom)  # Adjust the axis to point towards the ball
    
def toggle_camera_follow():
    global camera_follow
    
    if camera_follow:
        scene.camera.follow(None)  # Stop following the ball
        camera_follow = False
        zoomIn_out(-700)
    else:
        scene.camera.follow(ball)  # Start following the ball
        camera_follow = True
        zoomIn_out(-115)
    
zoom_levels = [-115, -180, -250]  # Define different zoom levels
current_zoom = 0  # Initial zoom level index

def on_key_down(event):
    global current_zoom
    
    if event.key == "f":
        current_zoom = (current_zoom + 1) % len(zoom_levels)  # Cycle through zoom levels
        zoomIn_out(zoom_levels[current_zoom])
    elif event.key == "b":
        toggle_camera_follow()
    
zoomIn_out(-115)
scene.bind("keydown", on_key_down)
# Create the pop-up text
popup_text = None

# Set up the animation
dt = 0.01
t = 0
scene.width = 800   
scene.height = 500

collision_first_box = False

runLah = True

gravitasi = 9.8

timenow = 0

v0 = 20  # Initial velocity magnitude
angle = radians(45)  # Launch angle in radians

# Calculate the initial velocity components
v0x = v0 * cos(angle)
v0y = v0 * sin(angle)

def reset():
    global ball, ball_velocity  # Declare ball and ball_velocity as global variables
    
    global gravitasi
    global timenow
    global v0,v0x,v0y
    
    timenow = 0
    gravitasi = 9.8
    
    # Reset the ball position, velocity, and color
    ball.pos = ball_pos
    ball_velocity = vector(0, -1, 0)
    ball.color = color.red
    
    v0 = 20  # Initial velocity magnitude
    angle = radians(45)  # Launch angle in radians
    
    # Calculate the initial velocity components
    v0x = v0 * cos(angle)
    v0y = v0 * sin(angle)

button_stop = button(bind=stop,pos = scene.title_anchor,text="Stop")
def stop():
    global runLah
    if runLah:
        runLah = False
        button_stop.text = "Continue"
    elif runLah == False:
        runLah = True
        button_stop.text = "Stop"
        animate()
        
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

rightwind = False
leftwind = False

willjospecial =400

mapnow = "map1"
special_andrean = -2200

def map4():
    global ball
    global ball_pos
    global ball_velocity
    global runlah
    global mapnow
    global timenow 
    global special_andrean
    global gravitasi
    global v0,v0x,v0y
    
    timenow = 0
    
    mapnow = "map4"
    
    ball.radius = 1
    ball_pos = vector(-8 + special_andrean, -4, 0)
    ball.pos.x = -8 + special_andrean
    ball.pos.y = -4
    ball_velocity = vector(0,-gravitasi,0)
    
    v0 = 20  # Initial velocity magnitude
    angle = radians(45)  # Launch angle in radians
    
    # Calculate the initial velocity components
    v0x = v0 * cos(angle)
    v0y = v0 * sin(angle)
    
    stop()
    
def map3():
    global ball
    global ball_pos
    global ball_velocity
    global runlah
    global mapnow
    global timenow 
    
    timenow = 0
    
    mapnow = "map3"
    
    ball.radius = 1
    ball_pos = vector(-445, -50, 0)
    ball.pos.x = -445
    ball.pos.y = -50
    ball_velocity = vector(0,-9.8,0)
    
    
    stop()
    
def map2():
    global ball
    global ball_pos
    global ball_velocity
    global runlah
    global mapnow
    global timenow 
    
    timenow = 0
    
    mapnow = "map2"
    
    ball.radius = 0.5
    ball_pos = vector(-6.0+willjospecial, 15, 0)
    ball.pos.x = -6.0+willjospecial
    ball.pos.y = 15
    ball_velocity = vector(0,0,0)
    
    
    stop()
#    reset()
    
def map1():
    global ball
    global ball_pos
    global ball_velocity
    global runlah
    global mapnow
    global timenow 
    
    timenow = 0
    
    mapnow = "map1"
    
    ball.radius = 1
    ball_pos = vector(-2, 25, 0)
    ball.pos.x = -2
    ball.pos.y = 25
    ball_velocity = vector(0,-1,0)
    

    stop()
#    reset()
    
button_reset = button(bind=reset,pos = scene.title_anchor,text='Reset')
button_gravity_up = button(bind=gravity_increase,pos = scene.title_anchor,text='Increase Gravity')
button_gravity_down = button(bind=gravity_decrease,pos = scene.title_anchor,text='Decrease Gravity')
button_gravity_earth = button(bind=gravity_earth,pos = scene.title_anchor,text='Earth Gravity')
button_gravity_moon = button(bind=gravity_moon,pos = scene.title_anchor,text='Moon Gravity')
button_gravity_sun = button(bind=gravity_sun,pos = scene.title_anchor,text='Sun Gravity')

button_map1 = button(bind= map1,pos = scene.title_anchor,text = "MAP1")
button_map2 = button(bind= map2,pos = scene.title_anchor,text = "MAP2")
button_map3 = button(bind= map3,pos = scene.title_anchor,text = "MAP3")
button_map4 = button(bind= map4,pos = scene.title_anchor,text = "MAP4")

#THIS IS FOR THE WIND

wind_particles = []

# Function to create a wind particle
def create_wind_particle():
    particle = sphere(pos=vector(-180, -75, 25), radius=0.3, color=color.white)
    particle.velocity = vector(random.uniform(0.05, 0.2), 0, 0)
    wind_particles.append(particle)

# Function to update the wind particles and create new particles when needed
def update_wind_particles():
    particles_to_remove = []
    num_particles = len(wind_particles)

    for i in range(num_particles):
        particle = wind_particles[i]
        particle.pos += particle.velocity

#        # Wrap the particle's x-position to the beginning if it goes beyond the limit
#        if particle.pos.x > 400:
#            particle.pos.x = -400

        # Randomly change the velocity of the particle within a range
        particle.velocity.x += random.uniform(0, 0.05)
        particle.velocity.y += random.uniform(-0.05, 0.05)
        particle.velocity.z += random.uniform(-0.01,0.01)

        # Check if a particle has passed the x-coordinate of 80
        if particle.pos.x > 400:
            particles_to_remove.append(i)

    # Remove the particles that have passed the x-coordinate of 80 and make them invisible
    for index in reversed(particles_to_remove):
        particle = wind_particles.pop(index)
        particle.visible = False

    # Create new wind particles to replace the removed particles
    num_removed_particles = len(particles_to_remove)
    for _ in range(num_removed_particles):
        create_wind_particle()

# Create initial wind particles
num_particles = 750
for _ in range(num_particles):
    create_wind_particle()

#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT I MEAN LEFT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
wind_particlez = []

# Function to create a wind particle
def create_wind_particlez():
    particle = sphere(pos=vector(180, -75, 25), radius=0.3, color=color.black)
    particle.velocity = vector(random.uniform(-0.2, -0.05), 0, 0)
    wind_particlez.append(particle)

# Function to update the wind particles and create new particles when needed
def update_wind_particlez():
    particles_to_remove = []
    num_particles = len(wind_particlez)

    for i in range(num_particles):
        particle = wind_particlez[i]
        particle.pos += particle.velocity


        # Randomly change the velocity of the particle within a range
        particle.velocity.x -= random.uniform(0, 0.05)
        particle.velocity.y -= random.uniform(-0.15, 0.15)
        particle.velocity.z -= random.uniform(-0.01, 0.01)

        # Check if a particle has passed the x-coordinate of -400
        if particle.pos.x < -400:
            particles_to_remove.append(i)

    # Remove the particles that have passed the x-coordinate of -400 and make them invisible
    for index in reversed(particles_to_remove):
        particle = wind_particlez.pop(index)
        particle.visible = False

    # Create new wind particles to replace the removed particles
    num_removed_particles = len(particles_to_remove)
    for _ in range(num_removed_particles):
        create_wind_particlez()

# Create initial wind particles
num_particlez = 750
for _ in range(num_particles):
    create_wind_particlez()
    
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT I MEAN LEFT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
#TO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTT
#WINDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
def wind_to_right():
    global rightwind
    global wind_particles
    global ball_velocity
    if (rightwind == False):
        rightwind = True
        ball_velocity.x +=  5.83 #35x human blow
        for particle in wind_particles:
            particle.visible = True
        
    elif rightwind == True:
        rightwind = False
        ball_velocity.x -=  5.83 #35x human blow
        for particle in wind_particles:
            particle.visible = False

    
def wind_to_left():
    global leftwind
    
    if(leftwind == False):
        leftwind = True
        ball_velocity.x -=  5.83 #35x human blow
        for particle in wind_particlez:
            particle.visible = True
    elif (leftwind) :
        leftwind = False
        ball_velocity.x +=  5.83 #35x human blow
        for particle in wind_particlez:
            particle.visible = False
        
button_wind_right = button(bind=wind_to_right,pos = scene.title_anchor,text='WindToRight')
button_wind_left = button(bind=wind_to_left,pos = scene.title_anchor,text='WindToLeft')
#WINDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD



##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
##
##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
h = 15  # heightnya 10 ini soalnya slope kan jadi miring
b = 10  # heightnya 5 ini

# dia ditaruh di height:10 di atas slope
def start_timer():
    global time_elapsed
    time_elapsed = 0


cekposisi = box(pos=vector(-6+willjospecial, -37.5, 0),size=vector(1, 1, 0), color=color.yellow)

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
# print(sin(-30)*slope1.pos.y + slope1.size.y + ball.size.y)
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

start_timer()
velocity_akhir3=0

def potential_energy(m, g, h):
    pe = m*gravitasi*h
    return pe


def kinetic_energy(m, v):
    ke = 1/2*m*v*v
    return ke


def potential_to_velocity_vector(h):
    v = (sqrt(2*gravitasi * h))*-1

    a = vector(0, v, 0)
    return a


def potential_to_velocity(h):
    v = (sqrt(2*gravitasi * h))*-1

    return v
##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
##
##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2

##MAP3333333333333333333333333333333333333333333333
##MAP3333333333333333333333333333333333333333333333
##MAP3333333333333333333333333333333333333333333333


# Create the half cylinder
resize_now = 12
cylinder_radius = 8 * resize_now
cylinder_height = 15 * resize_now
cylinder_thickness = 1 * resize_now / 2

# Create the base of the half cylinder
ring_top = cylinder(pos=vector(-350 - cylinder_radius, cylinder_height / 2 - 1, 0), axis=vector(0, cylinder_thickness, 0), radius=cylinder_radius, color=color.blue)
ring_top.opacity = 0.5

ring = cylinder(pos=vector(-350 - cylinder_radius, -cylinder_height / 2, 0), axis=vector(0, cylinder_thickness, 0), radius=cylinder_radius, color=color.blue)

# Create the curved surface of the half cylinder
num_segments = 100
angle = pi
dtheta = angle / num_segments

# Create the trampoline structure
box_size = cylinder_radius * 2 / num_segments

for i in range(num_segments):
    theta = angle - i * dtheta + 3.15
    x = cylinder_radius * cos(theta) - cylinder_radius - 350
    y = cylinder_radius * sin(theta)

    top = vector(x, cylinder_height / 2, y)
    bottom = vector(x, -cylinder_height / 2, y)
    side = cylinder(pos=top, axis=bottom - top, radius=cylinder_thickness, color=color.blue)
    side.rotate(angle=pi, axis=vector(0, 1, 0))

ring = cylinder(pos=vector(-350 - cylinder_radius, -cylinder_height / 2.5 , 0), axis=vector(0, cylinder_thickness, 0), radius=cylinder_radius/4, color=color.red)

box_length_trampoline = 30
box_width_trampoline = 2.5
box_height_trampoline = 8
box_thickness_trampoline = 15
box_angle_trampoline = 30  # Tilt angle of the box in degrees

side1_yes = box(pos=vector(0 - 350, box_height_trampoline/2 + 1+280, 0), length=box_length_trampoline, width=box_thickness_trampoline, height=box_width_trampoline, color=color.blue)
side1_yes.rotate(angle=radians(box_angle_trampoline), axis=vector(0, 0, 1), origin=vector(0, 0, 0))

box_length_trampolines = 30
box_width_trampolines = 2.5
box_height_trampolines = 8
box_thickness_trampolines = 15
box_angle_trampolines = 30  # Tilt angle of the box in degrees

side3_yes = box(pos=vector(0 - 320, box_height_trampolines/2 + 1+210, 0), length=box_length_trampolines, width=box_thickness_trampolines, height=box_width_trampolines, color=color.white)
side3_yes.rotate(angle=radians(box_angle_trampolines), axis=vector(0, 0, 1), origin=vector(0, 0, 0))


# Create a panel to display the time estimate

bottom_pos = vector(0, -scene.range.y, 0)
panel = wtext(text=('Time Estimate: '+timenow+' seconds'), align='left', height=30, pos=scene.bottom_pos, box=False)
mantulatas = False

mantultrampoline = False
titikatas = -50
mantulyes = 22

box_length_trampolines = 30
box_width_trampolines = 2.5
box_height_trampolines = 8
box_thickness_trampolines = 15
box_angle_trampolines = 45  # Tilt angle of the box in degrees

side2_yes = box(pos=vector(0 - 330, box_height_trampolines/2 + 1+370, 0), length=box_length_trampolines, width=box_thickness_trampolines, height=box_width_trampolines, color=color.white)
side2_yes.rotate(angle=radians(box_angle_trampolines), axis=vector(0, 0, 1), origin=vector(0, 0, 0))

box_length_trampoline = 30
box_width_trampoline = 10
box_height_trampoline = 8
box_thickness_trampoline = 15
box_angle_trampoline = 30  # Tilt angle of the box in degrees

side4_yes = box(pos=vector(0 - 530, -50, 0), length=box_length_trampoline, width=box_thickness_trampoline, height=box_width_trampoline, color=color.yellow)

box_length_trampoline = 10
box_width_trampoline = 30
box_height_trampoline = 10
box_thickness_trampoline = 15
box_angle_trampoline = 30  # Tilt angle of the box in degrees

side5_yes = box(pos=vector(0 - 530, -70, 0), length=box_length_trampoline, width=box_thickness_trampoline, height=box_width_trampoline, color=color.black)
##MAP3333333333333333333333333333333333333333333333
##MAP3333333333333333333333333333333333333333333333
##MAP3333333333333333333333333333333333333333333333

##MAP4444444444444444444444444444444444444444444444
##MAP4444444444444444444444444444444444444444444444
##MAP4444444444444444444444444444444444444444444444
special_andrean = -1200

# Create the grounds
base = box(pos=vector(0 + special_andrean + 200, -105, 0), size=vector(500, 15, 100), color=color.yellow)
base.texture = textures.wood

base_back = box(pos=vector(0 + special_andrean + 200, 50, -5), size=vector(500, 300, 10), color=color.white)
base_back.texture = textures.wood
# Left pillar
left_pillar = cylinder(
    pos=vector(-250 + special_andrean + 200, -97.5, -5),
    axis=vector(0, 300, 0),
    radius=25,
    color=color.gray(0.7),
)
left_pillar.texture = textures.metal

# Right pillar
right_pillar = cylinder(
    pos=vector(250 + special_andrean + 200, -97.5, -5),
    axis=vector(0, 300, 0),
    radius=25,
    color=color.gray(0.7),
)
right_pillar.texture = textures.metal
############
ground1 = box(pos=vector(0 + special_andrean, -5, 0), size=vector(20, 3.5, 20), color=color.white)
ground1.texture = textures.metal
pillar1 = cylinder(
    pos=vector(special_andrean, -105, 0),
    axis=vector(0, 100, 0),
    radius=5,
    color=color.gray(0.3),
)
pillar1.texture = textures.metal

ground2 = box(pos=vector(40 + special_andrean, -10, 0), size=vector(20, 3.5, 20), color=color.white)
ground2.texture = textures.metal
pillar2 = cylinder(
    pos=vector(special_andrean + 40, -100, 0),
    axis=vector(0, 90, 0),
    radius=5,
    color=color.gray(0.3),
)
pillar2.texture = textures.metal

ground3 = box(pos=vector(80 + special_andrean, -15, 0), size=vector(20, 3.5, 20), color=color.white)
ground3.texture = textures.metal
pillar3 = cylinder(
    pos=vector(special_andrean + 80, -100, 0),
    axis=vector(0, 85, 0),
    radius=5,
    color=color.gray(0.3),
)
pillar3.texture = textures.metal

ground4 = box(pos=vector(120 + special_andrean, -20, 0), size=vector(20, 3.5, 20), color=color.white)
ground4.texture = textures.metal
pillar4 = cylinder(
    pos=vector(special_andrean + 120, -100, 0),
    axis=vector(0, 80, 0),
    radius=5,
    color=color.gray(0.3),
)
pillar4.texture = textures.metal

ground5 = box(pos=vector(160 + special_andrean, -25, 0), size=vector(20, 3.5, 20), color=color.blue)
ground5.texture = textures.stucco
pillar5 = cylinder(
    pos=vector(special_andrean + 160, -100, 0),
    axis=vector(0, 75, 0),
    radius=5,
    color=color.gray(0.3),
)
pillar5.texture = textures.metal

ground6 = box(pos=vector(305 + special_andrean, 125, 0), size=vector(28, 4, 28), color=color.orange)
pillar6 = cylinder(
    pos=vector(special_andrean + 305, -100, 0),
    axis=vector(0, 225, 0),
    radius=5,
    color=color.red,
)
pillar6.texture = textures.metal

# Set the initial velocity and angle
#v0 = 20  # Initial velocity magnitude
#angle = radians(45)  # Launch angle in radians
#
## Calculate the initial velocity components
#v0x = v0 * cos(angle)
#v0y = v0 * sin(angle)

# Set the bounce factor
bounce_factor = 0.8

# Launch the ball
t = 0
dt = 0.01

# Create the body
body = sphere(pos=vector(0 + special_andrean + 305, 0 + 132, 0), radius=2, color=color.red)

# Create the eyes
left_eye = sphere(pos=vector(-0.7 + special_andrean + 305, 1 + 132, 1), radius=0.8, color=color.yellow)
right_eye = sphere(pos=vector(0.7 + special_andrean + 305, 1 + 132, 1), radius=0.8, color=color.yellow)

# Create the mouth
mouth = cone(pos=vector(0 + special_andrean + 305, -0.5 + 132, 1.3), axis=vector(0, -1, 0), radius=1, color=color.green)

# Create the horns
left_horn = pyramid(pos=vector(-1 + special_andrean + 305, 2.5 + 132, 0), size=vector(1, 2, 1), color=color.blue)
right_horn = pyramid(pos=vector(0.5 + special_andrean + 305, 2.5 + 132, 0), size=vector(1, 2, 1), color=color.blue)

# Create the arms
left_arm = box(pos=vector(-2.5 + special_andrean + 305, 0 + 132, 0), size=vector(1, 2, 1), color=color.orange)
right_arm = box(pos=vector(2.5 + special_andrean + 305, 0 + 132, 0), size=vector(1, 2, 1), color=color.orange)

# Create the legs
left_leg = cylinder(pos=vector(-1 + special_andrean + 305, -2 + 132, 0), axis=vector(0, -2, 0), radius=0.5, color=color.purple)
right_leg = cylinder(pos=vector(1 + special_andrean + 305, -2 + 132, 0), axis=vector(0, -2, 0), radius=0.5, color=color.purple)

scene.camera.follow(ball)

num_particlezz = 100
particlez = []
has_particles = True
##MAP4444444444444444444444444444444444444444444444
##MAP4444444444444444444444444444444444444444444444
##MAP4444444444444444444444444444444444444444444444
def animate():
    global ball, ball_velocity,button_stop,stop_or_start, ball_pos
    global time_elapsed
    global t
    global velocity_akhir, velocity_akhir2, velocity_akhir3, velocity_akhir4
    global willjospecial
    global mapnow
    global dt
    global ball, ball_velocity
    global mantulatas,titikatas,mantultrampoline,mantulyes
    global timenow,panel
    global v0x,v0y
    global particlez
    global num_particlezz
    while runLah:
        timenow += 1/150
        timenow_formatted = "{:.2f}".format(timenow)
        
        panel.text = 'Time Estimate: '+timenow_formatted+' seconds'
        if mapnow == "map1":
            rate(150)
           
            ball.pos = ball.pos + ball_velocity * dt
        
             # Check for collision with the inclined surface of the first box
            delta1 = ball.pos - side1.pos
            delta_rotated1 = rotate(delta1, angle=radians(-box_angle), axis=vector(0, 0, 1))
        
            if abs(delta_rotated1.x) < (side1.length/2 - ball.radius) and abs(delta_rotated1.z) < (side1.width/2 - ball.radius):
                if 0 < delta_rotated1.y < (side1.height/2 + ball.radius):
                    # Reflect the velocity
                    normal = rotate(vector(0, 1, 0), angle=radians(box_angle), axis=vector(0, 0, 1))
                    ball_velocity = ball_velocity - 2 * dot(ball_velocity, normal) * normal
        
                    # Reset the collision flag for the first box
                    collision_first_box = False
        
                    # Add a small delay to prevent immediate re-collision
                    rate(10)
            else:
                # If the ball is not colliding with the first box, reset the collision flag
                collision_first_box = False
        
            # Check for collisions with the second box
            if (side2.pos.y - side2.height/2 - ball.radius) <= ball.pos.y <= (side2.pos.y + side2.height/2 + ball.radius) and (side2.pos.x - side2.length/2 - ball.radius) <= ball.pos.x <= (side2.pos.x + side2.length/2 + ball.radius) and (side2.pos.z - side2.width/2 - ball.radius) <= ball.pos.z <= (side2.pos.z + side2.width/2 + ball.radius):
                ball_velocity.y = abs(ball_velocity.y)
            
            # Check for collision with the third box
            if ball.pos.y < side3.pos.y + side3.height/2 and abs(ball.pos.x - side3.pos.x) < (side3.length/2 - ball.radius) and abs(ball.pos.z - side3.pos.z) < (side3.width/2 - ball.radius):
                ball_velocity = vector(0, 0, 0)  # Set both vertical and horizontal velocities to zero
                ball.pos.y = side3.pos.y + side3.height/2 - ball.radius  # Adjust the position of the ball to be just inside the box
            #           
                #this will give GOOD GAME TEXT TO SHOW THE USER ALREADY WIN
                popup_text = label(pos=side3.pos + vector(side3.length/2 + 2*ball_radius, 0, 0), text="Good Game", color=color.white)
                break
        
        
            
            # Check for collision with the bouncing box
            if (ball.pos.y - ball.radius <= bounce_box.pos.y + bounce_box.height/2) and \
            (abs(ball.pos.x - bounce_box.pos.x) < (bounce_box.length/2 + ball.radius)) and \
            (abs(ball.pos.z - bounce_box.pos.z) < (bounce_box.width/2 - ball.radius)):
        
                # Check if the ball is in contact with the top surface of the bouncing box
                if ball.pos.y - ball.radius <= bounce_box.pos.y + bounce_box.height/2:
                    ball_velocity.x = abs(ball_velocity.x)
        
            # Check for collision with the new bouncing box
            if (ball.pos.y - ball.radius <= new_bounce_box.pos.y + new_bounce_box.height/2) and \
            (new_bounce_box.pos.x - new_bounce_box.length/2 - ball.radius) <= ball.pos.x <= (new_bounce_box.pos.x + new_bounce_box.length/2 + ball.radius) and \
            (new_bounce_box.pos.z - new_bounce_box.width/2 - ball.radius) <= ball.pos.z <= (new_bounce_box.pos.z + new_bounce_box.width/2 + ball.radius):
        
                # Check if the ball is in contact with the top surface of the new bouncing box
                if ball.pos.y - ball.radius <= new_bounce_box.pos.y + new_bounce_box.height/2:
                    ball_velocity.x = -abs(ball_velocity.x)
                    
            # Check for collision with new_bouncing_box_1
            if (ball.pos.y - ball.radius <= new_bounce_box_1.pos.y + new_bounce_box_1.height/2) and \
                (abs(ball.pos.x - new_bounce_box_1.pos.x) < (new_bounce_box_1.length/2 + ball.radius)) and \
                (abs(ball.pos.z - new_bounce_box_1.pos.z) < (new_bounce_box_1.width/2 - ball.radius)):
        
                # Check if the ball is in contact with the top surface of the new_bouncing_box_1
                if ball.pos.y - ball.radius <= new_bounce_box_1.pos.y + new_bounce_box_1.height/2:
                    ball_velocity.x = abs(ball_velocity.x)
        
            # Check for collision with the new object
            if (ball.pos.y - ball.radius <= push_object.pos.y + push_object.height/2) and \
                (abs(ball.pos.x - push_object.pos.x) < (push_object.length/2 + ball.radius)) and \
                (abs(ball.pos.z - push_object.pos.z) < (push_object.width/2 - ball.radius)):
        
                # Check if the ball is in contact with the top surface of the new object
                if ball.pos.y - ball.radius <= push_object.pos.y + push_object.height/2:
                    ball_velocity.y = abs(ball_velocity.y) + 2 # Apply the force of 40 N to the ball
        
            # Apply gravity
            ball_velocity.y -= gravitasi * dt
            
            if (rightwind):
                update_wind_particles()
                
            if (leftwind):
                update_wind_particlez()
        
            # Stop the animation if the ball falls below the ground
            if ball.pos.y < -350:
                break
        
        elif mapnow == "map2":
            ##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
            ##
            ##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
            rate(80)  # Limit the refresh rate of the scene
            time_elapsed += 1/80
            
            # Update position
            ball.pos += ball_velocity * dt

            # Apply gravity
            ball_velocity += potential_to_velocity_vector(10) * dt
    
    
             # Check if the ball hits slope 1
            if ball.pos.y >= (slope1.pos.y + (slope1.size.x / 2 + 2*ball.radius) * sin(radians(slope1_angle))) and ball.pos.y <= 4.5 and ball.pos.x <= slope1.pos.x + (slope1.size.x / 2 + ball.radius) * cos(radians(slope1_angle)):
    
                if (gravitasi == 274):
                    y_v = (potential_to_velocity(10) * sin(radians(-30)) + 10)
                    x_v = (potential_to_velocity(10) * sin(radians(-30)))
                else:
                    print(ball.pos)
                    y_v = (potential_to_velocity(10) * sin(radians(-30)) - (t*gravitasi))
                    x_v = (potential_to_velocity(10) * cos(radians(-30)))*-1

                ball_velocity.x = x_v
                ball_velocity.y = y_v
                ball.pos += ball_velocity * dt
                velocity_akhir = sqrt(pow((x_v), 2) + pow((y_v), 2))
    
            if ball.pos.y <= - 3.6 and ball.pos.x > 6.9+willjospecial and ball.pos.y > -8.5 + ball.radius and ball.pos.x < 7.4+willjospecial:

                ball_velocity.x = 0
                ball_velocity.y = -sqrt(pow(velocity_akhir, 2) + 2 * gravitasi * 3.5)
                velocity_akhir = ball_velocity.y

                ball.pos += ball_velocity * dt

    
            # check if ball hits slope2
    
            if ball.pos.y >= (slope2.pos.y + (slope2.size.x / 2 - 2*ball.radius) * sin(radians(slope2_angle))-0.5) and ball.pos.y <= -7.5 and ball.pos.x > -4.5+willjospecial:
                if (gravitasi == 274):
                    y2_v = 2*(velocity_akhir *
                        sin(radians(-30)) - (t*gravitasi)-4.5)
                    x2_v = 2*(velocity_akhir * cos(radians(-30)))
                else:
                    y2_v = (velocity_akhir *
                        sin(radians(-30)) - (t*gravitasi)-4.5)
                    x2_v = (velocity_akhir * cos(radians(-30)))
                ball_velocity.x = x2_v
                ball_velocity.y = y2_v
                ball.pos += ball_velocity * dt
                velocity_akhir2 = sqrt(pow((x2_v), 2) + pow((y2_v), 2))

            if ball.pos.x >= -6+willjospecial - ball.radius and ball.pos.y <= -13 and ball.pos.y >= -19.5 and ball.pos.x < 7.4+willjospecial:

                ball_velocity.x = 0
                ball_velocity.y = -sqrt(
                    pow(velocity_akhir2, 2) + 2 * 9.8 * 3.5)
                velocity_akhir2 = ball_velocity.y
                # h = 3.5
                ball.pos += ball_velocity * dt
    
            # ball hits slope3?
            if ball.pos.y >= (slope3.pos.y + (slope3.size.x / 2 + 2*ball.radius) * sin(radians(slope3_angle))) and ball.pos.y <= -19.5 and ball.pos.x <= slope3.pos.x + (slope3.size.x / 2 + ball.radius) * cos(radians(slope3_angle)):
                y3_v = (velocity_akhir2 * sin(radians(-30)) - (t*9.8)-5.5)
                x3_v = (velocity_akhir2 * cos(radians(-30)))
                ball_velocity.x = - x3_v
                ball_velocity.y = y3_v
                ball.pos += ball_velocity * dt

                velocity_akhir3 = sqrt(pow((x2_v), 2) + pow((y2_v), 2))
    
            # ball finish slope 3 hits wall 2
            if ball.pos.y <= wall_c.pos.y + wall_c.size.y/2 and ball.pos.x > 6.9+willjospecial and ball.pos.y > wall_c.pos.y - wall_c.size.y/2:
                ball_velocity.x = 0
                ball_velocity.y = -sqrt(pow(velocity_akhir3, 2) + 2 * 9.8 * 7)
                velocity_akhir3 = ball_velocity.y
                print(ball.pos)
                # h = 7 = (30.5-23.6)
                ball.pos += ball_velocity * dt
    
        # Slope 4 - still progress
            if ball.pos.y >= (slope4.pos.y + (slope4.size.x / 2 - 2*ball.radius) * sin(radians(slope4_angle))-0.5) and ball.pos.y <= -29.5 and ball.pos.x > -4.5+willjospecial:
                y4_v = (velocity_akhir3 * sin(radians(-30)) - (t*gravitasi)-7.5)
                x4_v = (velocity_akhir3 * cos(radians(-30)))
                ball_velocity.x = x4_v
                ball_velocity.y = y4_v
                ball.pos += ball_velocity * dt
                velocity_akhir4 = sqrt(pow((x2_v), 2) + pow((y2_v), 2))
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
        
            ##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2
            ##
            ##WILLJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPUNYA MAP 2

        elif mapnow == "map3":
            rate(150) 

            if (mantulatas == False):
                if(mantultrampoline and ball.pos.y < titikatas):
                    mantulyes -= 0.5
                    ball_velocity.y = titikatas/10 + mantulyes - gravitasi
                elif(mantultrampoline and ball.pos.y > titikatas):
                    mantultrampoline = False
                else:
                    ball_velocity.y = -gravitasi-15
        
            ball.pos = ball.pos + ball_velocity * dt
            
            if(ball.pos.y < (-cylinder_height / 2.5+cylinder_thickness)):
                ball_velocity.y += 20
                titikatas += (5+titikatas/20)
                mantultrampoline = True
                
            if(ball.pos.y >70):
                ball_velocity = vector(45,-25,0)
                mantulatas = True
        
            if(ball.pos.y < 31 and mantulatas and ball.pos.x > -373 and ball.pos.x < -370):
                ball_velocity = vector(-45,0,0)
            
            if(ball.pos.y < 31 and mantulatas and ball.pos.x < -500):
                ball_velocity = vector(-12,-28,0)
                
            if(ball.pos.x < -500 and ball.pos.y <= -50):
                break
            
        elif mapnow == "map4":
            rate(150)
            
            ball_velocity = vector(0,-gravitasi,0)
            ball.pos.x += v0x * dt
            ball.pos.y += v0y * dt + 0.5 * ball_velocity.y * dt**2
            ball.pos.z += 0.5 * ball_velocity.z * dt**2
        
            # Check for collision with the grounds
            if ball.pos.y - ball.radius <= ground1.pos.y + ground1.size.y / 2 and ball.pos.x >= ground1.pos.x - ground1.size.x / 2 and ball.pos.x <= ground1.pos.x + ground1.size.x / 2 and v0y < 0:
                v0y *= -bounce_factor  # Reverse the vertical velocity
            if ball.pos.y - ball.radius <= ground2.pos.y + ground2.size.y / 2 and ball.pos.x >= ground2.pos.x - ground2.size.x / 2 and ball.pos.x <= ground2.pos.x + ground2.size.x / 2 and v0y < 0:
                v0y *= -bounce_factor  # Reverse the vertical velocity
            if ball.pos.y - ball.radius <= ground3.pos.y + ground3.size.y / 2 and ball.pos.x >= ground3.pos.x - ground3.size.x / 2 and ball.pos.x <= ground3.pos.x + ground3.size.x / 2 and v0y < 0:
                v0y *= -bounce_factor  # Reverse the vertical velocity
            if ball.pos.y - ball.radius <= ground4.pos.y + ground4.size.y / 2 and ball.pos.x >= ground4.pos.x - ground4.size.x / 2 and ball.pos.x <= ground4.pos.x + ground4.size.x / 2 and v0y < 0:
                v0y *= -bounce_factor  # Reverse the vertical velocity
            if ball.pos.y - ball.radius <= ground5.pos.y + ground5.size.y / 2 and ball.pos.x >= ground5.pos.x - ground5.size.x / 2 and ball.pos.x <= ground5.pos.x + ground5.size.x / 2 and v0y < 0:
                v0y *= -5*bounce_factor  # Reverse the vertical velocity
            if ball.pos.y - ball.radius <= body.pos.y + body.size.y / 2 and ball.pos.x >= body.pos.x - body.size.x / 2 and ball.pos.x <= body.pos.x + body.size.x / 2 and v0y < 0:
                v0x = 0
                v0y = 0
                ball_velocity = vector(0, 0, 0)
                for _ in range(num_particlezz):
                    particle = sphere(pos=ball.pos, radius=1, color=color.red)
                    particle.velocity = vector(random.uniform(-5, 5), random.uniform(0, 10), random.uniform(-5, 5))
                    particlez.append(particle)
                    print("particle")
        
            # Update the ball's velocity due to gravity
            v0y += ball_velocity.y * dt
        
            # Add the current position to the trail
#            ball.trail.append(pos=ball.pos)
            
            for particle in particlez:
                 particle.pos += particle.velocity * dt
                 particle.velocity += ball_velocity * dt
                
                 if particle.pos.y <= ground6.pos.y + ground6.size.y / 2:
                     particlez.remove(particle)
    
                     break
        
            # Remove particlez that have fallen below the ground
        #    particlez = [particle for particle in particlez if particle.pos.y > ground6.pos.y + ground6.size.y / 2 + particle.radius]
            
            # Update time

            
animate()