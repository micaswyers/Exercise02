def add(a,b):
    #print "ADDING %d + %d" %(a, b)
    return a+b
"""
#Working on adding 3+ arguments
def add_many(*args):
    input = args
    tokens = input.split(" ")
    return tokens[1] + tokens(range(2, len(tokens)-1))
add_many("+", "2", "3")

"""

def subtract(a,b):
    #print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a,b):
    #print "MULTIPLYING %d * %d" % (a, b)
    return a*b

def divide(a,b):
    #print "DIVIDING %d / %d" % (a, b)
    return float(a) / float(b)

def square(a):
    #print "SQUARING %d" % a
    return a*a

def cube(a):
    #print "CUBING %d" % a
    return a*a*a

def power(a,b):
    #print "RAISING %d to the %d power" %(a,b)
    original_a = a
    for any_number in range(1, b):
        a = a * original_a
    return a

def mod(a,b):
    #print "RETURNING REMAINDER OF %d / %d" %(a,b)
    return a%b