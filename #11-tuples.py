# Tuple is collection which is ordered and unchangeable

theTuple = ("apple", "apple", "orange", "banana", "kiwi", "lemon")

get1Tuple = theTuple[0]  # indexing value
getNegetiveTuple = theTuple[-1]  # negetive indexing
getRangeTuple = theTuple[2:4]  # range indexing
getNegetiveRangeTuple = theTuple[-4:-1]  # negetive range indexing
countApple = theTuple.count("apple")  # this will count the apple in tuple

# changing tuple value
# once declared tuple's value is Unchangeble but we can convert back and forth to list
mytuplelist = list(theTuple)  # converting to the list
mytuplelist.append("NewFruit")  # appending
mytuplelist[0] = 'mango'  # changing the value of 0 index
theTuple = tuple(mytuplelist)  # converting back to the tuple

# looping through the tuple

for x in theTuple:
    print(x)

if "apple" in theTuple:
    print('apple')

getTupleLength = len(theTuple)

# one item tuple
oneTuple = ("apple",)  # add coomma

# deleting tuple
# del theTuple

# joining tuple
newTuple = tuple((1, 2, 3))  # tuple using constructor
joinedTuple = theTuple + newTuple  # Adding tuple

print(joinedTuple)
