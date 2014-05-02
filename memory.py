# implementation of card game - Memory

import simplegui
import random

card_images_url = []
card_images_done_url = []          
card_face_url = "http://hyunjunkim.com/images/memory_game/face_down.png"

for i in range(8):
    card_images_url.append("http://hyunjunkim.com/images/memory_game/" + str(i) + ".png")
    card_images_done_url.append("http://hyunjunkim.com/images/memory_game/" + str(i) + "_done.png")

canvas_image_pos = [0, 90]

              
# helper function to initialize globals
def new_game():
    global card_images, card_images_done, card_face_image, state, card_exposed, card_done, selected_cards, card_exposed_track, turn
    card_images = []
    card_images_done = []
    for i in range(len(card_images_url)):
        # card_images consists of card images, its value & card object done images
        card_images.append([simplegui.load_image(card_images_url[i]), i, simplegui.load_image(card_images_done_url[i])])
        card_images.append([simplegui.load_image(card_images_url[i]), i, simplegui.load_image(card_images_done_url[i])])
     
    card_face_image = simplegui.load_image(card_face_url)
    card_exposed = [[False, False], [False, False], [False, False], [False, False],
                    [False, False], [False, False], [False, False], [False, False],
                    [False, False], [False, False], [False, False], [False, False],
                    [False, False], [False, False], [False, False], [False, False]]
    
    random.shuffle(card_images)
    
    state = 0
    selected_cards = []
    card_exposed_track = []
    turn = 0
    label.set_text("Turns = " + str(turn))

    
        
# define event handlers
def mouseclick(pos):
    global state, card_images, card_exposed, selected_cards, card_exposed_track, turn
    pos = pos[0] // 60
#    print
#    print "position:", pos
    
    if not card_exposed[pos][0]:
        card_exposed[pos][0] = True
        selected_cards.append(card_images[pos][1])
        card_exposed_track.append(pos)
#        print "card position tracking:", card_exposed_track
#        print "selected cards:", selected_cards

        # add game state logic
        if state == 0:
            state = 1            
            
        elif state == 1:
            state = 2
            turn += 1
            label.set_text("Turns = " + str(turn))
            
            #check and turn paired images
            if selected_cards[0] == selected_cards[1]:
                card_exposed[card_exposed_track[0]][1] = True
                card_exposed[card_exposed_track[1]][1] = True
            
        elif state == 2:
            state = 1
            if selected_cards[0] == selected_cards[1]:
                card_exposed[card_exposed_track[0]][0] = True
                card_exposed[card_exposed_track[1]][0] = True
                
            else:
                card_exposed[card_exposed_track[0]][0] = False
                card_exposed[card_exposed_track[1]][0] = False
            for i in range(2):
                card_exposed_track.pop(0)
                selected_cards.pop(0)

#            print "selected cards:", selected_cards
                   
#    print "state:", state
#    print "lenth of selected_cards:", len(selected_cards)
#    for i in range(len(selected_cards)):
#        print "selected_cards:" ,selected_cards[i]
#    print "length of card_exposed_track:", len(card_exposed_track)
    
    
                       
# cards are logically 60x90 pixels in size    
def draw(canvas):
    for card in range(len(card_images)):        
        offset = canvas_image_pos[0] + (card * 60)
        if card_exposed[card][0]:
            if card_exposed[card][1]:
                # draw paired image
                canvas.draw_image(card_images[card][2], [30, 45], [60, 90], [30 + offset, 45], [60, 90])
            else:
                canvas.draw_image(card_images[card][0], [30, 45], [60, 90], [30 + offset, 45], [60, 90])
        else:
            canvas.draw_image(card_face_image, [30, 45], [60, 90], [30 + offset, 45], [60, 90])


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 960, 90)
frame.set_canvas_background("White")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()