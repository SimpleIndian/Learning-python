# Lists in python
theList = ["banana", "apple", "cherry", "tomato"]
# list using constructor
thelist = list(("banana", "apple", "cherry", "tomato"))

theList.append("orange")  # adding item to the list.
theList[0] = "kiwi"  # changing item to the list.
theList.insert(1, "banana")  # adding item to a specific index.
theList.remove("tomato")  # removing item from the list.
theList.pop(0)  # delet the specific index item.
# theList.clear()#empty the list
# del theList # delet the list

# looping through the eash item in the list
for x in theList:
    print(x)
# check if the is in list
if "apple" in theList:
    print("we got apple")
else:
    print("keep the cherry")

# get the lenth of the list
getLength = len(theList)

# copy a list
newList = theList.copy()
newList2 = list(theList)  # another way

# joining a list
numList = [1, 2, 3]
getJoinedlist = numList + theList
for x in theList:
    numList.append(x)  # another way

numList.extend(theList)  # another way
numList.count(3)  # this count how much we add one value
numList.reverse()  # reverse the list
theList.sort(reverse=False)  # sort it by a-z

print(theList)
