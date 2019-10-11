# Python Built-in Function
# The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions. For example, print() function prints the given object to the standard output device (screen) or to the text stream file.

#                           !MAP()

# map() is a built-in Python function that takes in two or more arguments: a function and one or more iterables, in the form:

# map(function, iterable, ...)

# map() returns an iterator - that is, map() returns a special object that yields one result at a time as needed. We will learn more about iterators and generators in a future lecture. For now, since our examples are so small, we will cast map() as a list to see the results immediately.

# When we went over list comprehensions we created a small expression to convert Celsius to Fahrenheit. Let's do the same here but use map:
# In [1]:

# def fahrenheit(celsius):
#     return (9/5)*celsius + 32

# temps = [0, 22.5, 40, 100]

# Now let's see map() in action:
# In [2]:

# F_temps = map(fahrenheit, temps)

# #Show
# list(F_temps)

# Out[2]:

# [32.0, 72.5, 104.0, 212.0]

# In the example above, map() applies the fahrenheit function to every item in temps. However, we don't have to define our functions beforehand; we can use a lambda expression instead:
# In [3]:

# list(map(lambda x: (9/5)*x + 32, temps))

# Out[3]:

# [32.0, 72.5, 104.0, 212.0]

# Great! We got the same result! Using map with lambda expressions is much more common since the entire purpose of map() is to save effort on having to create manual for loops.
# map() with multiple iterables

# map() can accept more than one iterable. The iterables should be the same length - in the event that they are not, map() will stop as soon as the shortest iterable is exhausted.

# For instance, if our function is trying to add two values x and y, we can pass a list of x values and another list of y values to map(). The function (or lambda) will be fed the 0th index from each list, and then the 1st index, and so on until the n-th index is reached.

# Let's see this in action with two and then three lists:
# In [4]:

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]

# list(map(lambda x,y:x+y,a,b))

# Out[4]:

# [6, 8, 10, 12]

# In [5]:

# # Now all three lists
# list(map(lambda x,y,z:x+y+z,a,b,c))

# Out[5]:

# [15, 18, 21, 24]

# We can see in the example above that the parameter x gets its values from the list a, while y gets its values from b and z from list c. Go ahead and play with your own example to make sure you fully understand mapping to more than one iterable.

# Great job! You should now have a basic understanding of the map() function.


#                           !REDUCE()


# reduce()

# Many times students have difficulty understanding reduce() so pay careful attention to this lecture. The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value.

# If seq = [ s1, s2, s3, ... , sn ], calling reduce(function, sequence) works like this:

#     At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
#     The list on which reduce() works looks now like this: [ function(s1, s2), s3, ... , sn ]
#     In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
#     The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
#     It continues like this until just one element is left and return this element as the result of reduce()

# Let's see an example:
# In [1]:

# from functools import reduce

# lst =[47,11,42,13]
# reduce(lambda x,y: x+y,lst)

# Out[1]:

# 113

# Lets look at a diagram to get a better understanding of what is going on here:
# In [2]:

# from IPython.display import Image
# Image('http://www.python-course.eu/images/reduce_diagram.png')

# Out[2]:

# Note how we keep reducing the sequence until a single final value is obtained. Lets see another example:
# In [3]:

# #Find the maximum of a sequence (This already exists as max())
# max_find = lambda a,b: a if (a > b) else b

# In [4]:

# #Find max
# reduce(max_find,lst)

# Out[4]:

# 47

# Hopefully you can see how useful reduce can be in various situations. Keep it in mind as you think about your code projects!


#                           !FILTER()


# filter

# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True.

# The function filter(function,list) needs a function as its first argument. The function needs to return a Boolean value (either True or False). This function will be applied to every element of the iterable. Only if the function returns True will the element of the iterable be included in the result.

# Like map(), filter() returns an iterator - that is, filter yields one result at a time as needed. Iterators and generators will be covered in an upcoming lecture. For now, since our examples are so small, we will cast filter() as a list to see our results immediately.

# Let's see some examples:
# In [1]:

