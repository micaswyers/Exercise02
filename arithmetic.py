def add(tokens):
    #print "ADDING %d + %d" %(a, b)
    sum = 0
    for i in range(len(tokens)):
        sum += tokens[i]
    return sum

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