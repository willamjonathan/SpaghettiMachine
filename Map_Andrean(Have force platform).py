from vpython import *

# Create the first rotated box
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

# Kayak Pinball
push_object_length = 10
push_object_width = 10
push_object_height = 1
push_object_pos = vector(-45, -225, 0)

push_object = box(pos=push_object_pos, length=push_object_length, width=push_object_width, height=push_object_height, color=color.magenta)

# Create the ball
ball_radius = 1
ball_pos = vector(-2, 25, 0)
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
    
    if event.key == " ":
        current_zoom = (current_zoom + 1) % len(zoom_levels)  # Cycle through zoom levels
        zoomIn_out(zoom_levels[current_zoom])
    elif event.key == "b":
        toggle_camera_follow()
    

scene.bind("keydown", on_key_down)
# Create the pop-up text
popup_text = None

# Set up the animation
dt = 0.01
scene.width = 1600
scene.height = 1000

collision_first_box = False
while True:

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
    if (side2.pos.y - side2.height/2 - ball.radius) <= ball.pos.y <= (side2.pos.y + side2.height/2 + ball.radius) and \
    (side2.pos.x - side2.length/2 - ball.radius) <= ball.pos.x <= (side2.pos.x + side2.length/2 + ball.radius) and \
    (side2.pos.z - side2.width/2 - ball.radius) <= ball.pos.z <= (side2.pos.z + side2.width/2 + ball.radius):
        ball_velocity.y = abs(ball_velocity.y)
    
    # Check for collision with the third box
    if ball.pos.y < side3.pos.y + side3.height/2 and abs(ball.pos.x - side3.pos.x) < (side3.length/2 - ball.radius) and abs(ball.pos.z - side3.pos.z) < (side3.width/2 - ball.radius):
        ball_velocity = vector(0, 0, 0)  # Set both vertical and horizontal velocities to zero
        ball.pos.y = side3.pos.y + side3.height/2 - ball.radius  # Adjust the position of the ball to be just inside the box
        if popup_text is None:
            popup_text = label(pos=side3.pos + vector(side3.length/2 + 2*ball_radius, 0, 0), text="Good Game", color=color.white)


    
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
    ball_velocity.y -= 9.8 * dt

    # Stop the animation if the ball falls below the ground
    if ball.pos.y < -350:
        break

