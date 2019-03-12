
#!  Lambda Expressions, Map, and Filter

# ? NORMAL FUNCTIONS are defined using the def keyword

# !ANONYMOUS FUNCTION is defined W/O a name.

# *  Anonymous functions are defined using the LAMBDA KEYWORD.

# Hence, anonymous functions are also called lambda functions.
# How to use lambda Functions in Python?

# *Syntax of Lambda Function in python

# todo                                               LAMBDA ARGS: expression

# Lambda functions can have any MANY ARGS
# ONLY 1 EXPRESSION(evaluated & returned).

# Lambda functions can be used wherever function OBJ are REQUIRED.

# Here is an example of lambda function that doubles the input value.

# Program to show the use of lambda functions


# In the above program, lambda x: x * 2 is the lambda function.
# Here x is the argument
# x * 2 is the expression that gets evaluated and returned.

def doubles(x): return x * 2


print(doubles(3))

# is nearly the same as

# def double(x):
#    return x * 2


def double(x): return x * 2


print(double(5))

# This function has no name.
# It returns a function object which is assigned to the identifier double.
# We can now call it as a normal function.


#! We use lambda functions when we require a nameless function for a short period of time.

# lambda funct gernally used as ARG to HIGER-ORDER-FUNCTION
# ! HIGHER-ORDER FUNCTION (a function that takes in other functions as arguments).
# * Lambda functions are used along with built-in functions like filter(), map() etc.

# todo                  EX filter() ===================

# ? The filter() function takes in a FUNCTION and a LIST as ARGS.

# The function is called with all the items in the list

# NEW list is returned
# * contains items for which the function evaluats to True.

# Here is an example use of filter() function to filter out only even numbers from a list.

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

# Output: [4, 6, 8, 12]
print('\nEX filter() ', new_list)

# todo ===============EX map() =====================

# ? The map() function takes in a FUNCTION AND a LIST as ARGS.

# The function is called with all the items in the list

# NEW list is returned

# * MAP() allows you to "map" a function to an ITERABLE OBJ.
# ? can call the same function to EVERY ITEM IN an ITERABLE (ie. list)
# contains items returned by that function for each item.

# Here is an example use of map() function to double all the items in a list.

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print('\nEX map() ', new_list)

# ! PYTHON CLASS ##########################

# map function


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

print('\n', map(square, my_nums))
#! <map at 0x205baec21d0>

# #* To get the results, either iterate through map()
# #? OR just cast to a list

print('\nEX2 MAP() ', list(map(square, my_nums)))
# [1, 4, 9, 16, 25]

# The functions can also be more complex


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]


mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']


print('ex3 map() ', list(map(splicer, mynames)))

# ['even', 'C', 'S', 'K', 'even']

#!=============== filter function===================

# The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.

# def check_even(num):
#     return num % 2 == 0


# nums = [0,1,2,3,4,5,6,7,8,9,10]


# filter(check_even,nums)

# <filter at 0x205baed4710>


# list(filter(check_even,nums))

# [0, 2, 4, 6, 8, 10]

# lambda expression

# One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.

# Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:

# lambda's body is a single expression, not a block of statements.

#     The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

# Lets slowly break down a lambda expression by deconstructing a function:

# def square(num):
#     result = num**2
#     return result


# square(2)

# 4

# We could simplify it:

# def square(num):
#     return num**2


# square(2)

# 4

# We could actually even write this all on one line.

# def square(num): return num**2


# square(2)

# 4

# This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:

# lambda num: num ** 2

# <function __main__.<lambda>>


# # You wouldn't usually assign a name to a lambda expression, this is just for demonstration!
# square = lambda num: num **2


# square(2)

# 4

# So why would use this? Many function calls need a function passed in, such as map and filter. Often you only need to use the function you are passing in once, so instead of formally defining it, you just use the lambda expression. Let's repeat some of the examples from above with a lambda expression

# list(map(lambda num: num ** 2, my_nums))

# [1, 4, 9, 16, 25]


# list(filter(lambda n: n % 2 == 0,nums))

# [0, 2, 4, 6, 8, 10]

# Here are a few more examples, keep in mind the more comples a function is, the harder it is to translate into a lambda expression, meaning sometimes its just easier (and often the only way) to create the def keyword function.

# Lambda expression for grabbing the first character of a string:

# lambda s: s[0]

# <function __main__.<lambda>>

# Lambda expression for reversing a string:

# lambda s: s[::-1]

# <function __main__.<lambda>>

# You can even pass in multiple arguments into a lambda expression. Again, keep in mind that not every function can be translated into a lambda expression.

# lambda x,y : x + y

# <function __main__.<lambda>>

# You will find yourself using lambda expressions often with certain non-built-in libraries, for example the pandas library for data analysis works very well with lambda expressions.
