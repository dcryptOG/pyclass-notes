#
# !Errors and Exception Handling

# todo                               SYNTAX ERROR
# Error caused by not following the proper structure (syntax) of the language is called syntax error or parsing error.

#! >>> if a < 3
#!   File "<interactive input>", line 1
#!     if a < 3
#            ^
#! SyntaxError: invalid syntax

# We can notice here that a colon is missing in the if statement.

#! print('Hello)

#!   File "<ipython-input-1-db8c9988558c>", line 1
# !    print('Hello)
#                  ^
#! SyntaxError: EOL while scanning string literal

# ?SyntaxError, description EOL (End of Line Error) while scanning the string  literal.

#!================================================

#! PYTHON ERRORS AND BUILT-IN EXCEPTIONS

#!================================================

# Even if a statement or expression is syntactically correct...
# Errors can also occur at runtime and these are called exceptions.

# * EXCEPTIONS == Errors detected during execution are called exceptions and are not unconditionally fatal.

# ? Python (interpreter) RAISES EXCEPTIONS when it encounter errors.

# * runtime error PYTHON creates an EXCEPTION OBJECT.
# *? If not handled properly...
# todo       ... it prints a TRACEBACK to error with details about error.

#                            EX: divided by zero.

# They occur, for example, when a file we try to open does not exist (FileNotFoundError), dividing a number by zero (ZeroDivisionError), module we try to import is not found (ImportError) etc.


#! >>> 1 / 0
# ? Traceback (most recent call last):
#!  File "<string>", line 301, in runcode
#!  File "<interactive input>", line 1, in <module>
# * ZeroDivisionError: division by zero

#! >>> open("imaginary.txt")
# ? Traceback (most recent call last):
#!  File "<string>", line 301, in runcode
#!  File "<interactive input>", line 1, in <module>
# * FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'

#!-================================================

#! Python Built-in Exceptions

#!-================================================

# Illegal operations can raise exceptions.

# ? There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.

# * VIEW ALL BUILT IN EXCEPTIONS

# todo                     locals()['__builtins__']

# This will return us a dictionary of built-in exceptions, functions and attributes.

# Some of the common built-in exceptions in Python programming along with the error that cause then are tabulated below.
#! Python Built-in Exceptions Exception 	Cause of Error

# * We can also define our own exception in Python (if required). Visit this page to learn more about user-defined exceptions.

# ? We can handle these built-in and user-defined exceptions in Python using try, except and finally statements.

# AssertionError 	Raised when assert statement fails.

# AttributeError 	Raised when attribute assignment or reference fails.

# EOFError 	Raised when the input() functions hits end-of-file condition.

# FloatingPointError 	Raised when a floating point operation fails.

# GeneratorExit 	Raise when a generator's close() method is called.

# ImportError 	Raised when the imported module is not found.

# IndexError 	Raised when index of a sequence is out of range.

# KeyError 	Raised when a key is not found in a dictionary.

# KeyboardInterrupt 	Raised when the user hits interrupt key (Ctrl+c or delete).

# MemoryError 	Raised when an operation runs out of memory.

# NameError 	Raised when a variable is not found in local or global scope.

# NotImplementedError 	Raised by abstract methods.

# OSError 	Raised when system operation causes system related error.

# OverflowError 	Raised when result of an arithmetic operation is too large to be represented.

# ReferenceError 	Raised when a weak reference proxy is used to access a garbage collected referent.

# RuntimeError 	Raised when an error does not fall under any other category.

# StopIteration 	Raised by next() function to indicate that there is no further item to be returned by iterator.

# SyntaxError 	Raised by parser when syntax error is encountered.

# IndentationError 	Raised when there is incorrect indentation.

# TabError 	Raised when indentation consists of inconsistent tabs and spaces.

# SystemError 	Raised when interpreter detects internal error.

# SystemExit 	Raised by sys.exit() function.

# TypeError 	Raised when a function or operation is applied to an object of incorrect type.

# UnboundLocalError 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.

# UnicodeError 	Raised when a Unicode-related encoding or decoding error occurs.

# UnicodeEncodeError 	Raised when a Unicode-related error occurs during encoding.

# UnicodeDecodeError 	Raised when a Unicode-related error occurs during decoding.

# UnicodeTranslateError 	Raised when a Unicode-related error occurs during translating.

# ValueError 	Raised when a function gets argument of correct type but improper value.

# ZeroDivisionError 	Raised when second operand of division or modulo operation is zero.


#!-============================================

#! Python Exception Handling - Try, Except and Finally

#!-============================================

# Table of Contents

#     What are exceptions in Python?
#     Catching Exceptions in Python
#     Catching Specific Exceptions in Python
#     Raising Exceptions
#     try...finally

