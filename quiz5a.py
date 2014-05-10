numbers = [23, 234, 341, 345, 345, 2342, 21, 1, 3]
product = 1
for n in numbers:
    product *= n
    
print product

def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
        print result
    return result

print reverse_string("hello")

import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        #points.append(point)
        points += point
    return points

players = ["player1", "player2", "player3"]
print starting_points(players)


def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers)-1):
        if numbers[i+1] < numbers[i]:
            return False
    return True

print is_ascending([1,2,5,4,5])


'''
1. Create a list with two numbers, 0 and 1, respectively.
2. For 40 times, add to the end of the list the sum of the last two numbers.
'''
def fibonacci(times):
    fib_list = [0, 1]
    for i in range(times):
        sum = fib_list[len(fib_list)-2] + fib_list[len(fib_list)-1]
        fib_list.append(sum) 
    print fib_list
    return fib_list[len(fib_list)-1]

print fibonacci(40)


x = 0
y = 1
for i in range(40):
    x, y = y, x + y
print y

my_list = [1, 2]
print my_list + [10, 20] # this is immutable.
print my_list
