# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import simplegui
import random

#global variables
width = 300
height = 300
position_user_title = [10, 50]
position_comp_title = [10, 150]
position_user = [30, 80]
position_comp = [30, 180]
position_result = [5, 250]

font_size = 30
user_font_color = "#FF0000"
comp_font_color = "#0000FF"
result_font_color = "#00FF00"
user_choice = ""
comp_choice = ""
result = ""



# helper functions   
def name_to_number(name):
    # convert name to number using if/elif/else
    if (name == "rock" or name == "Rock") :
        number = 0
    elif (name == "Spock" or name == "spock") :
        number = 1
    elif (name == "paper" or name == "Paper") :
        number = 2
    elif (name == "lizard" or name == "Lizard") :
        number = 3
    elif (name == "scissors" or name == "Scissors") :
        number = 4
    else :
        number = 5
        
    return number


def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0 :
        name = "rock"
    elif number == 1 :
        name = "Spock"
    elif number == 2 :
        name = "paper"
    elif number == 3 :
        name = "lizard"
    elif number == 4 :
        name = "scissors"
    return name
    

def rpsls(player_choice):
    global comp_choice
    
    print ""

    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    result_number = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if (player_number != 5) :
        
        if result_number == 1 or result_number == 2 :
            #print "Player wins!"
            return "Player wins!"
        elif result_number == 3 or result_number == 4 :
            #print "Computer wins!"
            return "Computer wins!"
        elif result_number == 0 :
            #print "Player and computer tie!"
            return "Player and computer tie!"
    else :
        #print "Please type a right choice!"
        return "Please type a right choice!"

# define event handlers
def rock():
    global user_choice, result
    user_choice = "rock"
    result = rpsls(user_choice)
    
def paper():
    global user_choice, result
    user_choice = "paper"
    result = rpsls(user_choice)
    
def scissors():
    global user_choice, result
    user_choice = "scissors"
    result = rpsls(user_choice)

def lizard():
    global user_choice, result
    user_choice = "lizard"
    result = rpsls(user_choice)

def spock():
    global user_choice, result
    user_choice = "Spock"
    result = rpsls(user_choice)
    
    
def draw(canvas):
    canvas.draw_text("User choice:", position_user_title, font_size, user_font_color)
    canvas.draw_text("Computer choice:", position_comp_title, font_size, comp_font_color)
    canvas.draw_text(user_choice, position_user, font_size, user_font_color)
    canvas.draw_text(comp_choice, position_comp, font_size, comp_font_color)
    canvas.draw_text(result, position_result, font_size, result_font_color)
    
        
        
# create a frame
frame = simplegui.create_frame("Rock-Paper-Scissors-Lizard-Spock", width, height)

frame.set_canvas_background("White")
frame.add_button("Rock", rock, 100)
frame.add_button("Paper", paper, 100)
frame.add_button("Scissors", scissors, 100)
frame.add_button("Lizard", lizard, 100)
frame.add_button("Spock", spock, 100)

# register handlers
frame.set_draw_handler(draw)

# start frame
frame.start()