try:  # use try block to test a code
    print('x')
except NameError:  # add a special exception
    print('name error accured')
except:  # use except block to handle if error happens
    print("an exception ocuured")
else:  # use if there is no exception
    print("nothing went wrong")

try:
    print(x)
except NameError:
    print("this is a name error")
else:
    print('nothing went wrong')
finally:  # finally executed regardless of try and except
    print('code block closed')

# raise an error
a = -1
if a < 0:
    raise Exception('Number under 0 are not allowed')