# #First let's make a function
# def even_check(num):
#     if num%2 ==0:
#         return True

# Now let's filter a list of numbers. Note: putting the function into filter without any parentheses might feel strange, but keep in mind that functions are objects as well.
# In [2]:

# lst =range(20)

# list(filter(even_check,lst))

# Out[2]:

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# filter() is more commonly used with lambda functions, because we usually use filter for a quick job where we don't want to write an entire function. Let's repeat the example above using a lambda expression:
# In [3]:

# list(filter(lambda x: x%2==0,lst))

# Out[3]:

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Great! You should now have a solid understanding of filter() and how to apply it to your code!


#                           !ZIP()


# zip

# zip() makes an iterator that aggregates elements from each of the iterables.

# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

# zip() is equivalent to:

# def zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)


# zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables.

# Let's see it in action in some examples:
# Examples
# In [1]:

# x = [1,2,3]
# y = [4,5,6]

# # Zip the lists together
# list(zip(x,y))

# Out[1]:

# [(1, 4), (2, 5), (3, 6)]

# Note how tuples are returned. What if one iterable is longer than the other?
# In [2]:

# x = [1,2,3]
# y = [4,5,6,7,8]

# # Zip the lists together
# list(zip(x,y))

# Out[2]:

# [(1, 4), (2, 5), (3, 6)]

# Note how the zip is defined by the shortest iterable length. Its generally advised not to zip unequal length iterables unless your very sure you only need partial tuple pairings.

# What happens if we try to zip together dictionaries?
# In [3]:

# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}

# list(zip(d1,d2))

# Out[3]:

# [('a', 'c'), ('b', 'd')]

# This makes sense because simply iterating through the dictionaries will result in just the keys. We would have to call methods to mix keys and values:
# In [4]:

# list(zip(d2,d1.values()))

# Out[4]:

# [('c', 1), ('d', 2)]

# Great! Finally lets use zip() to switch the keys and values of the two dictionaries:
# In [5]:

# def switcharoo(d1,d2):
#     dout = {}

#     for d1key,d2val in zip(d1,d2.values()):
#         dout[d1key] = d2val

#     return dout

# In [6]:

# switcharoo(d1,d2)

# Out[6]:

# {'a': 4, 'b': 5}

# Great! You can use zip to save a lot of typing in many situations! You should now have a good understanding of zip() and some possible use cases.


#                           !ENUMERATE()


# enumerate()

# In this lecture we will learn about an extremely useful built-in function: enumerate(). Enumerate allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element). The function itself is equivalent to:

# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1

# Example
# In [1]:

# lst = ['a','b','c']

# for number,item in enumerate(lst):
#     print(number)
#     print(item)

# 0
# a
# 1
# b
# 2
# c

# enumerate() becomes particularly useful when you have a case where you need to have some sort of tracker. For example:
# In [2]:

# for count,item in enumerate(lst):
#     if count >= 2:
#         break
#     else:
#         print(item)

# a
# b

# enumerate() takes an optional "start" argument to override the default value of zero:
# In [3]:

# months = ['March','April','May','June']

# list(enumerate(months,start=3))

# Out[3]:

# [(3, 'March'), (4, 'April'), (5, 'May'), (6, 'June')]

# Great! You should now have a good understanding of enumerate and its potential use cases.


#!                          ALL() and ANY


# all() and any()

# all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable. all() will return True if all elements in an iterable are True. It is the same as this function code:

# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# any() will return True if any of the elements in the iterable are True. It is equivalent to the following function code:

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# Let's see a few examples of these functions. They should be fairly straightforward:
# In [1]:

# lst = [True,True,False,True]

# In [2]:

# all(lst)

# Out[2]:

# False

# Returns False because not all elements are True.
# In [3]:

# any(lst)

# Out[3]:

# True

# Returns True because at least one of the elements in the list is True

# There you have it, you should have an understanding of how to use any() and all() in your code.


#!                          COMPLEX()


# complex()

# complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number.

# If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

# If you are doing math or engineering that requires complex numbers (such as dynamics, control systems, or impedance of a circuit) this is a useful tool to have in Python.