# Built-in Exceptions forces your program to output an ERROR when something in it goes wrong.

# * When these EXCEPTIONS OCCUR,
# ? it causes the current PROCESS to STOP and PASSES it to the CALLING PROCESS... until it is handled.

#!  IF NOT HANDLED, our program will crash.

# EX, if function A calls function B which in turn calls function C and an exception occurs in function C. If it is not handled in C, the exception passes to B and then to A.

# If never handled, an error message is spit out and our program come to a sudden, unexpected halt.
# * Catching Exceptions in Python

# * try:
#    You do your operations here...
#    ...
# * except ExceptionI:
#    If there is ExceptionI, then execute this block.
# * except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ...
# * else:
#    If there is no exception then execute this block.

# todo                                                      TRY

# ? A critical operation which can RAISE EXCEPTION is placed inside the TRY CLAUSE

# todo                                                        EXCEPT

# ? and the code that HANDLES EXCEPTION is written in EXCEPT CLAUSE

# It is up to us, what operations we perform once we have caught the exception.

# Here is a simple example.

# import module sys to get the type of exception
# import sys

import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# Output

# The entry is a
# !Oops! <class 'ValueError'> occured.
# Next entry.

# The entry is 0
# !Oops! <class 'ZeroDivisionError' > occured.
# Next entry.

# The entry is 2
# The reciprocal of 2 is 0.5

# In this program, we loop until the user enters an integer that has a valid reciprocal.
#  The portion that can cause exception is placed inside try block.
# If no exception occurs, except block is skipped and normal flow continues.
# But if any exception occurs, it is caught by the except block.

# Here, we print the name of the exception using ex_info() function inside sys module and ask the user to try again.
# We can see that the values 'a' and '1.3' causes ValueError and '0' causes ZeroDivisionError.

#! Catching Specific Exceptions in Python

# In the above example, we did not mention any exception in the except clause.

# This is not a good programming practice as it will catch all exceptions and handle every case in the same way.
# * We can specify which exceptions an except clause will catch.

# A try clause can have any number of except clause to handle them differently
#  but only one will be executed in case an exception occurs.

# We can use a tuple of values to specify multiple exceptions in an except clause. Here is an example pseudo code.

try:
    # do something
    pass

except ValueError:
    # handle ValueError exception
    pass

except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    pass

except:
    # handle all other exceptions
    pass

#!============================================================

#! Python Custom Exception using assert statement

# todo                                                                                      ASSERT

# Using ASSERT statement you can CREATE OWN EXCEPTION
#  ASSERT check for a condition.

# In Python, users can define such exceptions by creating a new class.
#  This exception class has to be derived, either directly or indirectly, from Exception class.

# ? ASSERTION ERROR  If the condition is not met then it will throw assertion error

# Ex
# Suppose you wrote a function where you take age as an argument.
# You don’t want to let programmers use the function if the age is less the 18.


# def input_age(age):
#     try:
#         assert int(age) > 18
#     except ValueError:
#         return 'ValueError: Cannot convert into int'
#     else:
#         return 'Age is saved successfully'


#!print(input_age('23'))  # This will print
# print(input_age(25))  # This will print
# print(input_age('nothing'))  # This will raise ValueError which is handled
# This will raise AssertionError and the the program collapse
# print(input_age('18'))
# print(input_age(43))  # This will not print

# The output of the following program will be

# Age is saved successfully
# Age is saved successfully
# ValueError: Cannot convert into int

# * Traceback (most recent call last):
#!   File "/home/imtiaz/ExceptionHandling.py", line 13, in
#!     print(input_age('18'))  # This will raise AssertionError the the program collapse
#!   File "/home/imtiaz/ExceptionHandling.py", line 3, in input_age
# !    assert int(age) > 18
# * AssertionError

# todo                                                                                      RAISE

# Exceptions are raised when corresponding errors occur at run time,
# * but we can forcefully raise it using the keyword RAISE.

# We can also optionally pass in value to the exception to clarify why that exception was raised.

#  Most of the built-in exceptions are also derived form this class.

# Your can raise an existing exception by using raise keyword.
#  So, you just simply write raise keyword and then the name of the exception.


def input_ages(age):
    try:
        if(int(age) <= 18):
            raise ZeroDivisionError
    except ValueError:
        return 'ValueError: Cannot convert into int'
    else:
        return 'Age is saved successfully'


# print(input_ages('23'))  # This will execute properly
# print(input_ages('18'))  # This will not execute properly

# The output of the code will be

# Age is saved successfully
# * Traceback (most recent call last):
#!   File "/home/imtiaz/ExceptionHandling.py", line 12, in
#!     print(input_age('18'))  # This will not print
#!   File "/home/imtiaz/ExceptionHandling.py", line 4, in input_age
# *     raise ZeroDivisionError
# * ZeroDivisionError

