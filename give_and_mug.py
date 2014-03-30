import random

def giveMug(friend, money):
    if friend and money > 20 :
        print "Hi! Here is $20."
        money = money - 20
    elif friend :
        print "Hello, I don't have enough money."
    else :
        print "Ha ha, I'll take your money."
        money = money + 20
    return money

def checkFriend():
    friend = random.randrange(1, 3)
    if friend == 1 :
        print "You are my friend."
        return True
    else :
        print "You are not my friend."
        return False

money = 15

print "Current money: $%s\n" % money


money = giveMug(checkFriend(), money)
print "Current money: $%s\n" % money

money = giveMug(checkFriend(), money)
print "Current money: $%s\n" % money

money = giveMug(checkFriend(), money)
print "Current money: $%s\n" % money


        