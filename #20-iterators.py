# Strings , list , tuples, dictionaries, sets, all are iterable object.
myList = ['apple',  'banana', 'cucumber']
mystr = 'Separator'
myiter = iter(myList)
myiter2 = iter(mystr)

print(next(myiter))  # print the first value of the list 'apple'
print(next(myiter2))  # print the first value of the string 'S'

# We can iterate through by a for loop
# this loop actually evalute the iterator object and execute the for loop iteself.
for x in myList:
    print(x)


# implement iteration in an class
class MyIterClass:
    def __iter__(self):  # implement iter method to the class
        self.a = 1  # 'a' is varriable to hold the value
        return self

    def __next__(self):  # implent next method to the class
        if self.a <= 20:
            x = self.a  # 'a' assign to 'x'
            self.a += 1  # increment 'a' and return 'x'
            return x
        else:
            # this will stop iterarion after 20 (if statement)
            raise StopIteration


myClass = MyIterClass()
MyNewIter = iter(myClass)
for x in MyNewIter:
    print(x)
