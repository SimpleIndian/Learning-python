# looping in python
# while loop
i = 1
while i <= 10:
    print(i)
    if i == 3:  # when the i's value is equal to 3 break the loop
        break
    i += 1
# this code describes when i value is 10 close the loop else continue and increment the value

j = 0
while j <= 10:
    j += 1
    if j == 3:  # when the i's value is equal to 3 then continue the loop
        continue
    print(j)

 # with else:
k = 0
while k <= 10:
    print(k)
    k += 1
else:
    print("we can't go beyond 10")

# for loops with if else
myTuple = tuple(("a", "b", "c"))
for x in myTuple:
    if x == 'b':
        break
    else:
        print(x)

for y in 'Nunito':  # string is itable
    print(y)

# with continue
for z in myTuple:
    if z == 'b':
        continue
    else:
        print(z)
# using range with start end and gap parameter
for r in range(2, 10, 2):
    print(r)
else:
    print("finally finished")

# nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for a in adj:
    for b in fruits:
        print(a,b)
