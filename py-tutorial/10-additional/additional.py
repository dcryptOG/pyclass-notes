# Python Iterators

#!                                                      ITERATORS

# What are iterators in Python?

# *ITERATIORS = are objects that can be iterated upon which will return data, one element at a time.

# An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

# Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.


# ! 2 special methods,

# Build your own iterator using 2 special methods:
# ? __iter__()
# ? __next__(),

# Technically speaking, Python iterator object must implement collectively called the iterator protocol.

# * iter()
# (which in turn calls the __iter__() method) returns an iterator from them.

# Iterating Through an Iterator in Python

# *next()
# To manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise StopIteration.
#
# NOTE EX

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# prints 4
print(next(my_iter))

# prints 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# prints 0
print(my_iter.__next__())

# prints 3
print(my_iter.__next__())

# This will raise error, no items left
# next(my_iter)


# A more elegant way of automatically iterating is by using the for loop. Using this, we can iterate over any object that can return an iterator, for example list, string, file etc.

#     >>> for element in my_list:
#     ...     print(element)
#     ...
#     4
#     7
#     0
#     3


# As we see in the above example, the for loop was able to iterate automatically through the list. In fact the for loop can iterate over any iterable.
#
# ?  Let's take a closer look at how the for loop is actually implemented in Python.

#     for element in iterable:
#         # do something with element

# NOTE Is actually implemented as.

#     # create an iterator object from that iterable
#     iter_obj = iter(iterable)
#     # infinite loop
#     while True:
#         try:
#             # get the next item
#             element = next(iter_obj)
#             # do something with element
#         except StopIteration:
#             # if StopIteration is raised, break from loop
#             break

# So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

# ? This for loop is actually an infinite while loop.

# Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. Note that any other kind of exception will pass through.

# ==========================#==========================

#! Building Your Own Iterator in Python

# Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().

# ? The __iter__() method returns the iterator object itself. If required, some initialization can be performed.

# ? The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

# NOTE EX

#  that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# Now we can create an iterator and iterate through it as follows.


a = PowTwo(4)
i = iter(a)
print(next(i))
#     1
#     >>> next(i)
#     2
#     >>> next(i)
#     4
#     >>> next(i)
#     8
#     >>> next(i)
#     16
#     >>> next(i)
#     Traceback (most recent call last):
#     ...
#     StopIteration

# We can also use a for loop to iterate over our iterator class.

#     >>> for i in PowTwo(5):
#     ...     print(i)
#     ...
#     1
#     2
#     4
#     8
#     16
#     32

#! Python Infinite Iterators

# It is not necessary that the item in an iterator object has to exhaust. There can be infinite iterators (which never ends). We must be careful when handling such iterator.

# Here is a simple example to demonstrate infinite iterators.

# The built-in function iter() can be called with two arguments where the first argument must be a callable object (function) and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel.

#     >>> int()
#     0
#     >>> inf = iter(int,1)
#     >>> next(inf)
#     0
#     >>> next(inf)
#     0

# We can see that the int() function always returns 0. So passing it as iter(int,1) will return an iterator that calls int() until the returned value equals 1. This never happens and we get an infinite iterator.

# We can also built our own infinite iterators. The following iterator will, theoretically, return all the odd numbers.


class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

# A sample run would be as follows.

#     >>> a = iter(InfIter())
#     >>> next(a)
#     1
#     >>> next(a)
#     3
#     >>> next(a)
#     5
#     >>> next(a)
#     7

# And so on...

# Be careful to include a terminating condition, when iterating over these type of infinite iterators.

# The advantage of using iterators is that they save resources. Like shown above, we could get all the odd numbers without storing the entire number system in memory. We can have infinite items (theoretically) in finite memory.

# ==========================#==========================

#!                                                       GENERATORS

# There's an easier way to create iterators in Python. To learn more visit: Python generators using yield.

# Create iterations easily using Python generators, how is it different from iterators and normal functions, and why you should use it.

# What are generators in Python?

# There is a lot of overhead in building an iterator in Python; we have to implement a class with __iter__() and __next__() method, keep track of internal states, raise StopIteration when there was no values to be returned etc.

# This is both lengthy and counter intuitive. Generator comes into rescue in such situations.

