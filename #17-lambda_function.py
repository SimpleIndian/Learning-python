# A Lamda is a small anonymous function
# It can have any number of arguments but only have a one expression
#   decl arg : exp
a = lambda x : print(x + 5) # Lambda function that add 5 to the number

b = lambda x, y: print(x + y) #this function add two arguments

def u_lambda(n):
    return lambda x : x * n

mydoubler = u_lambda(2) # this parameter will be a pass as a lambda function parameter (x)

print(mydoubler(12)) # this parameter will be passed as a 'n' 