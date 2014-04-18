#Simple "screensaver"

import simplegui
import random

# global variables
message = "Python is fun"
interval = 2000
width = 500
height = 500
position = [100, 100]


# event handlers

def update(text):
    global message
    message = text
    
def tick():
    position[0] = random.randrange(0, width)
    position[1] = random.randrange(0, height)
    

def draw(canvas):
    canvas.draw_text(message, position, 20, "Red")
    
    
# create a frame
frame = simplegui.create_frame("Screen Saver", width, height)

# register handlers
timer = simplegui.create_timer(interval, tick)
frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)

# start frame and timer
frame.start()
timer.start()