# 8. Errors and Exceptions
#! 8. Errors and Exceptions

# There are (at least) two distinguishable kinds of errors:
#           1. Syntax Errors
#           2. Exceptions.

#! 8.1. Syntax Errors

# SYNTAX ERRORS alsoknown as (aka) PARSING ERROS:
# >>>

# >>> while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
#                    ^
# SyntaxError: invalid syntax

# The PARSER REPEATS the offending line and displays a LITTLE ARROW pointing at the EARLIEST POINT in the line where the ERROR was DETECTED.
#
# The error is caused by (or at least detected at) the token preceding the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing before it.
#
# File name and line number are printed so you know where to look in case the input came from a script.

#! 8.2. Exceptions

# Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.
#
# * EXCEPTIONS == Errors detected during execution and are not unconditionally fatal: you will soon learn how to handle them in Python programs.

# NOTE MOST EXCEPTIONS are NOT HANDLED by PROGRAMS, however, and result in error messages as shown here:

# ===================================================

# >>> 10 * (1/0)
# NOTE Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>

# STACK TRACEBACK = part of the error message shows the CONTEXT where the exception happened.
#
# In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input


# NOTE ZeroDivisionError: division by zero

# ? EXCEPTION TYPE ==  The string printed as the NAME of the BUILT-IN EXCEPTION that occurred.

# This is true for all built-in exceptions, but need NOT TRUE for USER-DEFINED EXCEPTIONS (although it is a useful convention).

# STANDARD EXCEPTION NAMES are built-in IDENTIFIERS (not RESERVED KW)


# ===================================================

# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ? NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last): STACK TRACEBACK
#   File "<stdin>", line 1, in <module>
# ?TypeError: Can't convert 'int' object to str implicitly

# ? The LAST LINE of the error message indicates what happened.

# Exceptions come in DIFFERNT TYPES types, and the type is printed as part of the message:
#  ZeroDivisionError,
#  NameError
#  TypeError.

#! Built-in Exceptions lists the built-in exceptions and their meanings.

# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

#! 8.3. Handling Exceptions

# It is possible to write programs that handle selected exceptions.
#
#  Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports);
#
# NOTE that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

# ? EX >>>

# >>> while True:
# ...     try:
# ...         x = int(input("Please enter a number: "))
# ...         break
# ...     except ValueError:
# ...         print("Oops!  That was no valid number.  Try again...")
# ...

#!TRY STATEMENT

#  statement works as follows.

#     First, the try clause (the statement(s) between the try and except keywords) is executed.

#     IF NO EXCEPTION occurs, the EXCEPT CALUSE is SKIPPED and execution of the try statement is finished.

#     If an EXCEPTION occurs during execution of the TRY CLAUSE, the rest of the clause is skipped.
#
# Then IF its TYPE MATCHES the EXCEPTION NAMED after the EXCEPT KW,
# the EXCEPT clause is executed, then execution continues AFTER the try statement.

#    IF an exception occurs which DOES NOT MATCH the exception named in the except clause, it is passed on to outer try statements;

# UNHANDLED EXCEPTION == IF NO HANDLER is found, execution stops with a message as shown above.

# A try statement may have  MULTIPLE (more than one) EXCEPT CLAUSE clause, to specify handlers for different exceptions.

# At most one handler will be executed.
#
# Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement.
#
# An EXCEPT CLAUSE may name MULTIPLE EXCEPTIONS  as a parenthesized TUPLE
# NOTE for example:

# ... except (RuntimeError, TypeError, NameError):
# ...     pass

# ? For example, the following code will print B, C, D in that order:

import os


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# NOTE # A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class).
#

# NOTE that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

# The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well):

# import sys

# ?try ex with import os vs import sys?
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", os.sys.exc_info()[0])
#     raise

# The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

# for arg in os.sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

# When an exception occurs, it may have an associated value, also known as the exception’s argument. The presence and type of the argument depend on the exception type.

# The except clause may specify a VARIABLE AFTER the EXCEPTION NAME.
# VARIABLE is bound to an exception instance with the arguments stored in
# ?instance.args.

# For convenience, the exception instance defines
# ? __str__()
# so the arguments can be printed directly WITHOUT having to reference .args.

# One may also instantiate an exception first before raising it and add any attributes to it as desired.