# Let's see some examples:
# In [1]:

# # Create 2+3j
# complex(2,3)

# Out[1]:

# (2+3j)

# In [2]:

# complex(10,1)

# Out[2]:

# (10+1j)

# We can also pass strings:
# In [3]:

# complex('12+2j')

# Out[3]:

# (12+2j)

# That's really all there is to this useful function. Keep it in mind if you are ever dealing with complex numbers in Python!


#!END OF UDEMY========================================

# In Python 3.6 (latest version), there are 68 built-in functions. They are listed below alphabetically along with brief description.
# Search Built-in Method
# Method 	Description
# Python abs() 	returns absolute value of a number
# Python all() 	returns true when all elements in iterable is true
# Python any() 	Checks if any Element of an Iterable is True
# Python ascii() 	Returns String Containing Printable Representation
# Python bin() 	converts integer to binary string
# Python bool() 	Converts a Value to Boolean
# Python bytearray() 	returns array of given byte size
# Python bytes() 	returns immutable bytes object
# Python callable() 	Checks if the Object is Callable
# Python chr() 	Returns a Character (a string) from an Integer
# Python classmethod() 	returns class method for given function
# Python compile() 	Returns a Python code object
# Python complex() 	Creates a Complex Number
# Python delattr() 	Deletes Attribute From the Object
# Python dict() 	Creates a Dictionary
# Python dir() 	Tries to Return Attributes of Object
# Python divmod() 	Returns a Tuple of Quotient and Remainder
# Python enumerate() 	Returns an Enumerate Object
# Python eval() 	Runs Python Code Within Program
# Python exec() 	Executes Dynamically Created Program
# Python filter() 	constructs iterator from elements which are true
# Python float() 	returns floating point number from number, string
# Python format() 	returns formatted representation of a value
# Python frozenset() 	returns immutable frozenset object
# Python getattr() 	returns value of named attribute of an object
# Python globals() 	returns dictionary of current global symbol table
# Python hasattr() 	returns whether object has named attribute
# Python hash() 	returns hash value of an object
# Python help() 	Invokes the built-in Help System
# Python hex() 	Converts to Integer to Hexadecimal
# Python id() 	Returns Identify of an Object
# Python input() 	reads and returns a line of string
# Python int() 	returns integer from a number or string
# Python isinstance() 	Checks if a Object is an Instance of Class
# Python issubclass() 	Checks if a Object is Subclass of a Class
# Python iter() 	returns iterator for an object
# Python len() 	Returns Length of an Object
# Python list() Function 	creates list in Python
# Python locals() 	Returns dictionary of a current local symbol table
# Python map() 	Applies Function and Returns a List
# Python max() 	returns largest element
# Python memoryview() 	returns memory view of an argument
# Python min() 	returns smallest element
# Python next() 	Retrieves Next Element from Iterator
# Python object() 	Creates a Featureless Object
# Python oct() 	converts integer to octal
# Python open() 	Returns a File object
# Python ord() 	returns Unicode code point for Unicode character
# Python pow() 	returns x to the power of y
# Python print() 	Prints the Given Object
# Python property() 	returns a property attribute
# Python range() 	return sequence of integers between start and stop
# Python repr() 	returns printable representation of an object
# Python reversed() 	returns reversed iterator of a sequence
# Python round() 	rounds a floating point number to ndigits places.
# Python set() 	returns a Python set
# Python setattr() 	sets value of an attribute of object
# Python slice() 	creates a slice object specified by range()
# Python sorted() 	returns sorted list from a given iterable
# Python staticmethod() 	creates static method from a function
# Python str() 	returns informal representation of an object
# Python sum() 	Add items of an Iterable
# Python super() 	Allow you to Refer Parent Class by super
# Python tuple() Function 	Creates a Tuple
# Python type() 	Returns Type of an Object
# Python vars() 	Returns __dict__ attribute of a class
# Python zip() 	Returns an Iterator of Tuples
# Python __import__() 	Advanced Function Called by import
