# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

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
    # print a blank line to separate consecutive games
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
            print "Player wins!"
        elif result_number == 3 or result_number == 4 :
            print "Computer wins!"
        elif result_number == 0 :
            print "Player and computer tie!"
    else :
        print "Please type a right choice!"

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

rpsls("roook")

# always remember to check your completed program against the grading rubric