# Python generators are a simple way of creating iterators. All the overhead we mentioned above are automatically handled by generators in Python.

# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# ? How to create a generator in Python?

# It is fairly simple to create a generator in Python. It is as easy as defining a normal function with yield statement instead of a return statement.

# If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

# The difference is that,
#  a return statement TERMINATES a function entirely,
# yield statement PAUSES the function saving all its states and later continues from there on successive calls.


print('#==========================#==========================')
# ? Differences between Generator function and a Normal function

# Here is how a generator function differs from a normal function.

#     Generator function contains ONE or MORE YIELD STATEMENT.
#     WHEN CALLED, it returns an object (iterator) but DOES NOT start execution immediately.
#     Methods like __iter__() and __next__() are IMPLEMENTED AUTOMATICALLY. So we can iterate through the items using next().
#     ONCE FUNCTION YIELDS, the function is PAUSED and the control is transferred to the caller.
#     Local variables and their states are remembered between successive calls.
#     FINALLY, when the function terminates, StopIteration is raised automatically on further calls.

# NOTE EX

# illustrate all of the points stated above. We have a generator function named my_gen() with several yield statements.

# A simple generator function


def my_gen():
    n = 1
    print(f'\nThis is printed first\n {n}')
    # Generator function contains yield statements
    yield n

    n += 1
    print(f'This is printed second\n {n}')
    yield n

    n += 1
    print(f'This is printed at last\n {n}')
    yield n

# An interactive run in the interpreter is given below. Run these in the Python shell to see the output.

#     >>> # It returns an object but does not start execution immediately.


a = my_gen()

# We can iterate through the items using next().

next(a)
#     This is printed first
#     1

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.

next(a)
#     This is printed second
#     2
next(a)
#     This is printed at last
#     3
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

# NOTE    >>> next(a)
# NOTE    Traceback (most recent call last):
#     ...
#     StopIteration
#     >>> next(a)
#     Traceback (most recent call last):
#     ...
#     StopIteration

# One interesting thing to note in the above example is that, the value of variable n is remembered between each call.

# Unlike normal functions, the local variables are not destroyed when the function yields.
#
# Furthermore, the GENERATOR OBJ can be ITERATED ONLY ONCE.

# RESTART PROCESS we need to create another generator object using something like a = my_gen().

# NOTE: One final thing to note is that we can use generators with for loops DIRECTLY. Because, a for loop takes an iterator and iterates over it using next() function. It automatically ends when StopIteration is raised.

print('\nExample equivalent')
# A simple generator function


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

# When you run the program, the output will be:

# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3

print('The above example is of less use and we studied it just to get an idea of what was happening in the background.\n#==========================#==========================\n')

#! Python Generators with a Loop

# Normally, generator functions are implemented with a loop having a suitable terminating condition.

# NOTE
# a generator that reverses a string.
print('Python Generators with a Loop')


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
    print(char)

# In this example, we use range() function to get the index in reverse order using the for loop.

# It turns out that this generator function not only works with string, but also with other kind of iterables like list, tuple etc.

#! Python Generator Expression

# Simple generators can be easily created on the fly using GENERATOR EXPRESSIONS. It makes building generators easy.

# NOTE Same as LAMBDA function creates an ANONYMOUS function,
# ? GENERATOR EXPRESSIONS creates an ANONYMOUS generator function.

#! SYNTAX for generator expression
# Similar to a LIST COMPREHENSION, but the square brackets
# ? are replaced with ROUND PARENTHESIS.

# NOTE The major difference between a list comprehension and a generator expression
# list comprehension produces the entire list,
# ? GENERATOR EXPRESSION produces ONE ITEM AT A TIME.

# For this reason, a GENERATOR EXPRESSION is much MORE MEMORY EFFICIENT than an equivalent list comprehension.

print('\nGENERATOR EXPRESSION vs LIST COMPREHENSION ex')

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print('\nList comprehension', [x**2 for x in my_list])

print('\nUsing GENERATOR EXPRESSION')
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x**2 for x in my_list))

# Generator expression did not produce the required result immediately. Instead, it returned a generator object with produces items on demand.

# Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
# next(a)

print('\nGENERATOR EXPRESSION can be used INSIDE FUNCTIONS. ')

