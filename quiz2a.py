# Question 5
def d(y):
    y = x + y
    return y
def b(x,y):
    x = x + y
    return x
def a(y):
    global x
    x = x + y
    return y
def c(y):
    return x + y

# Question 6 
count = 0

def square(x):
    global count
    count += 1
    return x**2

#print square(square(square(square(3))))
#print count

# Question 7
a = 3
b = 6

def f(a):
    c = a + b
    return c
print f(a)

def f(a, b, c):
    return b and c or a
#    return (a or b) and c
#    return a or (b and c)
#    return a or b and not c
#    return a or b and c

print f(True, True, True)
print f(True, True, False)
print f(True, False, True)
print f(True, False, False)
print f(False, True, True)
print f(False, True, False)
print f(False, False, True)
print f(False, False, False) 