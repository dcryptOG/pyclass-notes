
# Functions
# Introduction to Functions

# Types of Functions

# 2 two types:

#     Built-in functions - Functions that are built into Python.
#     User-defined functions - Functions defined by the users themselves.

# So what is a function?

# In Python, function is a set of related statements that perform a specific task, reducing repetitive code.

# They can also let us specify parameters that can serve as inputs to the functions.

# Furthermore, it avoids repetition and makes code reusable.

# Above shown is a function definition which consists of following components.

#     Keyword def marks the start of function header.
#     A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
#     PARAMETERS (ARGUMENTS) through which we pass values to a function. OPTIONAL.
#     Arguments can be used in a function and referenced within the function
#     A COLON (:) @ end of function header.
#     Optional documentation string (docstring) to describe what the function does.
#     One or more valid python statements that make up the function body.
#     Statements must have same indentation level (usually 4 spaces).
#     An optional return statement to return a value from the function.

# EX1

# Let's see how to build out a function's syntax in Python. It has the following form:

# def name_of_function(arg1,arg2):
#     '''
#     This is where the function's Document String (docstring) goes
#     '''
#     # Do stuff here
#     # Return desired result

import math
print(
    'SYNTAX FUNCTION\ndef name_of_function(arg1, arg2): \n    Document String(docstring) goes\n    Do stuff here\n    Return desired result')

print('EX1\ndef greet(name):    \n"""This function greets to    \nthe person passed in as\n    parameter"""\n    print("Hello, " + name + ". Good morning!") ')


def greet(name):
    """This function greets to
    the person passed in as
    parameter"""
    print("Hello, " + name + ". Good morning!")

# call function


print('\ncall function\ngreet("Paul")')
greet('Paul')


# DOCSTRING AKA DOCUMENTATION STRING = The first string after the function header to explain what a function does.

# In the above example, we have a docstring immediately below the function header.
# We generally use triple quotes so that docstring can extend up to multiple lines.
#  This string is available to us as __doc__ attribute of the function.

# For example:

# Try running the following into the Python shell to see the output.
print('\nprint(greet.__doc__)')
print(greet.__doc__)
# OUTPUT
# This function greets to
# 	the person passed into the
# 	name parameter

# RETURN STATEMENT
print("\nRETURN STATEMENT\n")
# The RETURN statement is used to EXIT a FUNCTION
# Going back to the place it was CALLED.

# Syntax of return

# return [expression_list]

print('\nreturn [expression_list]')

# If there is NO EXPRESSION in the statement
# OR the NO RETURN STATEMENT inside a function,
#  THEN the function will return the None object.


# Next you'll see the docstring, this is where you write a basic description of the function.

# Example 1: A simple print 'hello' function
print('EX2\ndef say_hello():\n    print("hello")')


def say_hello():
    print('hello')

# Call the function:


say_hello()

# output: hello

# Example 3: A simple greeting function

# Let's write a function that greets people with their name.

print("\nEX3\ndef greeting(name):\n    print('Hello %s' % (name))")


def greeting(name):
    print('Hello %s' % (name))


greeting('Jose')

# Hello Jose

# Using return

# Let's see some example that use a return statement. return allows a function to return a result that can then be stored as a variable, or used in whatever manner a user wants.
# Example 4: Addition function
print('\nEX4\ndef add_num(num1, num2):\n    return num1+num2')


def add_num(num1, num2):
    return num1+num2


add_num(4, 5)

# # Can also save as variable due to return
result = add_num(4, 5)

print(result)

# What happens if we input two strings?


add_num('one', 'two')


# 'onetwo'

# Note that because we don't declare variable types in Python, this function could be used to add numbers or sequences together!
# We'll later learn about adding in checks to make sure a user puts in the correct arguments into a function.

# Let's also start using break, continue, and pass statements in our code.

# Check if a number is prime (a common interview exercise).

# We know a number is prime if that number is only evenly divisible by 1 and itself.
# Let's write our first version of the function to check all the numbers from 1 to N and perform modulo checks.


def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
    else:  # If never mod zero, then prime
        print(num, 'is prime!')


is_prime(16)

# 16 is not prime


is_prime(17)

# 17 is prime!

# Note how the else lines up under for and not if.
#  This is because we want the for loop to exhaust all possibilities in the range before printing our number is prime.

# Also note how we break the code after the first print statement.
# As soon as we determine that a number is not prime we break out of the for loop.

# We can actually improve this function by only checking to the square root of the target number,
# Disregarding all even numbers after checking for 2.

#  We'll also switch to returning a boolean value to get an example of using return statements:


def is_prime2(num):
    '''
    Better method of checking for primes.
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


is_prime2(18)


# False

# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

# In this program, variable num is checked if it's prime or not. Numbers less than or equal to 1 are not prime numbers. Hence, we only proceed if the num is greater than 1.

# We check if num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime. Else the number is prime.

# We can decrease the range of numbers where we look for factors.

# In the above program, our search range is from 2 to num - 1.

# We could have used the range, [2, num / 2] or [2, num ** 0.5]. The later range is based on the fact that a composite number must have a factor less than square root of that number; otherwise the number is prime.

# You can change the value of variable num in the above source code and test for other integers (if you want).

# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Why don't we have any break statements?
# It should be noted that as soon as a function returns something, it shuts down.
# A function can deliver multiple print statements, but it will only obey one return.

# Start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).
