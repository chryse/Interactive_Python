# template for "Stopwatch: The Game"

import simplegui

# define global variables
time_text = 0
width = 400
height = 400
position = [width/2 - 30, height/2]
interval = 100
total_stop = 0
right_stop = 0
stop_position = [width-60, 30]
point_sign = [width-100, 50]
point_sign_font_size = 16
stop_point_font_size = 20
is_start = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    point_seconds = t % 10
    seconds = (t - point_seconds) / 10
    minutes = 0
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
    if seconds < 10:
        return str(minutes) + ":" + "0" + str(seconds) + "." + str(point_seconds)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(point_seconds)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_start
    is_start = True
    timer.start()

def stop():
    timer.stop()
    global total_stop, right_stop, time_text, is_start
    if is_start != False:
        total_stop += 1
        if time_text % 10 == 0:
            right_stop += 1
#        print time_text
        is_start = False

def reset():
    timer.stop()
    global time_text, total_stop, right_stop, is_start
    time_text = 0
    total_stop = 0
    right_stop = 0
    is_start = False
    

# define event handler for timer with 0.1 sec interval
def start_watch():
    global time_text
    time_text += 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_text), position, 30, "Black")
    canvas.draw_text(str(right_stop) + " / " + str(total_stop), stop_position, stop_point_font_size, "Black")
    canvas.draw_text("success / tries", point_sign, point_sign_font_size, "Black")

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.set_canvas_background("White")

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, start_watch)


# start frame
frame.start()

# Please remember to review the grading rubric
