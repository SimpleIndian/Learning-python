x = 31
y = 3

# Addition Operators
z = x + y
# Subtraction Operators
z = x - y
# Multiplication Operators
z = x * y
# Division Operators
z = x / y

# Modulus Operators
z = x % y
# Exponent / Power Operators
z = x ** y
# Floor division Operators , round the float number
z = x // y


# comparisons operators
z = x == y
z = x != y
z = x > y
z = x < y
z = x >= y
z = x <= y

# logical operators

z = x < 5 or x == 31  # logical OR
z = x < 5 and x == 31  # logical AND
z = not(x < 5 and x == 31)  # logical NOT

# assignment Operators
x = 32
x += 3
x -= 3
x *= 3
x //= 3
x **= 3
x &= 3
x %= 3

# identity operators

b = ["apple", "banana"]
a = ["apple", "banana"]
c = b

d = a is not c  # return true if it not the s
d = a is b  # return false because it not the same object also content is same

d = "banana" in c  # returns true if it has the item
d = "cherry" not in c  # returns true if it has not the item