# NOTE EX
# >>> try:
# ...     raise Exception('spam', 'eggs')
# ... except Exception as inst:
# ...     print(type(inst))    # the exception instance
# ...     print(inst.args)     # arguments stored in .args
# ...     print(inst)          # __str__ allows args to be printed directly,
# ...                          # but may be overridden in exception subclasses
# ...     x, y = inst.args     # unpack args
# ...     print('x =', x)
# ...     print('y =', y)
# NOTE ...OUTPUT
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

# If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.

# IF EXCEPTION HANDLERS occur IMMEDIATELY in the TRY CLAUSE, but also if they occur inside functions that are called (even indirectly) in the try clause.
#
#  For example:

# NOTE EX >>>

# >>> def this_fails():
# ...     x = 1/0
# ...
# >>> try:
# ...     this_fails()
# ... except ZeroDivisionError as err:
# ...     print('Handling run-time error:', err)
# NOTE OUTPUT ...
# Handling run-time error: division by zero

#!8.4. Raising Exceptions

# The RAISE STATEMENT allows the programmer to FORCE a SPECIFIED EXCEPTION to occur. For example:

# NOTE >>>

# >>> raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: HiThere

# The sole ARG to raise indicates the exception to be raised. This MUST be either an EXCEPTION INSTANCE or an EXCEPTION CLASS (a class that derives from Exception).

#  If an EXCEPTION CLASS is passed, it will be implicitly instantiated by calling its CONSTRUCTOR with NO ARGS:

# raise ValueError  # shorthand for 'raise ValueError()'

# ?EX
#  If you need to determine whether an EXCEPTION was RAISED but DONT intend to HANDLE it...
#  a simpler form of the raise statement allows you to re-raise the exception:

# NOTE EX >>>

# >>> try:
# ...     raise NameError('HiThere')
# ... except NameError:
# ...     print('An exception flew by!')
# ...     raise
# ...NOTE OUTPUT
# An exception flew by!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# NameError: HiThere

#! 8.5. User-defined Exceptions

# GENERALLY Programs may name their own exceptions by creating a new EXCEPTION CLASS (see Classes for more about Python classes). Exceptions derived either DIRECTLY or INDIRECTLY.

# Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.
#
# NOTE BEST PRACTCE for errors when creating a MODULE is to create a BASE CLASS for EXCEPTIONS defined by that module, and subclass that to create specific exception classes for different error conditions:


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

# Many standard modules define their own exceptions to report errors that may occur in functions they define.

#! 8.6. Defining Clean-up Actions

# * FINALLY CLAUSE ==  OPTIONAL CLAUSE of the TRY STATEMENT which is intended to define clean-up actions that MUST be EXECUTED under ALL circumstances.
#
# ? EX

# NOTE EX >>>
# >>> try:
# ...     raise KeyboardInterrupt
# ... finally:
# ...     print('Goodbye, world!')
# NOTE OUTPUT ...
# Goodbye, world!
# KeyboardInterrupt
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>

# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.
#
# When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in an except or else clause), it is re-raised after the finally clause has been executed.
#
# The finally clause is also executed “on the way out” when any other clause of the try statement is left via a break, continue or return statement.
#
# ?EX:

# NOTE EX >>>

# >>> def divide(x, y):
# ...     try:
# ...         result = x / y
# ...     except ZeroDivisionError:
# ...         print("division by zero!")
# ...     else:
# ...         print("result is", result)
# ...     finally:
# ...         print("executing finally clause")
# ...
# >>> divide(2, 1)
# result is 2.0
# executing finally clause
# >>> divide(2, 0)
# division by zero!
# executing finally clause
# >>> divide("2", "1")
# executing finally clause
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in divide
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

# As you can see, the finally clause is executed in any event.
#
# The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

# NOTE REAL WORLD applications the FINALLY CLAUSE is useful for releasing EXTERNAL RESOURCES (such as FILES or NETWORK CONNECTIONS), regardless of whether the use of the resource was successful.

#! 8.7. Predefined Clean-up Actions

# Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed.
#
# ? EX
# code tries to open a file and print its contents to the screen.


# for line in open("myfile.txt"):
#     print(line, end="")


# The PROBLEM with this code is that it LEAVES FILE OPEN for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications.
#
# ?EX
# The WITH STATEMENT allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines.
#
# Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.
