import random    # add random module to get random number                       
                            
                              # There are Three type of number in Python
# int
x = 56 # a whole number without limit can be positive or negetive
x1 = -55676454
x2 = 35834357545345617531453

# float 
y = 5.8 # can be positive or negetive or can be Exponent and negetive Exponent
y1 = - 6.656
y2 = 52e5
y3 = -5E7


# complex number denoted by j
z = 5j

    # type conversion
a = float(x) # this will convert x to a float number
b = int(y) # this will convert y to a integer number
c = complex(x) # this will convert x to a complex number
# ! you cannot convert complex numbers into any other format !

randomNumGenerator = random.randrange(1,10) # this will generate random number by adding 'start' and 'stop' parameter

print(randomNumGenerator)