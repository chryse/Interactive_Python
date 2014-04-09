# Question 2
p = True
q = True
print not (p or not q)

p = True
q = False
print not (p or not q)

p = False
q = True
print not (p or not q)

p = False
q = False
print not (p or not q)

# Question 3
n = 123
#print (n % 10) / 10
#print (n % 100 - n % 10) / 10
#print (n // 10) % 10

# Question 4
import random
#print random.randint(0, 10)
#print random.randrange(0, 10)

# Question 5 f(x) = -5 x5 + 69 x2 - 47
def fx(x):
    return -5 * x**5 + 69 * x**2 - 47

print fx(0), fx(1), fx(2), fx(3)

# Question 6 FV = PV (1+rate)periods
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * (1 + rate_per_period) ** periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print "$500 at 4% compounded daily for 10 years yields $", future_value(500, .04, 10, 10)

# Question 7  the area of a regular polygon. 
# Given the number of sides, n, and the length of each side, s, the polygon's area is 
# 1/4 n s2 / tan( pi/n)

def area_polygon(num_sides, length_side):
    import math
    return 1.0 / 4 * num_sides * length_side **2 / math.tan(math.pi / num_sides)

print area_polygon(5, 7)  
print area_polygon(7, 3)

# Question 8 incorrect indentation
a, b, c = 1, 2, 3
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

#print max_of_3(a,b,c)

# Question 9 
def project_to_distance(point_x, point_y, distance):
    import math
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)