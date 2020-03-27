a = 32
b = 30
# if condition
if a > b:
    print("a is greater than b")

# elif condition and else
b = 32
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")  # fallback condition

# shorthand if and else
print("a") if a > b else print("=") if a == b else print("b")

# logical tester
a = 220
b = 562
if a == b or a < b:
    print("yap")
else:
    print("nopee")

if a == b and a < b:
    print("yap")
else:
    print("nopee")

# nested if and else
num = 20
if num > 5:
    print("the number is above 5")
    if num > 15:
        print("and also getter than 15")
    else:
        print("not greater than 25")

# if expression:
#     pass # use pass to avoid error
