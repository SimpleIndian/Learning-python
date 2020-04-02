#Inheritance in python

# Parent Class is being inherited from a Base class(python Documentation)


class ParentClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        print("My Name is " + self.fname + " " + self.lname)


# object created from Parent class
myParent = ParentClass('Sukumar', 'Mandal')

# Child class inherited from Parent class pass parent class as a parameter


class Child(ParentClass):
    # when we use init we override the parent value
    def __init__(self, fname, lname, year, sub):
        # to keep the class to inherit from parent class add a call to super method
        super().__init__(fname, lname)
        self.GYear = year
        self.subject = sub

    def comeMessage(self):
        print("your grd year is", self.GYear)


iamChild = Child("jhon", 'doe', 2019, 'Biology')
iamChild.comeMessage()
