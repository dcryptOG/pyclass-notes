#! PEP8 use lowercase no caps
#! Python uses SNAKE CASE _underscore
# * CAPS for GLOBAL VAR

# ? Avoid using kw or keywords like
# ie str is reserved
# * There are 33 keywords in Python 3.3. This number can vary slightly in course of time.
# python keywords are case senstive


#! DYNAMIC TYPING - can reassign variables to differnt data types
# * other languages are Statically Typed

# ? EX value of a can be changed

import keyword
a = 5
print(a + a)
a = 10
print(a + a)

num_x = 2
print(num_x)


print('\nVAR SYNTAX SNAKE CASE')
my_dogs = 2
print(my_dogs)
my_dogs = ["Sammy", "Frankie"]
print(my_dogs)
print(type(my_dogs))


#!  be aware of type() in python to avoid bugs


my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)


#!KEYWORDS

# * ALL KEYWORDS ARE LOWERCASE... EXCEPT
# ? True
# ?  False
# ? None


# >>> import keyword
print(keyword.kwlist)

#! The list of all the keywords are given below.

# * while
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. Use when we don't know number of times to iterate

# * for
# used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

# * break
# interrupt the (loop) cycle, if needed

# * continue
# used to interrupt the current cycle, without jumping out of the whole cycle.
# New cycle will begin.

# * if
# used to determine, which statements are going to be executed.

# * elif
# stands for else if.If the first test evaluates to False,
# then it continues with the next one

# * else
# is optional. The statement after the else keyword is executed, unless the condition is True

# * is
# tests for object identity

# * not
# negates a boolean value

# * and
# all conditions in a boolean expression must be met

# * or
# at least one condition must be met.

# * import
# import other modules into a Python script

# * as
# if we want to give a module a different alias

# * from
# for importing a specific variable, class or a function from a module

# * def
# used to create a new user defined function

# * return
# exits the function and returns a value

# * lambda
# creates a new anonymous function

# * global
# access variables defined outside functions

# * try
# specifies exception handlers

# * except
# catches the exception and executes codes

# * finally
# is always executed in the end. Used to clean up resources.

# * raise
# create a user defined exception

# * del
# deletes objects

# * pass
# does nothing

# * assert
# used for debugging purposes

# * class
# used to create new user defined objects

# * exec
# executes Python code dynamically

# * yield
# is used with generators

#! Python Identifiers

#! Identifier is the name given to entities like class, functions, variables etc. in Python. It helps differentiating one entity from another.
# * Rules for writing identifiers

#     Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). Names like myClass, var_1 and print_this_to_screen, all are valid example.

#     An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.

# todo     Keywords cannot be used as identifiers.

#     >>> global = 1
#       File "<interactive input>", line 1
#         global = 1
#                ^
#     SyntaxError: invalid syntax

#     We cannot use special symbols like !, @, #, $, % etc. in our identifier.


#     >>> a@ = 0
#       File "<interactive input>", line 1
#         a@ = 0
#          ^
#     SyntaxError: invalid syntax

#     Identifier can be of any length.

# Python is a case-sensitive language. This means, Variable and variable are not the same. Always name identifiers that make sense.

# ==========================#==========================

#                           ! What is Name in Python?

#! Name (also called identifier) is simply a name given to objects.

# Everything in Python is an object.

#  Name is a way to access the underlying object.

# NOTE
#  when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with.
#
# todo                                  Get the address (in RAM) of some Object through the built-in function, id(). Let's check it.

# Note: You may get different value of id

a = 2
# Output: id(2)= 10919424
print('a=2\nid(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))
# Here, both refer to the same object.

# NOTE You may get different value of id

a = a+1

# Output: id(a) = 10919456
print('\na = a+1\nid(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2

# Output: id(2)= 10919424
print('b=2\nid(b) =', id(b))
print('id(2) =', id(2))

# ?What is happening in the above sequence of steps?

# Initially, an object 2 is created and the name a is associated with it, when we do a = a+1, a new object 3 is created and now a associates with this object.

# Note that id(a) and id(3) have same values.

# Furthermore, when we do b = 2, the new name b gets associated with the previous object 2.

# This is efficient as Python doesn't have to create a new duplicate object. This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

# >>> a = 5
# >>> a = 'Hello World!'
# >>> a = [1,2,3]

# All these are valid and a will refer to three different types of object at different instances. Functions are objects too, so a name can refer to them as well.


def printHello():
    print("Hello")


a = printHello()

# Output: Hello
a

# Our same name a can refer to a function and we can call the function through it, pretty neat.

#! What is a Namespace in Python?

# So now that we understand what names are, we can move on to the concept of namespaces.

# To simply put it, namespace is a collection of names.

# In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

# Different namespaces can co-exist at a given time but are completely isolated.

# A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

# This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.

# These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.

# Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it. Similar, is the case with class. Following diagram may help to clarify this concept.

# Nested Namespaces in Python Programming

# ==========================#==========================


#! Python Variable Scope

# Although there are various unique namespaces defined, we may not be able to access all of them from every part of the program. The concept of scope comes into play.

# Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

# At any given moment, there are at least three nested scopes.

#     Scope of the current function which has local names
#     Scope of the module which has global names
#     Outermost scope which has built-in names

# When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

# If there is a function inside another function, a new scope is nested inside the local scope.
# Example of Scope and Namespace in Python


def outer_function():
    b = 20

    def inner_func():
        c = 30


a = 10

# Here, the variable a is in the global namespace. Variable b is in the local namespace of outer_function() and c is in the nested local namespace of inner_function().

# When we are in inner_function(), c is local to us, b is nonlocal and a is global. We can read as well as assign new values to c but can only read b and a from inner_function().

# If we try to assign as a value to b, a new variable b is created in the local namespace which is different than the nonlocal b. Same thing happens when we assign a value to a.

# However, if we declare a as global, all the reference and assignment go to the global a. Similarly, if we want to rebind the variable b, it must be declared as nonlocal. The following example will further clarify this.


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# As you can see, the output of this program is

# a = 30
# a = 20
# a = 10

# In this program, three different variables a are defined in separate namespaces and accessed accordingly. While in the following program,


def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# The output of the program is.

# a = 30
# a = 30
# a = 30

# Here, all reference and assignment are to the global a due to the use of keyword global.