# ? GENERATOR EXPRESSION can be used INSIDE FUNCTIONS.
# The ROUND PARENTHESIS can be dropped.

print(sum(x**2 for x in my_list))
#     146
print(max(x**2 for x in my_list))
#     100

#! Why generators are used in Python?

# There are several reasons which make generators an attractive implementation to go for.

# ? 1. Easy to Implement

# Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.

# NOTE EX to implement a sequence of power of 2's using iterator class.


class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result

# This was lengthy. Now lets do the same using a generator function.


def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


print('\n', PowTwo(5), '\n', PowTwoGen(5))

# Since, generators keep track of details automatically, it was concise and much cleaner in implementation.

# ? 2. Memory Efficient

# A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large.

# Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

# ? 3. Represent Infinite Stream

# Generators are excellent medium to represent an infinite stream of data.

#   Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.

# NOTE EX can generate all the even numbers (at least in theory).


def all_even():
    n = 0
    while True:
        yield n
        n += 2


print('\n', all_even())

# ? 4. Pipelining Generators

# Generators can be used to pipeline a series of operations.

# This is best illustrated using an example. Suppose we have a log file from a famous fast food chain. The log file has a column (4th column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.

# Assume everything is in string and numbers that are not available are marked as 'N/A'. A generator implementation of this could be as follows.

#     with open('sells.log') as file:
#         pizza_col = (line[3] for line in file)
#         per_hour = (int(x) for x in pizza_col if x != 'N/A')
#         print("Total pizzas sold = ",sum(per_hour))

# This pipelining is efficient and easy to read (and yes, a lot cooler!).


# ==========================#==========================

#!                                                      CLOSURES

print('\n#==========================#==========================\n\t\tCLOSURES\n')

# Nonlocal variable in a nested function

# Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.

# * NESTED FUNCTION =  function defined inside another function .
# Nested functions can access variables of the enclosing scope.

# ? Non-local variables are READ-ONLY by DEFAULT

# ? TO MODIFY must declare explicitly as non-local (using NONLOCAL KEYWORD)

# ==========================#==========================

# NOTE EX of a nested function accessing a non-local variable.

print('Nested Function EX')


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()


# We execute the function
# Output: Hello
print_msg("Hello")

# We can see that the NESTED FUNCTION printer() was able to access the NON-LOCAL VAR msg of the enclosing function.

#! Defining a Closure Function

# In the example above, what would happen if the last line of the function print_msg() returned the printer() function instead of calling it? This means the function was defined as follows.

print('\nEX Nested Function w/ return')


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # this got changed


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()

# That's unusual.

# The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. On calling another(), the message was still remembered although we had already finished executing the print_msg() function.

# *CLOSURE = technique by which some data ("Hello") gets attached to the code

# This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

# Try running the following in the Python shell to see the output.

#     >>> del print_msg
#     >>> another()
#     Hello
#     >>> print_msg("Hello")
#     Traceback (most recent call last):
#     ...
#     NameError: name 'print_msg' is not defined

#! When do we have a closure?

#  CLOSURE when a nested function references a value in its enclosing scope.

# * CRITERIA that must be met to create closure:

# ?     1.   We must have a NESTED FUNCTION (function inside a function).

# ?     2.   The nested function must refer to a VALUE defined in the ENCLOSING FUNCTION

# ?     3.   The enclosing function must RETURN the NESTED FUNCTIONM.

#! When to use closures?

# So what are closures good for?

# Closures can AVOID the use of GLOBAL VALUES and provides some form of DATA HIDING. It can also provide an object oriented solution to the problem.

# CLOSURES ideal when there are FEW METHODS (ONE in MOST CASES) to be implemented in a class, closures can provide an alternate and more elegant solutions.
#
# When the number of METHODS and ATTRIBUTES gets larger, better implement a class.

# NOTE EX where a closure might be more preferable than defining a class and making objects. But the preference is all yours.
print('\nEX CLOSURE \nAll Function Objects have a __closure__ attribute ')


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

# DECORATORS in Python make an extensive use of closures as well.

# The values that get enclosed in the closure function can be found out.

# All function objects have a __closure__ attribute that returns a TUPLE of cell objects if it is a CLOSURE FUNCTION.
#
# Referring to the example above, we know times3 and times5 are CLOSURE FUNCTIONS.

