# https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950
# https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9
# In this tutorial you'll learn how to handle error conditions in Python from a whole system point of view. Error handling is a critical aspect of design, and it crosses from the lowest levels (sometimes the hardware) all the way to the end users. If you don't have a consistent strategy in place, your system will be unreliable, the user experience will be poor, and you'll have a lot of challenges debugging and troubleshooting.

# The key to success is being aware of all these interlocking aspects, considering them explicitly, and forming a solution that addresses each point.
# Status Codes vs. Exceptions

# There are two main error handling models: status codes and exceptions. Status codes can be used by any programming language. Exceptions require language/runtime support.

# Python supports exceptions. Python and its standard library use exceptions liberally to report on many exceptional situations like IO errors, divide by zero, out of bounds indexing, and also some not so exceptional situations like end of iteration (although it is hidden). Most libraries follow suit and raise exceptions.

# That means your code will have to handle the exceptions raised by Python and libraries anyway, so you may as well raise exceptions from your code when necessary and not rely on status codes.
# Quick Example

# Before diving into the inner sanctum of Python exceptions and error handling best practices, let's see some exception handling in action:
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29


def f():

    return 4 / 0


def g():

    raise Exception("Don't call us. We'll call you")


def h():

    try:

        f()

    except Exception as e:

        print(e)

    try:

        g()

    except Exception as e:

        print(e)

# Here is the output when calling h():
# 1
# 2
# 3
# 4
# 5

# h()

# division by zero

# Don't call us. We'll call you
# Python Exceptions

# Python exceptions are objects organized in a class hierarchy.

# Here is the whole hierarchy:
# 001
# 002
# 003
# 004
# 005
# 006
# 007
# 008
# 009
# 010
# 011
# 012
# 013
# 014
# 015
# 016
# 017
# 018
# 019
# 020
# 021
# 022
# 023
# 024
# 025
# 026
# 027
# 028
# 029
# 030
# 031
# 032
# 033
# 034
# 035
# 036
# 037
# 038
# 039
# 040
# 041
# 042
# 043
# 044
# 045
# 046
# 047
# 048
# 049
# 050
# 051
# 052
# 053
# 054
# 055
# 056
# 057
# 058
# 059
# 060
# 061
# 062
# 063
# 064
# 065
# 066
# 067
# 068
# 069
# 070
# 071
# 072
# 073
# 074
# 075
# 076
# 077
# 078
# 079
# 080
# 081
# 082
# 083
# 084
# 085
# 086
# 087
# 088
# 089
# 090
# 091
# 092
# 093
# 094
# 095
# 096
# 097
# 098
# 099
# 100

# BaseException

#  +-- SystemExit

#  +-- KeyboardInterrupt

#  +-- GeneratorExit

#  +-- Exception

#       +-- StopIteration

#       +-- StandardError

#       |    +-- BufferError

#       |    +-- ArithmeticError

#       |    |    +-- FloatingPointError

#       |    |    +-- OverflowError

#       |    |    +-- ZeroDivisionError

#       |    +-- AssertionError

#       |    +-- AttributeError

#       |    +-- EnvironmentError

#       |    |    +-- IOError

#       |    |    +-- OSError

#       |    |         +-- WindowsError (Windows)

#       |    |         +-- VMSError (VMS)

#       |    +-- EOFError

#       |    +-- ImportError

#       |    +-- LookupError

#       |    |    +-- IndexError

#       |    |    +-- KeyError

#       |    +-- MemoryError

#       |    +-- NameError

#       |    |    +-- UnboundLocalError

#       |    +-- ReferenceError

#       |    +-- RuntimeError

#       |    |    +-- NotImplementedError

#       |    +-- SyntaxError

#       |    |    +-- IndentationError

#       |    |         +-- TabError

#       |    +-- SystemError

#       |    +-- TypeError

#       |    +-- ValueError

#       |         +-- UnicodeError

#       |              +-- UnicodeDecodeError

#       |              +-- UnicodeEncodeError

#       |              +-- UnicodeTranslateError

#       +-- Warning

#            +-- DeprecationWarning

#            +-- PendingDeprecationWarning

#            +-- RuntimeWarning

#            +-- SyntaxWarning

#            +-- UserWarning

#            +-- FutureWarning

#   +-- ImportWarning

#   +-- UnicodeWarning

#   +-- BytesWarning


# There are several special exceptions that are derived directly from BaseException, like SystemExit, KeyboardInterrupt and GeneratorExit. Then there is the Exception class, which is the base class for StopIteration, StandardError and Warning. All the standard errors are derived from StandardError.

