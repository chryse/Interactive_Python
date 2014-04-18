# Truck drawing
import simplegui

def draw_truck(canvas):
    canvas.draw_circle((90, 200), 20, 10, "White")
    canvas.draw_circle((210,200), 20, 10, "White")
    canvas.draw_line((50,180), (250,180), 40, "Red")
    canvas.draw_line((55, 170), (90, 120), 5, "Red")
    canvas.draw_line((90, 120), (130, 120), 5, "Red")
    canvas.draw_line((180, 108), (180, 160), 140, "Red")
    
def draw_archery(canvas):
    canvas.draw_circle((150,150), 40, 1, "Black", "Red")
    canvas.draw_circle((150,150), 30, 1, "Black", "Red")
    canvas.draw_circle((150,150), 20, 1, "Black", "Yellow")
    canvas.draw_circle((150,150), 10, 1, "Black", "Yellow")
        
    
frame = simplegui.create_frame("", 300, 300)

frame.set_draw_handler(draw_truck)

frame.start()
