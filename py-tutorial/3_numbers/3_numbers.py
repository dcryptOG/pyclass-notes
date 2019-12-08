# Number Data Type in Python
#! Number Data Type in Python

# Python supports integers, floating point numbers and complex numbers. They are defined as int, float and complex class in Python.

# Integers and floating points are separated by the presence or absence of a decimal point. 5 is integer whereas 5.0 is a floating point number.

# * Complex numbers are written in the form, x + yj,
# ? where x is the real part
# ? y is the imaginary part.

# We can use the type() function to know which class a variable or a value belongs to and isinstance() function to check if it belongs to a particular class.

import random
import math
from fractions import Fraction as F
import fractions
from decimal import Decimal as D
import decimal
a = 5

# Output: <class 'int'>
print(type(a))

# Output: <class 'float'>
print(type(5.0))

# Output: (8+3j)
c = 5 + 3j
print('\nc=5+3j\nprint(c+3)\n', c + 3)

# Output: True
print(isinstance(c, complex))

# ? While integers can be of any length,
# ?Floating point number is accurate only up to 15 decimal places
# ?(the 16th place is inaccurate).

# Numbers we deal with everyday are decimal (base 10) number system.
# But computer programmers (generally embedded programmer) need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.

# ==========================#==========================

# Represent these numbers by appropriately placing a prefix before that number.

# Lists these prefix.
# Number system prefix for Python numbers Number System 	Prefix
# Binary 	'0b' or '0B'
# Octal 	'0o' or '0O'
# Hexadecimal 	'0x' or '0X'

# todo
#  Here are some examples

# Output: 107
print('\nNUMBER PREFIXES\nBinary 0b 0B\nOctal 0o or 0O\nHexadecimal 0x or 0X\n\nprint(0b1101011)\n', 0b1101011)

# Output: 253 (251 + 2)
print('\n0xFB + 0b10\nOutput 253 (251 +2)', 0xFB + 0b10)

# Output: 13
print(f'\n0o15\nOutput{0o15}\n')

# ? When you run the program, the output will be:

# 107
# 253
# 13

# ==========================#==========================

#! Type Conversion


# *Type Conversion AKA Coercion == We can convert one type of number into another.

# If one of the operand is float, operations like addition, subtraction coerce integer to float implicitly (automatically)

#     >>> 1 + 2.0
#     3.0

# We can see above that 1 (integer) is coerced into 1.0 (float) for addition and the result is also a floating point number.

# We can also use built-in functions like int(), float() and complex() to convert between types explicitly. These function can even convert from strings.

#     >>> int(2.3)
#     2
#     >>> int(-2.8)
#     -2
#     >>> float(5)
#     5.0
#     >>> complex('3+5j')
#     (3+5j)

# When converting from float to integer, the number gets truncated (integer that is closer to zero).

#! Python Decimal

# Python built-in class float performs some calculations that might amaze us. We all know that the sum of 1.1 and 2.2 is 3.3, but Python seems to disagree.

#     >>> (1.1 + 2.2) == 3.3
#     False

# What is going on?

# It turns out that floating-point numbers are implemented in computer hardware as binary fractions, as computer only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know, cannot be accurately stored in our computer.

# Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and we can only approximate it.

# Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011... and our computer only stores a finite number of it.

# This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error in Python.

#     >>> 1.1 + 2.2
#     3.3000000000000003

# To overcome this issue, we can use decimal module that comes with Python. While floating point numbers have precision up to 15 decimal places, the decimal module has user settable precision.


# Output: 0.1
print(0.1)

# Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))

# This module is used when we want to carry out decimal calculations like we learned in school.

# It also preserves significance. We know 25.50 kg is more accurate than 25.5 kg as it has two significant decimal places compared to one.

#from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))

# Notice the trailing zeroes in the above example.

# We might ask, why not implement Decimal every time, instead of float? The main reason is efficiency. Floating point operations are carried out must faster than Decimal operations.
# When to use Decimal instead of float?

# We generally use Decimal in the following cases.

#     When we are making financial applications that need exact decimal representation.
#     When we want to control the level of precision required.
#     When we want to implement the notion of significant decimal places.
#     When we want the operations to be carried out like we did at school

#! Python Fractions

# Python provides operations involving fractional numbers through its fractions module.

# A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.

# We can create Fraction objects in various ways.

#import fractions

# Output: 3/2
print(fractions.Fraction(1.5))

# Output: 5
print(fractions.Fraction(5))

# Output: 1/3
print(fractions.Fraction(1, 3))
# While creating Fraction from float, we might get some unusual results. This is due to the imperfect binary floating point number representation as discussed in the previous section.

# Fortunately, Fraction allows us to instantiate with string as well. This is the preferred options when using decimal numbers.

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

# This datatype supports all basic operations. Here are few examples.

#from fractions import Fraction as F

# Output: 2/3
print(F(1, 3) + F(1, 3))

# Output: 6/5
print(1 / F(5, 6))

# Output: False
print(F(-3, 10) > 0)

# Output: True
print(F(-3, 10) < 0)

#! Python Mathematics

# Python offers modules like math and random to carry out different mathematics like trigonometry, logarithms, probability and statistics, etc.

#import math

# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))

# Here is the full list functions and attributes available in Python math module.

#import random

# Output: 16
print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())

# Here is the full list functions and attributes available in Python random module.
