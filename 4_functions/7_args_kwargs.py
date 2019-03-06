
# *args and **kwargs

# Arguments

# ARGUEMENTS

#     A value passed to a function (or method) when calling the function. There are two kinds of argument:

# KEYWORD ARGUMENT: an argument preceded by an IDENTIFIER (e.g. name=) in a FUNCTION CALL
# OR VALUE PASSED in a DICTIONARY preceded by **.

#  For example, 3 and 5 are both keyword arguments in the following calls to complex():

#         complex(real=3, imag=5)
#         complex(**{'real': 3, 'imag': 5})

# POSITIONAL ARGUMENT: an argument that is not a keyword argument.
#       can appear at the beginning of an argument list
#       and/or be PASSED as elements of an ITERABLE preceded by *.
#
#        For example, 3 and 5 are both positional arguments in the following calls:

#         complex(3, 5)
#         complex(*(3, 5))

#     Arguments are assigned to the named local variables in a function body.
#     See the Calls section for the rules governing this assignment.
#       Syntactically, any expression can be used to represent an argument;
#       the evaluated value is assigned to the local variable.


# In user-defined function topic, we learned about defining a function and calling it. Otherwise, the function call will result into an error. Here is an example.

# PARAMETER

#     A NAMED entity in a function (or method) definition that specifies an argument
#     (or in some cases, arguments).
#
#      There are five kinds of parameter:

#      POSITIONAL-OR-KEYWORD: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example foo and bar in the following:

#          def func(foo, bar=None): ...

#       POSITIONAL-ONLY: specifies an argument that can be supplied only by position. Python has no syntax for defining positional-only parameters. However, some built-in functions have positional-only parameters (e.g. abs()).

#       KEYWORD-ONLY: specifies an argument that can be supplied only by keyword. Keyword-only parameters can be defined by including a single var-positional parameter or bare * in the parameter list of the function definition before them, for example kw_only1 and kw_only2 in the following:

#         def func(arg, *, kw_only1, kw_only2): ...

#        VAR-POSITIONAL: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with *, for example args in the following:

#         def func(*args, **kwargs): ...

#        VAR-KEYWORD: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with **, for example kwargs in the example above.

#     Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

def greet0(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)


greet0("Monica", "Good morning!")

# Hello Monica, Good morning!

# Here, the function greet() has two parameters.

# Since, we have called this function with two arguments, it runs smoothly and we do not get any error.

# If we call it with different number of arguments, the interpreter will complain. Below is a call to this function with one and no arguments along with their respective error messages.

# >>> greet("Monica")    # only one argument
# TypeError: greet() missing 1 required positional argument: 'msg'

# >>> greet()    # no arguments
# TypeError: greet() missing 2 required positional arguments: 'name' and 'msg'

# Variable Function Arguments

# Up until now functions had fixed number of arguments. In Python there are other ways to define a function which can take variable number of arguments.

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

# In this function, the parameter name does not have a default value and is required (mandatory) during a call.

# On the other hand, the parameter msg has a default value of "Good morning!". So, it is optional during a call. If a value is provided, it will overwrite the default value.

# Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.

# This means to say, non-default arguments cannot follow default arguments. For example, if we had defined the function header above as:

# def greet(msg = "Good morning!", name):

# We would get an error as:

# SyntaxError: non-default argument follows default argument

# Python Keyword Arguments

# When we call a function with some values, these values get assigned to the arguments according to their position.

# For example, in the above function greet(), when we called it as greet("Bruce","How do you do?"), the value "Bruce" gets assigned to the argument name and similarly "How do you do?" to msg.

# Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed. Following calls to the above function are all valid and produce the same result.

# >>> # 2 keyword arguments
# >>> greet(name = "Bruce",msg = "How do you do?")

# >>> # 2 keyword arguments (out of order)
# >>> greet(msg = "How do you do?",name = "Bruce")

# >>> # 1 positional, 1 keyword argument
# >>> greet("Bruce",msg = "How do you do?")

# As we can see, we can mix positional arguments with keyword arguments during a function call. But we must keep in mind that keyword arguments must follow positional arguments.

# Having a positional argument after keyword arguments will result into errors. For example the function call as follows:

# greet(name="Bruce","How do you do?")

# Will result into error as:

# SyntaxError: non-keyword arg after keyword arg

# Python Arbitrary Arguments

# Sometimes, we do not know in advance the number of arguments that will be passed into a function.Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.

# In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument. Here is an example.


def greet2(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet2("Monica", "Luke", "Steve", "John")

# Output

# Hello Monica
# Hello Luke
# Hello Steve
# Hello John

# Here, we have called the function with multiple arguments. These arguments get wrapped up into a tuple before being passed into the function. Inside the function, we use a for loop to retrieve all the arguments back.

# Check out these examples to learn more:


# Work with Python long enough, and eventually you will encounter *args and **kwargs. These strange terms show up as parameters in function definitions. What do they do? Let's review a simple function:
# In [1]:

# def myfunc(a,b):
#     return sum((a,b))*.05

# myfunc(40,60)

# Out[1]:

# 5.0

# This function returns 5% of the sum of a and b. In this example, a and b are positional arguments; that is, 40 is assigned to a because it is the first argument, and 60 to b. Notice also that to work with multiple positional arguments in the sum() function we had to pass them in as a tuple.

# What if we want to work with more than two numbers? One way would be to assign a lot of parameters, and give each one a default value.
# In [2]:

# def myfunc(a=0,b=0,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))*.05

# myfunc(40,60,20)

# Out[2]:

# 6.0

# Obviously this is not a very efficient solution, and that's where *args comes in.
# *args

# When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:
# In [3]:

# def myfunc(*args):
#     return sum(args)*.05

# myfunc(40,60,20)

# Out[3]:

# 6.0

# Notice how passing the keyword "args" into the sum() function did the same thing as a tuple of arguments.

# It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:
# In [4]:

# def myfunc(*spam):
#     return sum(spam)*.05

# myfunc(40,60,20)

# Out[4]:

# 6.0

# **kwargs

# Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs. For example:
# In [5]:

# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
#     else:
#         print("I don't like fruit")

# myfunc(fruit='pineapple')

# My favorite fruit is pineapple

# In [6]:

# myfunc()

# I don't like fruit

# *args and **kwargs combined

# You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
# In [7]:

# def myfunc(*args, **kwargs):
#     if 'fruit' and 'juice' in kwargs:
#         print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
#         print(f"May I have some {kwargs['juice']} juice?")
#     else:
#         pass

# myfunc('eggs','spam',fruit='cherries',juice='orange')

# I like eggs and spam and my favorite fruit is cherries
# May I have some orange juice?

# Placing keyworded arguments ahead of positional arguments raises an exception:
# In [8]:

# myfunc(fruit='cherries',juice='orange','eggs','spam')

#   File "<ipython-input-8-fc6ff65addcc>", line 1
#     myfunc(fruit='cherries',juice='orange','eggs','spam')
#                                           ^
# SyntaxError: positional argument follows keyword argument

# As with "args", you can use any name you'd like for keyworded arguments - "kwargs" is just a popular convention.

# That's it! Now you should understand how *args and **kwargs provide the flexibilty to work with arbitrary numbers of arguments!
