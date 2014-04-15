# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
guess_num = 0
secret_num = 0
range_num = 100
remaining_guess = int(math.ceil(math.log(range_num, 2)))


# helper function to start and restart the game
def new_game():
    #reset global variables
    global guess_num, secret_num, range_num, remaining_guess
    
    guess_num = 0
    secret_num = random.randint(0, range_num)
    remaining_guess_for_range = int(math.ceil(math.log(range_num, 2)))
    remaining_guess = remaining_guess_for_range

    print "------------------------------"
    print "---------- NEW GAME ----------"
    print "Range is from 0 to", range_num
    print "Number of remaining guess is", remaining_guess
    print ""
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global range_num
    global remaining_guess
    
    range_num = 100
    remaining_guess = int(math.ceil(math.log(range_num, 2)))
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global range_num, remaining_guess
    
    range_num = 1000
    remaining_guess = int(math.ceil(math.log(range_num, 2)))
    new_game()
 
    
def input_guess(guess):
    # main game logic goes here    
    global guess_num, secret_num, range_num, remaining_guess
    
    # change input number into integer num
    guess_num = int(guess)
    
    if (guess_num >= 0) and (guess_num <= range_num):
        remaining_guess -= 1
        print "Guess was ", guess_num
        print "Number of remaining guess is ", remaining_guess
        
        if remaining_guess > 0:
            if guess_num > secret_num:
                print "\"LOWER\""
                print ""
            elif guess_num < secret_num:
                print "\"HIGHER\""
                print ""
            else:
                print "\"CORRECT\""
                print ""
                new_game()
        elif (remaining_guess == 0) and (secret_num == guess_num):
            print "\"Correct\""
            print ""
            new_game()
        else:
            print ""
            print "Game is over."
            print "The secret number is " + str(secret_num) + "."
            print ""
            new_game()
    else:
        print "A number you typed is out of the range."
        print "Please try again."
        print ""
        
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Guess the number", input_guess, 150)


# call new_game and start frame
frame.start()
new_game()
