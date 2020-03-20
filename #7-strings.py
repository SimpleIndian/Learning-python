# string literal
# All string have to be in between double or single quotes.

a = 'Hello Python'  # Assigning string to a varriable.

# Assigning Multiline string to a Varriable.
multiLineString = """this is a demo multiline string
that create multiline string."""
# Like many other programming in python strings are the array of bytes representing unicode Character
# array start counting at '0'
b = a[0]  # access 1th element in an word
b = a[0:5]  # Array slicing , print character between 0 and 5
b = a[-6:-1]  # Negetive array slicing , print character from last 0 and -6
getLength = len(a)  # The 'len' Function return the length of an string

# String Methods
myDemoText = '  Hello, Python '
# strip Method removes the white space from start and end of the word
stripenText = myDemoText.strip()
lowerText = stripenText.lower()  # lower Method convert the text in lowercase
upperText = lowerText.upper()  # upper Method convert the text in uppercase
# replace the text in the destination
replacedText = upperText.replace("P", "G")
# Split method split string based on an separator like ','
splitedString = stripenText.split(",")

txt = "the main function is not a junction"
x = "tion" in txt  # return true if it has the following phrase
y = "pf" not in txt  # return true if it has not the following string
# string concatention
a = "hello"
b = "world"
c = a + " " + b

# string and number concatention
mygpa = 8.2
myYear = 1
mygpaText = "this is my {1}st year gpa - {0}"  # add {} too give a placeholder
# index adding is optional but good for sureity of positioning
# the format() function helps to add string to number and it takes unlimited parameter
total = mygpaText.format(mygpa, myYear)

# escape charactes , to use illegal characters in string
myEscapeCharacter = "the gravity's law is created by\n-\"newton\" "
print(myEscapeCharacter)
