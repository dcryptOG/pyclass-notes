
# Methods
# ?
# *
# TODO
# !asdf


# Methods are essentially functions built into objects.
# Later create our own objects and methods using Object Oriented Programming (OOP) and classes.

# Methods perform specific actions on an object and can also take arguments,

# Methods are in the form:

# object.method(arg1,arg2,etc...)

# You'll later see that we can think of methods as having an argument 'self' referring to the object itself.

# # Create a simple list
lst = [1, 2, 3, 4, 5]
lst.reverse()
# The methods for a list are:

#     append
#     count
#     extend
#     insert
#     pop
#     remove
#     reverse
#     sort

# Let's try out a few of them:

# append() allows us to add elements to the end of a list:

lst.append(6)


lst = [1, 2, 3, 4, 5, 6]

# Great! Now how about count()? The count() method will count the number of occurrences of an element in a list.

# # Check how many times 2 shows up in the list
lst.count(2)

# In general Python you can use the help() function:

help(lst.count)

# Help on built-in function count:

# count(...) method of builtins.list instance
#     L.count(value) -> integer -- return number of occurrences of value