# Again, in another method we raised the UnderAge exception if the condition is not met. The following code will give you some insight about the idea.


class UnderAge(Exception):
    pass


def verify_age(age):
    if int(age) < 18:
        raise UnderAge
    else:
        print('Age: '+str(age))


# main program
# verify_age(23)  # won't raise exception
# verify_age(17)  # will raise exception

# todo                                                        FINALLY

# * The TRY statement can have an OPTINAL FINALLY clause.
# ? FINALLY is executed no matter what,

# * try:
#    Code block here
#    ...
#    Due to any exception, this code may be skipped!
# * finally:
#    This code block would always be executed.

# For example:

# FINALLY  is generally used to release external resources.
# For example, we may be connected to a remote data center through the network
#  Working with a file or working with a Graphical User Interface (GUI).

# In all these circumstances, we must clean up the resource once used, whether it was successful or not.
#  These actions (closing a file, GUI or disconnecting from network) are performed in the finally clause to guarantee execution.

# Here is an example of file operations to illustrate this.

# * try:
# ?    f = open("test.txt", encoding='utf-8')
#     # perform file operations
# * finally:
# ?     f.close()

# This type of construct makes sure the file is closed even if an exception occurs.


#! Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.

#! try and except

# We will look at some code that opens and writes a file:

try:
    f = open('testfile', 'w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
# .
#! Errors and Exception Handling

# In this lecture we will learn about Errors and Exception Handling in Python. You've definitely already encountered errors by this point in the course. For example:
# In [1]:

# print('Hello)

#   File "<ipython-input-1-db8c9988558c>", line 1
#     print('Hello)
#                  ^
# SyntaxError: EOL while scanning string literal

# Note how we get a SyntaxError, with the further description that it was an EOL (End of Line Error) while scanning the string literal. This is specific enough for us to see that we forgot a single quote at the end of the line. Understanding these various error types will help you debug your code much faster.

# This type of error and description is known as an Exception. Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.

# You can check out the full list of built-in exceptions here. Now let's learn how to handle errors and exceptions in our own code.
#! try and except

# The basic terminology and syntax used to handle errors in Python are the try and except statements. The code which can cause an exception to occur is put in the try block and the handling of the exception is then implemented in the except block of code. The syntax follows:

# try:
#    You do your operations here...
#    ...
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ...
# else:
#    If there is no exception then execute this block.

# We can also just check for any exception with just using except: To get a better understanding of all this let's check out an example: We will look at some code that opens and writes a file:
# In [2]:

# try:
#     f = open('testfile','w')
#     f.write('Test write this')
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()


# Content written successfully

# Now let's see what would happen if we did not have write permission (opening only with 'r'):


try:
    f = open('testfile', 'r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

# In [3]:

# try:
#     f = open('testfile','r')
#     f.write('Test write this')
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()


# Error: Could not find file or read data

# Great! Notice how we only printed a statement! The code still ran and we were able to continue doing actions and running code blocks. This is extremely useful when you have to account for possible input errors in your code. You can be prepared for the error and keep running code, instead of your code just breaking as we saw above.

# We could have also just said except: if we weren't sure what exception would occur. For example:


try:
    f = open('testfile', 'r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

# Error: Could not find file or read data

# ? Now what if we kept wanting to run code after the exception occurred? This is where finally comes in.


# In [4]:

# try:
#     f = open('testfile','r')
#     f.write('Test write this')
# except:
#     # This will check for any exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()

# Error: Could not find file or read data

# Great! Now we don't actually need to memorize that list of exception types! Now what if we kept wanting to run code after the exception occurred? This is where finally comes in.

#! finally

# The finally: block of code will always be run regardless if there was an exception in the try code block. The syntax is:


# * try:
#    Code block here
#    ...
#    Due to any exception, this code may be skipped!
# * finally:
#    This code block would always be executed.

# For example:

try:
    f = open("testfile", "w")
    f.write("Test write statement")
    f.close()
finally:
    print("Always execute finally code blocks")

# try:
#    Code block here
#    ...
#    Due to any exception, this code may be skipped!
# finally:
#    This code block would always be executed.

# For example:
# In [5]:

# try:
#     f = open("testfile", "w")
#     f.write("Test write statement")
#     f.close()
# finally:
#     print("Always execute finally code blocks")


# Always execute finally code blocks

# We can use this in conjunction with except. Let's see a new example that will take into account a user providing the wrong input:


def askint():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")

    finally:
        print("Finally, I executed!")
    print(val)


# In [6]:

# def askint():
#     try:
#         val = int(input("Please enter an integer: "))
#     except:
#         print("Looks like you did not enter an integer!")

#     finally:
#         print("Finally, I executed!")
#     print(val)

# In [7]:


# askint()

# Please enter an integer: 5
# Finally, I executed!
# 5

# askint()


# In [8]:

# askint()


# Please enter an integer: five
# Looks like you did not enter an integer!
# Finally, I executed!

# ---------------------------------------------------------------------------
# UnboundLocalError                         Traceback (most recent call last)
# <ipython-input-8-cc291aa76c10> in <module>()
# ----> 1 askint()

# <ipython-input-6-c97dd1c75d24> in askint()
#       7     finally:
#       8         print("Finally, I executed!")
# ----> 9     print(val)

# UnboundLocalError: local variable 'val' referenced before assignment

# Notice how we got an error when trying to print val (because it was never properly assigned). Let's remedy this by asking the user and checking to make sure the input type is an integer:


def askints():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")
        val = int(input("Try again-Please enter an integer: "))
    finally:
        print("Finally, I executed!")
    print(val)


# askints()

# Please enter an integer: five
#!!Try again-Please enter an integer: four
# !Finally, I executed!

# ---------------------------------------------------------------------------
# !ValueError
# In [9]:

# def askint():
#     try:
#         val = int(input("Please enter an integer: "))
#     except:
#         print("Looks like you did not enter an integer!")
#         val = int(input("Try again-Please enter an integer: "))
#     finally:
#         print("Finally, I executed!")
#     print(val)

# In [10]:

# askint()

# Please enter an integer: five
# Looks like you did not enter an integer!
# Try again-Please enter an integer: four
# Finally, I executed!

# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)

# <ipython-input-9-92b5f751eb01> in askint()
#       2     try:
# ----> 3         val = int(input("Please enter an integer: "))
#       4     except:

# ValueError: invalid literal for int() with base 10: 'five'

# During handling of the above exception, another exception occurred:


# ValueError         Traceback (most recent call last)

# ValueError                                Traceback (most recent call last)

# <ipython-input-10-cc291aa76c10> in <module>()
# ----> 1 askint()

# <ipython-input-9-92b5f751eb01> in askint()
#       4     except:
#       5         print("Looks like you did not enter an integer!")
# ----> 6         val = int(input("Try again-Please enter an integer: "))
#       7     finally:
#       8         print("Finally, I executed!")

#! ValueError: invalid literal for int() with base 10: 'four'

# Hmmm...that only did one check. How can we continually keep checking? We can use a while loop!

def ask_int():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)


# ask_int()

# ValueError: invalid literal for int() with base 10: 'four'

# Hmmm...that only did one check. How can we continually keep checking? We can use a while loop!
# In [11]:

# def askint():
#     while True:
#         try:
#             val = int(input("Please enter an integer: "))
#         except:
#             print("Looks like you did not enter an integer!")
#             continue
#         else:
#             print("Yep that's an integer!")
#             break
#         finally:
#             print("Finally, I executed!")
#         print(val)

# In [12]:

# askint()


# Please enter an integer: five
# Looks like you did not enter an integer!
# Finally, I executed!
# Please enter an integer: four
# Looks like you did not enter an integer!
# Finally, I executed!
# Please enter an integer: 3
# Yep that's an integer!
# Finally, I executed!

# So why did our function print "Finally, I executed!" after each trial, yet it never printed val itself?

# This is because with a try/except/finally clause, any continue or break statements are reserved until after the try clause is completed.

#  This means that even though a successful input of 3 brought us to the else: block, and a break statement was thrown

#  the try clause continued through to finally: before breaking out of the while loop.

# And since print(val) was outside the try clause, the break statement prevented it from running.

# Let's make one final adjustment:


def ask_ints():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")


# ask_ints()

# So why did our function print "Finally, I executed!" after each trial, yet it never printed val itself? This is because with a try/except/finally clause, any continue or break statements are reserved until after the try clause is completed. This means that even though a successful input of 3 brought us to the else: block, and a break statement was thrown, the try clause continued through to finally: before breaking out of the while loop. And since print(val) was outside the try clause, the break statement prevented it from running.

# Let's make one final adjustment:
# In [13]:

# def askint():
#     while True:
#         try:
#             val = int(input("Please enter an integer: "))
#         except:
#             print("Looks like you did not enter an integer!")
#             continue
#         else:
#             print("Yep that's an integer!")
#             print(val)
#             break
#         finally:
#             print("Finally, I executed!")

# In [14]:

# askint()


# Please enter an integer: six
# Looks like you did not enter an integer!
# Finally, I executed!
# Please enter an integer: 6
# Yep that's an integer!
# 6
# Finally, I executed!

# Great! Now you know how to handle errors and exceptions in Python with the try, except, else, and finally notation!
