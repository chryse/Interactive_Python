# Card game - Memory

import simplegui
import random

CARD_WIDTH = 50

# helper function to initialize globals
def new_game():
    global card_list,exposed_list,game_state,turns,select_card_1, select_card_2
    game_state = 0
    turns = 0
    card_list = range(8)
    card_list.extend(range(8))
    random.shuffle(card_list)
    exposed_list = [False for n in range(len(card_list))]
    select_card_1 = select_card_2 = -1    
     
# define event handlers
def mouseclick(pos):
    global game_state,turns, select_card_1, select_card_2
    card_clicked  = pos[0]/CARD_WIDTH
    
    if not exposed_list[card_clicked]:
        exposed_list[card_clicked] = True
        if game_state == 0:
            game_state = 1
            select_card_1 = card_clicked
            turns = 1
        elif game_state == 1:
            exposed_list[card_clicked] = True
            select_card_2 = card_clicked
            game_state = 2
        elif game_state == 2: 
            game_state = 1
            if card_list[select_card_1] != card_list[select_card_2]:
                exposed_list[select_card_1] = exposed_list[select_card_2] = False
            select_card_1 = card_clicked
            turns += 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(len(card_list)):
        left_border  = n*CARD_WIDTH
        right_border = n*CARD_WIDTH+CARD_WIDTH
        if exposed_list[n]:
            canvas.draw_text(str(card_list[n]), (left_border + 5, 75), 75, 'White')
        else:
            canvas.draw_polygon([(left_border,0), (right_border,0), (right_border,100), (left_border,100)], 1, 'red', 'green')
        
        label.set_text("Turns = " + str(turns))
        #canvas.draw_line((num*50 + 50, 0), (num*50 + 50, 100), 1, 'red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric