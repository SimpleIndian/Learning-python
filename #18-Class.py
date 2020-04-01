# Everything in python is a object


class MyFirstClass:  # simple class created
    x = 5


c = MyFirstClass()  # creating object with class

# self keyword is used to access the varriable in class it have to be the first parameter in the object method
# we can name this self function as we want like - 'mCons
# Basically it refers to the class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myPee(self):  # object Method
        print("hello this is my name " + self.name)


p1 = Person('Jhon', 32)
# Modifying value
p1.age = 40
# deleting items from object
del p1.age

# use pass to avoid error


class NewDummy:
    pass

# Cars Object
class Cars:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def horseP(self):
        return print("Horse Power of this car is", self.price * 5)

# add as much cars as you want
getCar = Cars('Toyota', 'black', 555999)

print(getCar.horseP())