#     >>> make_multiplier_of.__closure__
print('\n', times3.__closure__)
#     (<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)

# The cell object has the attribute cell_contents which stores the closed value.

print(times3.__closure__[0].cell_contents)
#     3
print(times5.__closure__[0].cell_contents)
#     5

# ==========================#==========================

#! DECORATORS

# A decorator takes in a function, adds some functionality and returns it.

# What are decorators in Python?

# Python has an interesting feature called decorators to add functionality to an existing code.

# This is also called METAPROGRAMMING as a part of the program tries to modify another part of the program at COMPILE TIME.

# Prerequisites for learning decorators

# In order to understand about decorators, we must first know a few basic things in Python.

# We must be comfortable with the fact that, everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. Functions are no exceptions, they are objects too (with attributes). Various different names can be bound to the same function object.

# NOTE EX
print('\n#==========================#==========================')
print('\tDECORATORS\nEX Decorator')


def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")

# When you run the code, both functions first and second gives same output. Here, the names first and second refer to the same function object.

# Now things start getting weirder.

# Functions can be passed as arguments to another function. If you have used functions like map, filter and reduce in Python, then you already know about this.

# * DECORATOR =  takes in a function, adds some functionality and returns it.

# *HIGHER ORDER FUNCTIONS = function that take other functions as arguments.

# NOTE EX

print('\n')


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

# We invoke the function as follows.


print(operate(inc, 3))
#     4
print(operate(dec, 3))
#     2

# ==========================#==========================
print('\n')
# Furthermore, a function can return another function.


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"

print(new())

# Here, is_returned() is a nested function which is defined and returned, each time we call is_called().

# ==========================#==========================

# Functions and methods are called callable as they can be called.

# In fact, any object which implements the special method __call__() is termed callable. So, in the most basic sense, a decorator is a CALLABLE that returns a CALLABLE.
print('\n')


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
# When you run the following codes in shell,


print(ordinary())
#     I am ordinary
#     >>> # let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

#     I got decorated
#     I am ordinary

# In the example shown above, make_pretty() is a decorator. In the assignment step.

#     pretty = make_pretty(ordinary)

# The function ordinary() got decorated and the returned function was given the name pretty.

# We can see that the decorator function added some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).

# ==========================#==========================

# Generally, we decorate a function and reassign it as,

#     ordinary = make_pretty(ordinary).

# This is a common construct and for this reason, Python has a syntax to simplify this.

# ? @ symbol along with the name of the DECORATOR FUNCTION
# place it above the definition of the function to be decorated.

# NOTE EX

#!     @make_pretty
#!     def ordinary():
#!         print("I am ordinary")

# ? is equivalent to

#!     def ordinary():
#!         print("I am ordinary")
#!     ordinary = make_pretty(ordinary)

# This is just a syntactic sugar to implement decorators.  The above decorator was simple and it only worked with functions that did not have any parameters.


# ==========================#==========================

#! Decorating Functions with Parameters

# What if we had functions that took in parameters like below?

def divide(a, b):
    return a/b

# This function has two parameters, a and b. We know, it will give error if we pass in b as 0.


divide(2, 5)
#     0.4
# NOTE     >>> divide(2,0)
# NOTE     Traceback (most recent call last):
#     ...
# NOTE     ZeroDivisionError: division by zero

print("Now let's make a decorator to check for this case that will cause the error.")


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

# This new implementation will return None if the error condition arises.


divide(2, 5)
#     I am going to divide 2 and 5
#     0.4
divide(2, 0)
#     I am going to divide 2 and 0
#     Whoops! cannot divide

# In this manner we can decorate functions that take parameters.

# A keen observer will notice that parameters of the nested inner() function inside the decorator is same as the parameters of functions it decorates.
#
#  Taking this into account, now we can make general decorators that work with any number of parameter.

# Done as function(*args, **kwargs). In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments.

# NOTE EX


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

#! Chaining Decorators in Python

# Multiple decorators can be chained in Python.

# This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place the decorators above the desired function.


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

# This will give the output.


# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************

# * SYNTAX

#!     @star
#!     @percent
#!     def printer(msg):
#!         print(msg)

