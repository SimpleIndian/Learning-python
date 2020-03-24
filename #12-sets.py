# sets is a unordered and unindexed collection
thesets = {"apple", "banana", "orange"}
theNum = set((1, 2, 3))

thesets.add('kiwi')  # add single item
thesets.update(["mango", "choco"])  # add multiple item
getLength = len(thesets)  # get length of the sets
thesets.discard('banana')  # use this instead of remove for sets
# thesets.clear()  # this will clear the sets
joinedSets = thesets.union(theNum)  # use uninon mehtod for set joining
theNum.update(thesets)  # add using update Method

#del thesets
# looping through the sets
for x in thesets:
    print(x)
# check if a item is in list
if 'banana' in thesets:
    print("yap")

print(theNum)