# When you raise an exception or some function you called raises an exception, that normal code flow terminates and the exception starts propagating up the call stack until it encounters a proper exception handler. If no exception handler is available to handle it, the process (or more accurately the current thread) will be terminated with an unhandled exception message.
# Raising Exceptions

# Raising exceptions is very easy. You just use the raise keyword to raise an object that is a sub-class of the Exception class. It could be an instance of Exception itself, one of the standard exceptions (e.g. RuntimeError), or a subclass of Exception you derived yourself. Here is a little snippet that demonstrates all cases:
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31

# Raise an instance of the Exception class itself

# raise Exception('Ummm... something is wrong')


# Raise an instance of the RuntimeError class

# raise RuntimeError('Ummm... something is wrong')


# Raise a custom subclass of Exception that keeps the timestamp the exception was created

# from datetime import datetime


class SuperError(Exception):

    def __init__(self, message):

        Exception.__init__(message)

        self.when = datetime.now()


# raise SuperError('Ummm... something is wrong')
# Catching Exceptions

# You catch exceptions with the except clause, as you saw in the example. When you catch an exception, you have three options:

#     Swallow it quietly (handle it and keep running).
#     Do something like logging, but re-raise the same exception to let higher levels handle.
#     Raise a different exception instead of the original.

# Swallow the Exception

# You should swallow the exception if you know how to handle it and can fully recover.

# For example, if you receive an input file that may be in different formats (JSON, YAML), you may try parsing it using different parsers. If the JSON parser raised an exception that the file is not a valid JSON file, you swallow it and try with the YAML parser. If the YAML parser failed too then you let the exception propagate out.
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15

# import json

# import yaml


def parse_file(filename):

    try:

        return json.load(open(filename))

    except json.JSONDecodeError

       return yaml.load(open(filename))

# Note that other exceptions (e.g. file not found or no read permissions) will propagate out and will not be caught by the specific except clause. This is a good policy in this case where you want to try the YAML parsing only if the JSON parsing failed due to a JSON encoding issue.

# If you want to handle all exceptions then just use except Exception. For example:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


def print_exception_type(func, *args, **kwargs):

    try:

        return func(*args, **kwargs)

    except Exception as e:

        print type(e)

# Note that by adding as e, you bind the exception object to the name e available in your except clause.
# Re-Raise the Same Exception

# To re-raise, just add raise with no arguments inside your handler. This lets you perform some local handling, but still lets upper levels handle it too. Here, the invoke_function() function prints the type of exception to the console and then re-raises the exception.
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11


def invoke_function(func, *args, **kwargs):

    try:

        return func(*args, **kwargs)

    except Exception as e:

        print type(e)

        raise
# Raise a Different Exception

# There are several cases where you would want to raise a different exception. Sometimes you want to group multiple different low-level exceptions into a single category that is handled uniformly by higher-level code. In order cases, you need to transform the exception to the user level and provide some application-specific context.
# Finally Clause

# Sometimes you want to ensure some cleanup code executes even if an exception was raised somewhere along the way. For example, you may have a database connection that you want to close once you're done. Here is the wrong way to do it:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# def fetch_some_data():

#     db = open_db_connection()

#     query(db)

#     close_db_Connection(db)

# If the query() function raises an exception then the call to close_db_connection() will never execute and the DB connection will remain open. The finally clause always executes after a try all exception handler is executed. Here is how to do it correctly:
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15


def fetch_some_data():

    db = None

    try:

        db = open_db_connection()

        query(db)

    finally:

        if db is not None:

            close_db_connection(db)

# The call to open_db_connection() may not return a connection or raise an exception itself. In this case there is no need to close the DB connection.

# When using finally, you have to be careful not to raise any exceptions there because they will mask the original exception.
# Context Managers

# Context managers provide another mechanism to wrap resources like files or DB connections in cleanup code that executes automatically even when exceptions have been raised. Instead of try-finally blocks, you use the with statement. Here is an example with a file:
# 1
# 2
# 3
# 4
# 5


def process_file(filename):

    with open(filename) as f:

        process(f.read())

# Now, even if process() raised an exception, the file will be closed properly immediately when the scope of the with block is exited, regardless of whether the exception was handled or not.
# Logging

# Logging is pretty much a requirement in non-trivial, long-running systems. It is especially useful in web applications where you can treat all exceptions in a generic way: Just log the exception and return an error message to the caller.

