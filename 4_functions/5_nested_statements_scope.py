
# ! Nested Statements and Scope

# Scope and Lifetime of variables

#! SCOPE of a Var = is the portion of a program where the variable is recognized.

# *  LOCAL SCOPE = PARAMETERS and VARS defined inside a function is not visible from outside.

#! LIFETIME OF A VAR = is the period throughout which the variable exits in the MEMORY.

# ?  The lifetime of variables inside a function is as long as the function executes.

# They are destroyed once we return from the function.

# Hence, a function does not remember the value of a variable from its previous calls.


def my_func():
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)

# Here, we can see that the value of x is 20 initially.

#  Even though the function my_func() changed the value of x to 10, it did not effect the value outside the function.

# This is because the variable x inside the function is different (local to the function) from the one outside.

# Although they have same names, they are two different variables with different scope.

# ! GLOBAL SCOPE = variables outside of the function are visible from inside.

# ? We can read these values from inside the function
# *but cannot change (write) them.
# todo                                                  to change value of vars outside func, declar GLOBAL VAR using KEYWORD GLOBAL

# When you create a variable name in Python the name is stored in a name-space.
# Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.

# ! Global Variables

# In Python, a variable declared outside of the function or in global scope is known as global variable.
# This means, global variable can be accessed inside or outside of the function.

# Let's see an example on how a global variable is created in Python.

x = "global"


def foo_0():
    print("x inside :", x)


foo_0()
print("x outside:", x)

# When we run the code, the will output be:

# x inside : global
# x outside: global

# In above code, we created x as a global variable and defined a foo_() to print the global variable x.
# Finally, we call the foo_() which will print the value of x.

# * What if you want to change value of x inside a function?

x = "global"


# !def foo_1():
#  !   x = x * 2
#!     print(x)


# !print(foo_1())

# ? UnboundLocalError: local variable 'x' referenced before assignment

# The output shows an error because Python treats x as a local variable and x is also not defined inside foo_().

# ! Local Variables

# A variable declared inside the function's body or in the local scope is known as local variable.

# ? Example 2: Accessing local variable outside the scope


def foo_2():
    y = "local"


print('\nEX Local Var ', foo_2())
# ! print(y)

# https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When we run the code, the will output be:

# * NameError: name 'y' is not defined

# The output shows an error, because we are trying to access a local variable y in a global scope whereas the local variable only works inside foo_() or local scope.

# ? Example 3: Create a Local Variable

# Normally, we declare a variable inside the function to create a local variable.


def foo_3():
    y = "local"
    print(y)


print('\nex3')
foo_3()

# When we run the code, it will output:

# local

# Let's take a look to the earlier problem where x was a global variable and we wanted to modify x inside foo_().
# Global and local variables

# ? Example 4: Using Global and Local variables in same code

print('\nExample 4: Using Global and Local variables in same code')

x = "global"


def foo_4():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


foo_4()

# When we run the code, the will output be:

# global global
# local

# In the above code, we declare x as a global and y as a local variable in the foo_(). Then, we use multiplication operator * to modify the global variable x and we print both x and y.

# After calling the foo_(), the value of x becomes global global because we used the x * 2 to print two times global.
#
# After that, we print the value of local variable y i.e local.

# ? Example 5: Global variable and Local variable with same name

print('\nExample 5: Global variable and Local variable with same name')

x = 5


def foo_5():
    x = 10
    print("local x:", x)


foo_5()
print("global x:", x)

# When we run the code, the will output be:

# local x: 10
# global x: 5

# In above code, we used same name x for both global variable and local variable.

# We get different result when we print same variable because the variable is declared in both scopes, i.e. the local scope inside foo_() and global scope outside foo_().

# When we print the variable inside the foo_() it outputs local x: 10, this is called local scope of variable.

# Similarly, when we print the variable outside the foo_(), it outputs global x: 5, this is called global scope of variable.

# ! Nonlocal Variables

# Nonlocal variable are used in nested function whose local scope is not defined.

#  This means, the variable can be neither in the local nor the global scope.

# We use NONLOCAL KEYWORD to create nonlocal variable.


# ? Example 6: Create a nonlocal variable

print('\nExample 6: Create a nonlocal variable')


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# When we run the code, the will output be:

# inner: nonlocal
# outer: nonlocal

# In the above code there is a nested function inner().

# We use nonlocal keyword to create nonlocal variable.

# ! The inner() function is defined in the scope of another function outer().

