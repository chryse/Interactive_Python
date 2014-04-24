# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
FAST_BALL = 1.10
SCORE1_POS = [WIDTH * 1/4, HEIGHT / 3]
SCORE2_POS = [WIDTH * 3/4, HEIGHT / 3]
SCORE_SIZE = 50
SCORE_COLOR = "#EEEEEE"
SCORE_FACE = "sans-serif"
CANVAS_BACKGROUND = "#00BB00"
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle1_vel = paddle2_vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction:
        ball_vel = [-random.randrange(2, 4), random.randrange(1, 3)]
    else:
        ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints   
    score1 = score2 = 0
    spawn_ball(RIGHT)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, paddle1_vel, paddle2_vel, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] -= ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    # ball boundary check
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos[1]) and (ball_pos[1] <= (paddle1_pos[1] + PAD_HEIGHT)):
            ball_vel[0] = - ball_vel[0] * FAST_BALL
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if (ball_pos[1] >= paddle2_pos[1]) and (ball_pos[1] <= (paddle2_pos[1] + PAD_HEIGHT)):
            ball_vel[0] = - ball_vel[0] * FAST_BALL
        else:
            spawn_ball(LEFT)
            score1 += 1
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]        
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "#000000", "#EEEEEE")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    # check paddle1 boundary
    if paddle1_pos[1] <= 0:
        paddle1_pos[1] = 0
    elif paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
    
    # check paddle2 boundary
    if paddle2_pos[1] <= 0:
        paddle2_pos[1] = 0
    elif paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT
    
    # draw paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "#AA0000")
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "#0000AA")
    
    # draw scores
    canvas.draw_text(str(score1), SCORE1_POS, SCORE_SIZE, SCORE_COLOR, SCORE_FACE)
    canvas.draw_text(str(score2), SCORE2_POS, SCORE_SIZE, SCORE_COLOR, SCORE_FACE)
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    
       
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = - 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background(CANVAS_BACKGROUND)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)


# start frame
new_game()
frame.start()
