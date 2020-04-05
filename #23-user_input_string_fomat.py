# use input function to get user input
# userName = input("Tell me your Name : ")
try:
    x = "Your name is " + userName
except NameError:
    print('name error')

# String formatting
# use 'format()' function to format
price = input('what is the current dollar price in rupees : ')
item = 1
country = 'india'

# add {} for placeholder and add index for correct placeholder
getPrice = 'Current Dollar price for {0} item is {1} in {2}'

readable = getPrice.format(item, price, country)  # use format with parameter

print(readable)

# create a fake server class
class Server:
    def __init__(self, fname, age):
        self.fname = 'souvik'
        self.age = 23


AwsLamdaServer = Server('jhon', 23)

getText = 'My Name is {username} and my age is {age}'

formatText = getText.format(username=AwsLamdaServer.fname, age=AwsLamdaServer.age) # get dynamic data from server class

print(formatText)
