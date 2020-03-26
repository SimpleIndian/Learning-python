# Dictionay is a collection which is unordered and changeable an indexed
theDict = {
    "brand": "Ford",
    "price": 1000000,
    "model": "pigeon"
}
theDict = dict(brand="Ford",  # using constructor
               price=1000000,
               model="pigeon")

# accessing item
getItem = theDict['price']
# or
getItem = theDict.get('model')
# adding item
theDict['color'] = 'red'
# changing value
theDict['price'] = 3000
# removing item
theDict.pop('model')
theDict.popitem()  # remove last item
del theDict['brand']
# theDict.clear() #empty the dict

# looping through a dict
for x in theDict:  # print the key
    print(x)

for x in theDict.values():  # print the values
    print(x)

# print both key and value
for x, y in theDict.items():
    print(x, y)

if 'model' in theDict:
    print('yap')

getLength = len(theDict)  # get the length

# copying a dictionary
newDict = theDict.copy()
# or
newDict = dict(theDict)

nestedDict = {
    "child1": {
        "name": "jhon",
        "age": 15
    },
    "child2": {
        "name": "mosh",
        "age": 22
    },
    "child3": {
        "name": "",
        "age": 18
    }
}

# or

child1 = {
    "name": "jhon",
    "age": 15
}
child2 = {
    "name": "mosh",
    "age": 22
}
child3 = {
    "name": "",
    "age": 18
}

myNewFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myNewFamily)
