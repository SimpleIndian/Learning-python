import os  # for delet
# this will methods will create the file if does not exits.
getNewFile = open('demo.txt', 'a')  # opening file in append mode(a).
# getNewFile = open('demo.txt', 'w')# opening file in write mode(w) (override every thing)
# getNewFile = open('demo.txt', 'x')# opening file in create(x) mode (override every thing)

# writing file
getNewFile.write('Adding new strings....')
getNewFile.close()  # you should always close the file after

getNewFile = open('demo.txt', 'r')  # open file in reading mode

# reading file
readFile = getNewFile.read()  # reding the first 5 character
print(readFile)

# closing file
getNewFile.close()

# deleting the file
if os.path.exists('demo.txt'):
    os.remove('demo.txt')  # this will delet the file
    print("file deleted")
else:
    print("file doesnot exits")
