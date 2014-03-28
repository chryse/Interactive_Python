
ne card game
import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def __cmp__(self, other):
        ## check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
            
        ## Aces are ranked higher than Kings
        if self.rank == 1 and other.rank == 13: return 1
        if self.rank == 13 and other.rank == 1: return -1
        
        ## suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
              
        ## ranks are the same... it's a tie           
        return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(i+1) + ". " + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
#        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True 
        else:
            return False

    def popCard(self):
        return self.cards.pop()

    def is_empty(self):
        return (len(self.cards) == 0)

    ## to deal card from the Deck into hands
    def deal(self, hands, num_cards=999):
        num_of_hands = len(hands)
        num_cards = num_of_hands * 7    ## 7장씩 사람수 만큼 분배를 위해
        for i in range(num_cards):
            if self.is_empty(): break   ## break if out of cards
            card = self.popCard()       ## take the top card
            hand = hands[i % num_of_hands] ## whose turn is next?
            hand.add(card)              ## add the card to the hand


class Hand(Deck):
    ## to initialize the attributes for the hand, which are name and cards
    def __init__(self, name=""):
        self.cards = []
        self.name = name
        
    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck.__str__(self)

    ## to add cards from the hand
    def add(self,card):
        self.cards.append(card)

## to create the deck and shuffling it        
class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


## subclass of CardGame with a new method called play that takes a list of players as a parameter
class OneCardGame(CardGame):
    def play(self, names):

        ## make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(Hand(name))
   
        ## deal the cards
        self.deck.deal(self.hands)
        print "---------- Cards have been dealt"
        self.printHands()
        ## Deck 의 제일 위카드
        print "==================================================="
        self.upper_card = self.deck.cards.pop()
        print "A upper Card of Deck is ** %s **" %(self.upper_card)
        print "==================================================="
        print "Start Game!!!\n"

        ## 사람수의 턴으로 돌아가면서 카드를 upper_card 와 매칭 시킨다.
        turn = 0
        numHands = len(self.hands)
        while 1:
            self.print_player_card(turn)
            if (self.play_One_Turn(turn)): break
            turn = (turn + 1) % numHands
   
        print "--------------------- Game is Over"
        self.printHands()


    ## to take a parameter that indicates whose turn it is
    ## The return value is the number of matches made during this turn
    def play_One_Turn(self, player):
        if self.hands[player].is_empty():
            print '\n####### ' + self.hands[player].name + ' wins! #######\n'
            return 1
        self.match_card(player)
        return 0

    def match_card(self, player):
        num = 0
        tmp = {}
        ## 매칭 되는 카드 검사
        print "a selectable card\n===================="
        for i in self.hands[player].cards:
            up_suit = self.upper_card.suits[self.upper_card.suit]
            play_suit = i.suits[i.suit]
            up_rank = self.upper_card.ranks[self.upper_card.rank]
            play_rank = i.ranks[i.rank]
            ## 모양과 숫자가 같은 카드를 보여 준다.
            if (up_suit == play_suit or up_rank == play_rank):
                print '[%s] %s' % (str(num+1), str(i))
                tmp[num] = i
                num = num +1
        print "===================="
        ## 버릴 수 있는 카드가 없다면 Deck에서 한장의 카드를 먹는다.
        if (num == 0):
            print 'No card to drop, you should take a card.'
            pickedcard = self.deck.cards.pop()
            self.hands[player].add(pickedcard)
        ## 랜덤함수로 카드를 선택해 버린다.
        else :
            tmp_key = tmp.keys()
            tmp_choice = random.choice(tmp_key)
            select_card = tmp[tmp_choice].ranks[tmp[tmp_choice].rank]
            self.hands[player].cards.remove(tmp[tmp_choice])
            self.deck.cards.append(self.upper_card)
            self.deck.shuffle()
            self.upper_card = tmp[tmp_choice]
            print self.hands[player].name, 'was dropped.', tmp[tmp_choice]
              
    ## to print cards from hands
    def printHands(self):
        for hand in self.hands:
            print hand
            
    ## 현재 player의 손에 있는 카드를 보여 준다.
    def print_player_card(self, player):
        player_card_num = 1
        print '\nA card on the top - ', self.upper_card
        print 'Cards of [%s]' % (str(self.hands[player].name))
        for hand in self.hands[player].cards:
            print '%s. %s' %(str(player_card_num), str(hand))
            player_card_num = player_card_num + 1


onecard = OneCardGame()
onecard.play(['Kim', 'Lee', 'Park', 'Choi'])

