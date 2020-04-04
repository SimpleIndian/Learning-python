# import mymodule  # Importing a module
import mymodule as mx  # same as above importation
# importing a part of a module
from mymodule import person1  # this will import person1(dict)
import setuptools
# built-in modules
import platform

# Use the module
# Syntax : module_Name . function_name
mx.getName("Roshni")

# access the dictionaries in the module
# when using 'from' keyword to import a separate var, omit the module name
a = person1['name']
print(a)

# using built in modules
y = platform.system()  # return the system name

x = dir(mx)  # list all function and varriable name(aplicable in all module)

