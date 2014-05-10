# Mini-project #6 - Blackjack

import simplegui
import random

WIDTH = 600
HEIGHT = 600
OUTCOME_POS = [WIDTH / 12, HEIGHT / 2]
DEALER_FONT_POS = [WIDTH / 12, HEIGHT / 5]
PLAYER_FONT_POS = [WIDTH / 12, HEIGHT * 3/5]
DEALER_FONT = "DEALER:"
PLAYER_FONT = "PLAYER:"
OUTCOME_FONT_SIZE = DEALER_FONT_SIZE = PLAYER_FONT_SIZE = 20
OUTCOME_FONT_COLOR = "15CDE3"
DEALER_FONT_COLOR = PLAYER_FONT_COLOR = "#FFFFFF"
OUTCOME_FONT_FACE = DEALER_FONT_FACE = PLAYER_FONT_FACE = "monospace"
MONEY_POS = [WIDTH * 7/9, HEIGHT * 1/7]
BET_POS = [WIDTH * 7/9 + 14, HEIGHT * 1/7 + 30]
MONEY_FONT_SIZE = BET_FONT_SIZE = 18
MONEY_FONT_COLOR = BET_FONT_COLOR = "#CCD71A"
MONEY_FONT_FACE = BET_FONT_FACE = "sans-serif"

CARD_OFFSET = WIDTH / 12


# load card sprite - 949x392
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://www.hyunjunkim.com/images/blackjack/cards.png")

CARD_BACK_SIZE = (73, 98)
CARD_BACK_CENTER = (36.5, 49)
card_back = simplegui.load_image("http://www.hyunjunkim.com/images/blackjack/card_back.png")    

# define globals for cards
SUITS = ("Club", "Spade", "Heart", "Diamond")
RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
VALUES = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

# initialize some useful global variables
in_play = False
is_bet = False
outcome = ""
player_value = ""
dealer_value = ""
money = 300
bet_amount = 10



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hold_cards = []

    def __str__(self):
        # return a string representation of a hand
        s = ""
        if len(self.hold_cards) == 0 :
            s = "No card holds."
        else:
           for i in range(len(self.hold_cards)):
                    s = s + str(self.hold_cards[i]) + "/ "
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.hold_cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hasAce = False
        self.hand_value = 0
        
        # check Ace is contained
        for card in self.hold_cards:
            if card.rank == "Ace":
                hasAce = True
            self.hand_value += VALUES[card.rank]
      
        if hasAce:
            if (self.hand_value + 10) <= 21:
                self.hand_value += 10
        
        return self.hand_value                    
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_cards.append(Card(suit, rank))        

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck_cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck_cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        s = ""
        for i in range(len(self.deck_cards)):
             s = s + (" " * i) + str(self.deck_cards[i]) + "\n"
        return s


#define event handlers for buttons
def deal():
    global outcome, in_play, is_bet, money, game, player_hand, dealer_hand, player_value, dealer_value, bet_amount
    if money > 0:
        is_bet = False
        player_hand = Hand()
        dealer_hand = Hand()
        game = Deck()
        game.shuffle()
        for i in range(2):
            player_hand.add_card(game.deal_card())
            dealer_hand.add_card(game.deal_card())
#            print "Dealer: " + str(dealer_hand)
#            print "Player: " + str(player_hand)
        
        if in_play:
            outcome = "You lost your bet money $" + str(bet_amount) + "."
            money -= bet_amount
            player_value = str(player_hand.get_value())
        else :          
            in_play = True
            outcome = "Hit or stand?"
            player_value = str(player_hand.get_value())
            dealer_value = ""
            bet_amount = 10
            bet_input.set_text("$" + str(bet_amount))
    

def hit():
    global outcome, in_play, is_bet, money, player_value
    # if the hand is in play, hit the player
    is_bet = True
    if in_play:
        player_hand.add_card(game.deal_card())
        #print player_hand
        #print player_hand.get_value()
        player_value = str(player_hand.get_value())
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
           # print "You have busted. New deal?"
            outcome = "You have busted. You lost $" + str(bet_amount) + ". New deal?"
            money -= bet_amount
            in_play = False
   
       
def stand():
    global outcome, in_play, is_bet, money, dealer_value
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    is_bet = True
    dealer_win = False
    if in_play:
#        print "Press stand", in_play
        if dealer_hand.get_value() == player_hand.get_value():
            #print "Tied. Dealer won. New deal?"
            outcome = "Tied. You lost $" + str(bet_amount) + ". New deal?"
            dealer_value = str(dealer_hand.get_value())
            in_play = False
            dealer_win = True
        elif dealer_hand.get_value() > player_hand.get_value():
            #print "Dealer won. New deal?"
            outcome = "You lost $" + str(bet_amount) + ". New deal?"
            dealer_value = str(dealer_hand.get_value())            
            in_play = False
            dealer_win = True
        else:
            while dealer_hand.get_value() <= 17:
                dealer_hand.add_card(game.deal_card())
                #print "dealer value:", dealer_hand.get_value(), dealer_hand
                if dealer_hand.get_value() < player_hand.get_value():
                    continue
                    
                if dealer_hand.get_value() == player_hand.get_value():
                    #print "Tied. Dealer won. New deal?"
                    outcome = "Tied. You lost $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = True
                    break
                elif dealer_hand.get_value() == 21:
                    #print "Dealer won. New deal?"
                    outcome = "You lost $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = True
                    break
                elif dealer_hand.get_value() > 21:
                    #print "Dealer has busted. You won. New deal?"
                    outcome = "Dealer has busted. You gained $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = False
                    break
                else:
                    if dealer_hand.get_value() < player_hand.get_value():
                        #print "You won. New deal?"
                        outcome = "You won. You gained $" + str(bet_amount) + ". New deal?"
                        dealer_value = str(dealer_hand.get_value())
                        dealer_win = False
                        break
                    else:
                        #print "Dealer won. New deal?"
                        outcome = "You lost $" + str(bet_amount) + ". New deal?"
                        dealer_value = str(dealer_hand.get_value())
                        dealer_win = True
                        break
                           
            if dealer_hand.get_value() > 17 and dealer_hand.get_value() <= 21:
                if dealer_hand.get_value() > player_hand.get_value():
                    #print "Dealer won. New deal?"
                    outcome = "You lost $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = True
                elif dealer_hand.get_value() == player_hand.get_value():
                    #print "Tied. Dealer won. New deal?"
                    outcome = "Tied. You lost $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = True
                else:
                    #print "You won. New deal?"
                    outcome = "You won. You gained $" + str(bet_amount) + ". New deal?"
                    dealer_value = str(dealer_hand.get_value())
                    dealer_win = False

        # count bet amount
        if dealer_win: money -= bet_amount
        else: money += bet_amount
                
        in_play = False