# Note : If we change value of nonlocal variable, the changes appears in the local variable.

print('\n=====UDEMY ACTIVITES======\n')

print('EX1')
x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

# print(x)

# 25


# print(printer())

# 50

# This idea of scope in your code is very important to understand in order to properly assign and call variable names.

# In simple terms, the idea of scope can be described by 3 general rules:

# *   1. NAME ASSIGN will create or change local names by default.
# *      2. Name ref. search (at most) 4 SCOPES, these are:
# todo                           L = local
# todo                           E = enclosing functions
# todo                           G = global
# todo                           B = built-in
# *       3. NAMES in GLOBAL and NONLOCAL statements map assigned names to ENCLOSING MODULE and FUNCTION SCOPES.

# The statement in #2 above can be defined by the LEGB rule.

# ! LEGB Rule:

# ? L: LOCAL —
# NAMES assigned in any way WITHIN a FUNCTION (def or lambda), and NOT declared global in that function.

# ? E: ENCLOSING FUNCTION LOCALS —
# NAMES in the LOCAL SCOPE of any AND all ENCLOSING FUNCTIONS (def or lambda), from inner to outer.

# ? G: GLOBAL (module) —
# Names assigned at the TOP-LEVEL of a module file, or declared GLOBAL in a DEF within the file.

# ? B: BUILT-IN (Python) —
# Names preassigned in the built-in names module : open, range, SyntaxError,...


# ? Quick examples of LEGB
# Local

# # x is local here:

print('\nEX2: LOCAL VAR\n', 'def f(x): return x**2\n', 'x is loval')


def f(x): return x**2

# Enclosing function locals

# This occurs when we have a function inside a function (nested functions)


print('\nEX3: Enclosing Function Locals\nname="This is a global name"\n',
      '\ndef greet():\n    name = "Sammy"\n    def hello():\n        print("Hello " + name)\n    hello()\n')

name = 'This is a global name'


def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)
# ! LOCAL name= 'Geoff'
    hello()


print('Sammy is Enclosing Func Local Var\ngreet()')
greet()

# Hello Sammy

# Note how Sammy was used, because the hello() function was enclosed inside of the greet function!
# Global

print('\nGlobal var\n', name)

# This is a global name

# ! Built-in

# * RESERVRED len()

# <function len>

# Local Variables

# When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function
# - i.e. variable names are local to the function.
#  This is called the scope of the variable.
# ? All variables have the scope of the block they are declared in starting from the point of definition of the name.

# Example:
print('\nEX4:\n')
x = 50


def func(x):
    print(f'output: X is {x}')
    x = 2
    # ! x=2 LOCAL REASSIGNMENT
    print(f'output: Changed local x to {x}')


print('func(x)')
func(x)

print('\nx is still', x)

# x is 50
# Changed local x to 2
# x is still 50

# The first time that we print the value of the name x with the first line in the function’s body, Python uses the value of the parameter declared in the main block, above the function definition.

# Next, we assign the value 2 to x. The name x is local to our function. So, when we change the value of x in the function, the x defined in the main block remains unaffected.

# With the last print statement, we display the value of x as defined in the main block, thereby confirming that it is actually unaffected by the local assignment within the previously called function.
# The global statement

# If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the global statement. It is impossible to assign a value to a variable defined outside a function without the global statement.

# You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function). However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. Using the global statement makes it amply clear that the variable is defined in an outermost block.

# Example:

print('\nEX5\nGLOBAL_KW\n')
x = 50


def func1():
    global x
    print('OUTPUT\nThis function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)


print('Before calling func(), x is: ', x)
print('\ndef func1():\n    global x\n    x = 2\n')
func1()
print('\nValue of x (outside of func()) is: ', x)

# Before calling func(), x is:  50
# This function is now using the global x!
# Because of global x is:  50
# Ran func(), changed global x to 2
# Value of x (outside of func()) is:  2

print('\nEX6: BEST PRACTICE REASSIGN\n')
print('def func1(x):\n    x = 2\n    return x\n')

print('print(x)\noutput: 50')
print('\nx = func(x)\nprint(x)\noutput: 2')

# The global statement is used to declare that x is a global variable - hence, when we assign a value to x inside the function, that change is reflected when we use the value of x in the main block.

# You can specify more than one global variable using the same global statement e.g. global x, y, z.

# ! globals() and locals() functions to check what are your current local and global variables.

# Another thing to keep in mind is that everything in Python is an object! I can assign variables to functio
