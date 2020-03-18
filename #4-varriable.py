     #Varriable Declaration
#define String
char_name = 'Souvik'

#define Integer
char_age = 17

#define float / decimal
char_gpa= 7.1

#define Boolean
isMale =  True 
 
                              # Concatation of strings and number
# String Concatention
name  = "Souvik ."
goodName =" Souvik Mandal"
total =  name + goodName # + will work here as a concatation 
print("My name is "+ total + " is my good name")

 #Number Concatention
a = 25
b = 25 
c = a+b # + will work here as a mathematical operation
print(c)

x = "awesome" #this is global varriable (accesbiole to everyone)
def myFunction():
   global x  #this Global keyword makes it accesiable to everyone
   x = "fantasic" # this is a local varriable (only accesbiole to this function)
   print("python is " + x)

myFunction()
print("python is " +x)