# is equivalent to

#!     def printer(msg):
#!         print(msg)
#!     printer = star(percent(printer))

# ?The order in which we chain decorators matter.
# If we had reversed the order as,

#     @percent
#     @star
#     def printer(msg):
#         print(msg)

# The execution would take place as,
# NOTE OUTPID OPPOSITE

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************
# Hello
# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# ==========================#==========================

#!                          @PROPERTY

# Python @property
# @property; pythonic way to use GETTERS and SETTERS.

# NOTE EX

# Let us assume that you decide to make a class that could store the temperature in degree Celsius. It would also implement a method to convert the temperature into degree Fahrenheit. One way of doing this is as follows.

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

# We could make objects out of this class and manipulate the attribute temperature as we wished. Try these on Python shell.

#     >>> # create new object
#     >>> man = Celsius()
#     >>> # set temperature
#     >>> man.temperature = 37
#     >>> # get temperature
#     >>> man.temperature
#     37
#     >>> # get degrees Fahrenheit
#     >>> man.to_fahrenheit()
#     98.60000000000001

# The extra decimal places when converting into Fahrenheit is due to the floating point arithmetic error (try 1.1 + 2.2 in the Python interpreter).

# Whenever we assign or retrieve any object attribute like temperature, as show above, Python searches it in the object's __dict__ dictionary.

#     >>> man.__dict__
#     {'temperature': 37}

# Therefore, man.temperature internally becomes man.__dict__['temperature'].

# Now, let's further assume that our class got popular among clients and they started using it in their programs. They did all kinds of assignments to the object.

# One fateful day, a trusted client came to us and suggested that temperatures cannot go below -273 degree Celsius (students of thermodynamics might argue that it's actually -273.15), also called the absolute zero. He further asked us to implement this value constraint. Being a company that strive for customer satisfaction, we happily heeded the suggestion and released version 1.01 (an upgrade of our existing class).
# Using Getters and Setters

# An obvious solution to the above constraint will be to hide the attribute temperature (make it private) and define new getter and setter interfaces to manipulate it. This can be done as follows.


class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

# We can see above that new methods get_temperature() and set_temperature() were defined and furthermore, temperature was replaced with _temperature. An underscore (_) at the beginning is used to denote private variables in Python.

#     >>> c = Celsius(-277)
#     Traceback (most recent call last):
#     ...
#     ValueError: Temperature below -273 is not possible
#     >>> c = Celsius(37)
#     >>> c.get_temperature()
#     37
#     >>> c.set_temperature(10)
#     >>> c.set_temperature(-300)
#     Traceback (most recent call last):
#     ...
#     ValueError: Temperature below -273 is not possible

# This update successfully implemented the new restriction. We are no longer allowed to set temperature below -273.

# Please note that private variables don't exist in Python. There are simply norms to be followed. The language itself don't apply any restrictions.

#     >>> c._temperature = -300
#     >>> c.get_temperature()
#     -300

# But this is not of great concern. The big problem with the above update is that, all the clients who implemented our previous class in their program have to modify their code from obj.temperature to obj.get_temperature() and all assignments like obj.temperature = val to obj.set_temperature(val).

# This refactoring can cause headaches to the clients with hundreds of thousands of lines of codes.

# All in all, our new update was not backward compatible. This is where property comes to rescue.

#! The Power of @property

# The pythonic way to deal with the above problem is to use property. Here is how we could have achieved it.


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

# And, issue the following code in shell once you run it.

# >>> c = Celsius()

# We added a print() function inside get_temperature() and set_temperature() to clearly observe that they are being executed.

# The last line of the code, makes a property object temperature. Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).

# Any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will automatically call set_temperature(). This is one cool feature in Python.

# We can see above that set_temperature() was called even when we created an object.

# Can you guess why?

# The reason is that when an object is created, __init__() method gets called. This method has the line self.temperature = temperature. This assignment automatically called set_temperature().

#     >>> c.temperature
#     Getting value
#     0

# Similarly, any access like c.temperature automatically calls get_temperature(). This is what property does. Here are a few more examples.

#     >>> c.temperature = 37
#     Setting value
#     >>> c.to_fahrenheit()
#     Getting value
#     98.60000000000001