# new game
def new():
    global outcome, in_play, is_bet, money, game, player_hand, dealer_hand, player_value, dealer_value, bet_amount    
    player_hand = Hand()
    dealer_hand = Hand()
    game = Deck()
    game.shuffle()
    for i in range(2):
        player_hand.add_card(game.deal_card())
        dealer_hand.add_card(game.deal_card())           
        
    in_play = True
    is_bet = False
    outcome = "Hit or stand?"
    player_value = str(player_hand.get_value())
    dealer_value = ""
    bet_input.set_text("$10")
    bet_amount = 10
    money = 300
            
# bet amount input handler            
def bet_input(bet):
    global bet_amount, outcome, is_bet
    if is_bet:
        outcome = "You can't change bet amount at this time."
    else:
        if bet.strip("$").isdigit():
            temp = bet.strip("$")
            if int(temp) < money and int(temp) > 0:
                bet_amount = int(temp)
                outcome = "You bet " + "$" + str(bet_amount) + "."
                is_bet = True
            elif int(temp) == money:
                bet_amount = int(temp)
                outcome = "You bet all-in " + "$" + str(bet_amount) + "."
                is_bet = True
            elif int(temp) == 0:
                outcome = "You can't bet $0. Please try again."
            else:
                outcome = "You can't bet over your money " + "$" + str(money) + "."
        else:
            #print "Please bet correctly."
            outcome = "Please bet correctly."
        
    bet_input.set_text("$")   
        
# draw handler    
def draw(canvas):
    global outcome
    # test to make sure that card.draw works, replace with your code below
    
    # draw dealer's cards
    if money >= 0:
        if in_play:
            for i in range(len(dealer_hand.hold_cards)-1):
                dealer_hand.hold_cards[i].draw(canvas, [CARD_OFFSET * (i+1), DEALER_FONT_POS[1]+10])
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_OFFSET * 2 + CARD_BACK_CENTER[0], DEALER_FONT_POS[1]+10 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        else:
            for i in range(len(dealer_hand.hold_cards)):
                dealer_hand.hold_cards[i].draw(canvas, [CARD_OFFSET * (i+1), DEALER_FONT_POS[1]+10])
        
        # draw player's cards    
        for i in range(len(player_hand.hold_cards)):
            player_hand.hold_cards[i].draw(canvas, [CARD_OFFSET * (i+1), PLAYER_FONT_POS[1]+10])
            
        canvas.draw_text(DEALER_FONT, DEALER_FONT_POS, DEALER_FONT_SIZE, DEALER_FONT_COLOR, DEALER_FONT_FACE)
        canvas.draw_text(PLAYER_FONT, PLAYER_FONT_POS, PLAYER_FONT_SIZE, PLAYER_FONT_COLOR, PLAYER_FONT_FACE)    
        canvas.draw_text(player_value, [PLAYER_FONT_POS[0] + 100, PLAYER_FONT_POS[1]], PLAYER_FONT_SIZE, PLAYER_FONT_COLOR, PLAYER_FONT_FACE)
        canvas.draw_text(dealer_value, [DEALER_FONT_POS[0] + 100, DEALER_FONT_POS[1]], DEALER_FONT_SIZE, DEALER_FONT_COLOR, DEALER_FONT_FACE)                
    
    
    # draw output interface 
    canvas.draw_text("Blackjack", [10, 40], 40, "#000000", "sans-serif")
    canvas.draw_text(outcome, OUTCOME_POS, OUTCOME_FONT_SIZE, OUTCOME_FONT_COLOR, OUTCOME_FONT_FACE)
    
    if money >= 0:
        canvas.draw_text("Total: " + "$" + str(money), MONEY_POS, MONEY_FONT_SIZE, MONEY_FONT_COLOR, MONEY_FONT_FACE)
    else:
        canvas.draw_text("Total: " + "-$" + str(money).strip("-"), MONEY_POS, MONEY_FONT_SIZE, MONEY_FONT_COLOR, MONEY_FONT_FACE)
    
    canvas.draw_text("Bet: " + "$" + str(bet_amount), BET_POS, BET_FONT_SIZE, BET_FONT_COLOR, BET_FONT_FACE)
    
    if money <= 0:
        outcome = "You went bankrupt. Please start over."


# initialization frame
frame = simplegui.create_frame("Blackjack", WIDTH, HEIGHT)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
bet_input = frame.add_input("Bet amount", bet_input, 100)
bet_input.set_text("$10")
frame.add_button("Start over", new, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

