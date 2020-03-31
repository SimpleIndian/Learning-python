#function in python
# function always defined with 'def' keyword


def myFunction():
    print("hello World from python")


myFunction()
# with arguments
# you have to pass all the parameter that defines not more or less than that

# with default parameter


def My_arg_function(fname='john'):
    print(fname + '@gmail.com')


# the arguments will be pass as a paramter to  the function calling
My_arg_function("open269")

# Aribitary arguments
# when you don't know the parameter count will be passed
# if the value is less than than the


def myariFun(*kids):
    print("the Young kids is " + kids[1])


myariFun("jhon", "mosh", "beauty")

# keyword arguments


def Keyword_args(child1, child2):
    print("the youngest child " + child2)


Keyword_args(child1="jhon", child2="moshi")

# Aribitary arg


def ar_Keyword_args(**kid):
    print("your last name " + kid["lname"])


ar_Keyword_args(fname='jhon', lname='doe')


def list_func(food):  # passing list as a param
    for x in food:
        print(x)


list_func(['jam', 'bread', 'rice'])

# returning value


def addition(fnum, lnum):
    return fnum + lnum


print(addition(2, 6))


# Recursion
# recursion is a popular thing that can used as a back self calling function
# so we have to first call the factotial of 5 so we have to know the factorial of 4 and thing chain is going till 0
def fact(k):
    if k == 0:
        return 1
    return k * fact(k-1)

print(fact(5))