# By using property, we can see that, we modified our class and implemented the value constraint without any change required to the client code. Thus our implementation was backward compatible and everybody is happy.

# Finally note that, the actual temperature value is stored in the private variable _temperature. The attribute temperature is a property object which provides interface to this private variable.

#! Digging Deeper into Property

# In Python, property() is a built-in function that creates and returns a property object. The signature of this function is

#     property(fget=None, fset=None, fdel=None, doc=None)

# where, fget is function to get value of the attribute, fset is function to set value of the attribute, fdel is function to delete the attribute and doc is a string (like a comment). As seen from the implementation, these function arguments are optional. So, a property object can simply be created as follows.

#     >>> property()
#     <property object at 0x0000000003239B38>

# A property object has three methods, getter(), setter(), and deleter() to specify fget, fset and fdel at a later point. This means, the line

#     temperature = property(get_temperature,set_temperature)

# could have been broken down as

#     # make empty property
#     temperature = property()
#     # assign fget
#     temperature = temperature.getter(get_temperature)
#     # assign fset
#     temperature = temperature.setter(set_temperature)

# These two pieces of codes are equivalent.

# Programmers familiar with decorators in Python can recognize that the above construct can be implemented as decorators.

# We can further go on and not define names get_temperature and set_temperature as they are unnecessary and pollute the class namespace. For this, we reuse the name temperature while defining our getter and setter functions. This is how it can be done.


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

# The above implementation is both, simple and recommended way to make properties. You will most likely encounter these types of constructs when looking for property in Python.

# ==========================#==========================

#!                                                       ASSERT

# Python Assert Statement
# In this article we will learn about assertion in Python using assert.
# What is Assertion?

# Assertions are statements that assert or state a fact confidently in your program. For example, while writing a division function, you're confident the divisor shouldn't be zero, you assert divisor is not equal to zero.

# Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error.

# It is also a debugging tool as it brings the program on halt as soon as any error is occurred and shows on which point of the program error has occurred.

# You can learn more about assertions in the article: The benefits of programming with Assertions

# We can be clear by looking at the flowchart below:

# Python Assert Flowchart

# Python assert Statement

# Python has built-in assert statement to use assertion condition in the program. assert statement has a condition or expression which is supposed to be always true. If the condition is false assert halts the program and gives an AssertionError.
# Syntax for using Assert in Pyhton:

# assert <condition>

# assert <condition>,<error message>

# In Python we can use assert statement in two ways as mentioned above.

#     assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
#     assert statement can also have a condition and a optional error message. If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.

# Let's take an example, where we have a function which will calculate the average of the values passed by the user and the value should not be an empty list. We will use assert statement to check the parameter and if the length is of the passed list is zero, program halts.

# Example 1: Using assert without Error Message

# def avg(marks):
#     assert len(marks) != 0
#     return sum(marks)/len(marks)

# mark1 = []
# print("Average of mark1:",avg(mark1))

# When we run the above program, the output will be:

# AssertionError

# We got an error as we passed an empty list mark1 to assert statement, the condition became false and assert stops the program and give AssertionError.

# Now let's pass another list which will satisfy the assert condition and see what will be our output.
# Example 2: Using assert with error message

# def avg(marks):
#     assert len(marks) != 0,"List is empty."
#     return sum(marks)/len(marks)

# mark2 = [55,88,78,90,79]
# print("Average of mark2:",avg(mark2))

# mark1 = []
# print("Average of mark1:",avg(mark1))

# When we run the above program, the output will be:

# Average of mark2: 78.0
# AssertionError: List is empty.

# We passed a non-empty list mark2 and also an empty list mark1 to the avg() function and we got output for mark2 list but after that we got an error AssertionError: List is empty. The assert condition was satisfied by the mark2 list and program to continue to run. However, mark1 doesn't satisfy the condition and gives an AssertionError.
# Key Points to Remember

#     Assertions are the condition or boolean expression which are always supposed to be true in the code.
#     assert statement takes an expression and optional message.
#     assert statement is used to check types, values of argument and the output of the function.
#     assert statement is used as debugging tool as it halts the program at the point where an error occurs.

#!#==========================#==========================                                                    CANCEL GITHUB PAGES                                                    #==========================#==========================