# When logging, it is useful to log the exception type, the error message, and the stacktrace. All this information is available via the sys.exc_info object, but if you use the logger.exception() method in your exception handler, the Python logging system will extract all the relevant information for you.

# This is the best practice I recommend:
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17

# import logging

# logger = logging.getLogger()


def f():

    try:

        flaky_func()

    except Exception:

        logger.exception()

        raise

# If you follow this pattern then (assuming you set up logging correctly) no matter what happens you'll have a pretty good record in your logs of what went wrong, and you'll be able to fix the issue.

# If you re-raise, make you sure you don't log the same exception over and over again at different levels. It is a waste, and it might confuse you and make you think multiple instances of the same issue occurred, when in practice a single instance was logged multiple times.

# The simplest way to do it is to let all exceptions propagate (unless they can be handled confidently and swallowed earlier) and then do the logging close to the top level of your application/system.
# Sentry

# Logging is a capability. The most common implementation is using log files. But, for large-scale distributed systems with hundreds, thousands or more servers, this is not always the best solution.

# To keep track of exceptions across your whole infrastructure, a service like sentry is super helpful. It centralizes all exception reports, and in addition to the stacktrace it adds the state of each stack frame (the value of variables at the time the exception was raised). It also provides a really nice interface with dashboards, reports and ways to break down the messages by multiple projects. It is open source, so you can run your own server or subscribe to the hosted version.
# Dealing With Transient Failure

# Some failures are temporary, in particular when dealing with distributed systems. A system that freaks out at the first sign of trouble is not very useful.

# If your code is accessing some remote system that is not responding, the traditional solution is timeouts, but sometimes not every system is designed with timeouts. Timeouts are not always easy to calibrate as conditions change.

# Another approach is to fail fast and then retry. The benefit is that if the target is responding fast then you don't have to spend a lot of time in sleep condition and can react immediately. But if it failed, you can retry multiple times until you decide it is really unreachable and raise an exception. In the next section, I'll introduce a decorator that can do it for you.
# Helpful Decorators

# Two decorators that can help with error handling are the @log_error, which logs an exception and then re-raises it, and the @retry decorator, which will retry calling a function several times.
# Error Logger

# Here is a simple implementation. The decorator excepts a logger object. When it decorates a function and the function is invoked, it will wrap the call in a try-except clause, and if there was an exception it will log it and finally re-raise the exception.
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23


def log_error(logger)

   def decorated(f):

        @functools.wraps(f)
        def wrapped(*args, **kwargs):

            try:

                return f(*args, **kwargs)

            except Exception as e:

                if logger:

                    logger.exception(e)

                raise

        return wrapped

    return decorated

# Here is how to use it:
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11

# import logging

# logger = logging.getLogger()


@log_error(logger)
def f():

    raise Exception('I am exceptional')

Retrier

# Here is a very good implementation of the @retry decorator.
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59
# 60
# 61
# 62
# 63
# 64
# 65
# 66
# 67
# 68
# 69
# 70
# 71
# 72
# 73
# 74
# 75
# 76
# 77
# 78
# 79
# 80
# 81

# import time

# import math


# Retry decorator with exponential backoff

def retry(tries, delay=3, backoff=2):
    '''Retries a function or method until it returns True.



    delay sets the initial delay in seconds, and backoff sets the factor by which

    the delay should lengthen after each failure. backoff must be greater than 1,

    or else it isn't really a backoff. tries must be at least 0, and delay

    greater than 0.'''


    if backoff <= 1:

        raise ValueError("backoff must be greater than 1")


    tries = math.floor(tries)

    if tries < 0:

        raise ValueError("tries must be 0 or greater")


    if delay <= 0:

        raise ValueError("delay must be greater than 0")


    def deco_retry(f):

        def f_retry(*args, **kwargs):

            mtries, mdelay = tries, delay  # make mutable


            rv = f(*args, **kwargs)  # first attempt

            while mtries > 0:

                if rv is True:  # Done on success

                    return True


                mtries -= 1      # consume an attempt

                time.sleep(mdelay)  # wait...

                mdelay *= backoff  # make future wait longer


                rv = f(*args, **kwargs)  # Try again


            return False  # Ran out of tries :-(


        return f_retry  # true decorator -> decorated function

    return deco_retry  # @retry(arg[, ...]) -> true decorator
# Conclusion

# Error handling is crucial for both users and developers. Python provides great support in the language and standard library for exception-based error handling. By following best practices diligently, you can conquer this often neglected aspect.
