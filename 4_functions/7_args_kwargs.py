
# *args and **kwargs

# Arguments

# ! ARGUEMENTS = A value passed to a function (or method) when CALLING the function.
#  There are 2 kinds of argument:

# !1 . KEYWORD ARGUMENT:

#                         ?argument preceded by an IDENTIFIER (e.g. name=) in a FUNCTION CALL
# TODO                                                         complex(real=3, imag=5)

#                          * OR VALUE PASSED in a DICTIONARY preceded by **.
# TODO                                                          complex(**{'real': 3, 'imag': 5})

# !2.  POSITIONAL ARGUMENT: an argument that is not a keyword argument.

#       ? can appear at the beginning of an argument list
# TODO                                                  complex(3, 5)

#       * and/or be PASSED as elements of an ITERABLE preceded by *.
# TODO                                                 complex(*(3, 5))

#   Arguments are assigned to the named local variables in a function body.

#   Syntactically, any expression can be used to represent an argument;the evaluated value is assigned to the local variable.


# In user-defined function topic, we learned about defining a function and calling it. Otherwise, the function call will result into an error. Here is an example.

#! PARAMETERS

#!     A NAMED ENTITY in a function/mehtod DEFINTION that SPECIFIES an ARGS
# *    OR in some, arguments).

# * Parameters specify OPTIONAL_ARGS and REQUIRED_ARGS
# ? as well as DEFAULT VALUES for some OPTIONAL arguments.


# TODO                                                    5 kinds of parameter:

#! POSITIONAL-OR-KEYWORD: specifies an argument that can be passed either positionally or as a keyword argument.
#  TODO                                             def func(foo, bar=None): ...

# !POSITIONAL-ONLY: specifies an argument that can be supplied only by position.
# * Python has NO SYNTAX for defining POSITIONAL-ONLY parameters.
# ? SOME BUILT-IN FUNCTIONS have positional-only parameters (e.g. abs()).

# !KEYWORD-ONLY:
# * ARG that can be supplied ONLY BY KEYWORD.
#  ? DEF by including a SINGLE VAR-POSITIONAL PARAMETER
# ? OR bare * in the BEFORE PARAMETER LIST

# TODO                                                def func(arg, *, kw_only1, kw_only2): ...

# ! VAR-POSITIONAL:
# *An arbitrary SEQUENCE of POSITIONAL ARGS (in addition to any POSITIONAL ARGS already accepted by other parameters).
# ? DEF by PREPENDING the parameter name with *
# TODO                                                        def func(*args): ...
# TODO                                                        def func(*args, **kwargs): ...


#! VAR-KEYWORD:
# * MANY keyword arguments can be provided (in addition to any KW_ARGS already accepted by other parameters).
# ?DEF by PREPENDING the parameter name with **
# TODO                                                        def func(**kwargs): ...
# TODO                                                        def func(*args, **kwargs): ...


# Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

def greet0(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)


greet0("Monica", "Good morning!")

# Hello Monica, Good morning!

# Here, the function greet() has two parameters.

# >>> greet("Monica")    # only one argument
# TypeError: greet() missing 1 required positional argument: 'msg'

# >>> greet()    # no arguments
# TypeError: greet() missing 2 required positional arguments: 'name' and 'msg'

# Variable Function Arguments

# Three different forms of this type are described below.
# Python Default Arguments

# Function arguments can have default values in Python.

# We can provide a default value to an argument by using the assignment operator (=). Here is an example.


