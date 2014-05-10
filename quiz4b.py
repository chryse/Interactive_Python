import simplegui


key_value = 5
count = 0

def keydown(key):
    global key_value, count
    key_value = key_value * 2
    count += 1
    print "Count: " + str(count)
#    print key_value
    

def keyup(key):
    global key_value
    key_value = key_value - 3
    print key_value
    print

def draw(c):
    pass


frame = simplegui.create_frame("", 100, 100)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()