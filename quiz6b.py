def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result
#print list_extend_many([[1,2], [3], [4, 5, 6], [7]])


def list_extend_many1(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result
#print list_extend_many1([[1,2], [3], [4, 5, 6], [7]])

def list_extend_many2(lists):
    result = []
    for i in range(len(lists) - 1, -1, -1):
        result.extend(lists[i])
    return result
#print list_extend_many2([[1,2], [3], [4, 5, 6], [7]])

def list_extend_many3(lists):
    result = []
    i = 0
    while i < len(lists): 
        result += lists[i]
        i += 1
    return result
#print list_extend_many3([[1,2], [3], [4, 5, 6], [7]])

'''
def list_extend_many4(lists):
    result = []
    i = 0
    while i <= len(lists): 
        result.extend(lists[i])
        i += 1
    return result
print list_extend_many4([[1,2], [3], [4, 5, 6], [7]])
'''

n = 1000
numbers = range(2, n)
result = []
i = 0
while 0 < len(numbers):
    result.insert(len(result), numbers[0])
    for n in numbers:
        if n % result[len(result)-1] == 0:
            numbers.remove(n)
#print result
print len(result)

number = range(2, n)
results = []
while number != []:
    results.append(number[0])
    number = [n for n in number if n % number[0] != 0]

print len(results)


def slow_wumpus(year):
    slow_wumpuses = 1000   
    while year > 1: 
        slow_wumpuses = slow_wumpuses * 2 * 0.6
        year -= 1 
    return slow_wumpuses

def fast_wumpus(year):
    fast_wumpuses = 1
    while year > 1:
        fast_wumpuses = fast_wumpuses * 2 * 0.7
        year -= 1
    return fast_wumpuses

print slow_wumpus(2)
print fast_wumpus(2)
print slow_wumpus(3)
print fast_wumpus(3)


n = 1
while True:
    if slow_wumpus(n) < fast_wumpus(n):
        print n
        break
    n += 1

print slow_wumpus(45)
print fast_wumpus(45)
print slow_wumpus(46)
print fast_wumpus(46)
     

    
         