def greet1(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet1("Kate")
greet1("Bruce", "How do you do?")

# * PARAM name does NOT have a DEFAULT VALUE and is REQUIRED (mandatory) during a call.

# ? PARAM msg HAS a DEFAULT VALUE of "Good morning!". So, it is OPTIONAL during a call.
#! IF a value is provided, it will OVERWRITE the DEFAULT VALUE.

# AFTER FIRST DEFAULT VALUE... ALL FOLLOWING ARGS to its right MUST have DEFAULT VALUES.

# TODO                          def greet(msg = "Good morning!", name):

# TODO                    SyntaxError: non-default argument follows default argument

# Python Keyword Arguments

# When we call a function with some values, these values get assigned to the arguments according to their position.

# For example, in the above function greet(), when we called it as greet("Bruce","How do you do?"), the value "Bruce" gets assigned to the argument name and similarly "How do you do?" to msg.

# >>> # 2 keyword arguments
greet1(name="Bruce", msg="How do you do?")

# >>> # 2 keyword arguments (out of order)
greet1(msg="How do you do?", name="Bruce")

# >>> # 1 positional, 1 keyword argument
greet1("Bruce", msg="How do you do?")

# ? Having a POSITIONAL_ARGS after KW_ARGS will result into errors.

# * greet1(name="Bruce","How do you do?")

#                                  SyntaxError: non-keyword arg after keyword arg

#! Python Arbitrary Arguments

# In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.


def greet2(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


print('\ndef greet2(*names):\n\tfor name in names:\n\t\tprint("Hello",name)\n')
greet2("Monica", "Luke", "Steve", "John")

# * Output
# Hello Monica
# Hello Luke
# Hello Steve
# Hello John

# Here, we have called the function with MULTIPLE arguments.
# These arguments get wrapped up into a TUPLE before being passed into the function.
# use a for loop to retrieve all the arguments back.

# !UDEMY CLASS EXAMPLES
print('\n')


def myfunc_1(a, b):
    return sum((a, b))*.05


print(myfunc_1(40, 60))

# What if we want to work with more than two numbers? One way would be to assign a lot of parameters, and give each one a default value.


def myfunc2(a=0, b=0, c=0, d=0, e=0):
    return sum((a, b, c, d, e))*.05


print(myfunc2(40, 60, 20), 'hi')


# Obviously this is not a very efficient solution, and that's where *args comes in.
#! *args

#! When a FUNCTION PARAMETER starts with an a*ASTERISK

# *1.    Allows for an arbitrary number of arguments
# *2.    the function takes them in as a TUPLE of values.

# ! PEP 8 IS *args

def myfunc(*args):
    return sum(args)*.05


print('\ndef myfunc(*args):\n    return sum(args)*.05', myfunc(12, 12, 1, 2, 5))

# Notice how passing the keyword "args" into the sum() function did the same thing as a tuple of arguments.

#! **kwargs

#! When a FUNCTION PARAMETER starts with a DOUBLE **ASTERISK

#!1    Allows for an arbitrary number of arguments

#  For example:
print('\n')


def func(**kwargs):
    if 'fruit' in kwargs:
        # review String Formatting and f-strings if this syntax is unfamiliar
        print(f"My favorite fruit is {kwargs['fruit']}")
        # print("My favorite fruit is {}".format(kwargs['fruit']))
    else:
        print("I don't like fruit")


func(fruit='pineapple', veggie='tomato')

# My favorite fruit is pineapple
func()

# I don't like fruit

# *args and **kwargs combined

# ? You can pass *args and **kwargs into the same function
#! but *args MUST be BEFORE **kwargs
print('\n')


def func0(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(
            f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


func0('eggs', 'ham', fruit='cherries', juice='orange')


def func1(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))
# I like eggs and spam and my favorite fruit is cherries
# May I have some orange juice?


print(func1(10, 20, 30, fruit='orange', food='pizzas', animal='dog'))
# * kwargs ahead of positional arguments raises an exception:

# myfunc(fruit='cherries',juice='orange','eggs','spam')

#   File "<ipython-input-8-fc6ff65addcc>", line 1
#     myfunc(fruit='cherries',juice='orange','eggs','spam')
#                                           ^
# ! SyntaxError: positional argument follows keyword argument

# As with "args", you can use any name you'd like for keyworded arguments - "kwargs" is just a popular convention.

# ! RETURN ONLY EVENS


def func4(*args):
    evens = []
    for arg in args:
        if arg % 2 == 0:
            evens.append(arg)
    return evens


print(func4(2, 1, 4))
