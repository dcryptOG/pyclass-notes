
# NOTES FOR MODULES AND PACKAGES
#! 1. MODULES and PACKAGES
# TODO ALL NOTES HERE 1. ORGANIZE 2. DO ACTIVITES
# Here is the best source the official docs! https://docs.python.org/3/tutorial/modules.html#packages

# But I really like the info here: https://python4astronomers.github.io/installation/packages.html

# Here's some extra info to help:

# *MODULES = Python files with the .PY EXTENSION, which implement a SET of FUNCTIONS IMPORTED from a SET of OTHER modules.

# IMPORT = command to import a module (from other modules/packages)

# ? The FIRST time a module is loaded into a running Python script
# It is initialized by EXECUTING the CODE in the MODULE ONCE.

# MODULES can ONLY be loaded ONCE

#  LOCAL VARAIBLES inside the MODULE act as a "SINGLETON" - they are initialized only ONCE.

# If we want to import the math module, we simply import the name of the module:

# # import the library
# * import math

# use it (ceiling rounding)
# * math.ceil(2.4)
# ?ouput: 3

#! 2. Check out the full list of BUILT-IN MODULES in the Python standard library here.

# https://docs.python.org/3/py-modindex.html


# Exploring built-in modules

# ?EXPLORING MODULES - TWO important FUNCTIONS

# * 1.  dir() = look for which functions are implemented in each module

# * 2 help() = find info on function

# EX dir()

# ? print(dir(math))

# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# When we find the function in the module we want to use,
# Using the help function, inside the Python interpreter:

# EX help()

# ? help(math.ceil)

# *OUTPUT
# *  Help on built-in function ceil in module math:
# * ceil(...)
# *     ceil(x)
# *     Return the ceiling of x as an Integral.
# *     This is the smallest integer >= x.


#!3.  Writing MODULES

# Writing Python modules is very simple.
# To create a module of your own,
# ?1. Create a new .py file with the module name
# ? 2. Import it using the Python file name
# (without the .py extension)using the import command.

# . Writing a module is just like writing any other Python file.

# ? EX for EXAMPLE FILES file1.py

# def myfunc(x):
#     return [num for num in range(x) if num%2==0]
# list1 = myfunc(11)

# file1.py is going to be used as a module.

#  it just defines a function called myfunc and a variable called list1.

#! 4. Writing PACKAGES

# * PACKAGES = NAME-SPACES which contain MULTIPLE PACKAGES, MODULES and must have a __init__.py
# Directories, but with a twist.

# Each PACKAGE in Python is a directory which MUST contain a special file:
# * __init__.py.

#  Indicates that the DIRECTORY it contains is a Python PACKAGE
# Can be IMPORTED the SAME WAY as a MODULE
# __init__.py can be empty


# If we create a directory called foo, which marks the package name,
# we can then create a module inside that package called bar.
# We also must not forget to add the __init__.py file inside the foo directory.

# To use the module bar, we can import it in two ways:

# # Just an example, this won't work
# import foo.bar


# # OR could do it this way
# from foo import bar

# In the first method, we must use the foo prefix whenever we access the module bar.
# In the second method, we don't, because we import the module to our module's name-space.

# The __init__.py file can decide which modules the package exports as the API, while keeping other modules internal, by overriding the __all__ variable, like so:

# __init__.py:

# __all__ = ["bar"]


#!5 Writing SCRIPTS


# writefile file2.py
# import file1
# file1.list1.append(12)
# print(file1.list1)

# Writing file2.py

# file2.py is a Python script.

# First, we import our file1 module (note the lack of a .py extension)
# Next, we access the list1 variable inside file1, and perform a list method on it.
# .append(12) proves we're working with a Python list object, and not just a string.
# Finally, we tell our script to print the modified list.
# Running scripts

#!6. Running SCRIPTS

# * ! python file2.py

# [0, 2, 4, 6, 8, 10, 12]

# Here we run our script from the command line.
#  The exclamation point is a Jupyter trick that lets you run command line statements from inside a jupyter cell.

# import file1
# print(file1.list1)

# [0, 2, 4, 6, 8, 10]

# The above cell proves that we never altered file1.py, we just appended a number to the list after it was brought into file2.

#!7. Passing command line arguments

# *sys = MODULE Gives you access to command line arguments when calling scripts.

# file3.py
# import sys
# import file1
# num = int(sys.argv[1])
# print(file1.myfunc(num))

# Writing file3.py

# Note that we selected the second item in the list of arguments with sys.argv[1].
# This is because the list created with sys.argv always starts with the name of the file being used.
# ? ! IS ACTUAL COMMAND
# * ! python file3.py 21

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Here we're passing 21 to be the upper range value used by the myfunc function in list1.py
