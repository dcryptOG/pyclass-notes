# STRING INTERPOLATION: placing variable into a string
# TODO ADD MORE AT END LINKS
#! 2 STRING INTERPOLATION methods

# * 1: .format()
# * 2: f-strings(formatted string liaterals)

# EXAMPLE .format()
print("INPUT: \t'This is a string {}'.format('inserted')")
print('OUTPUT:\t This is a string {}'.format('inserted'))

print("'\nINPUT:\t The {2} {1} {0}'.format('fox', 'brown', 'quick')")
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print("'\nINPUT:\tThe {0} {0} {0}'.format('fox', 'brown', 'quick')")
print('OUTPUT\t The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print("'\nINPUT:\t The {f} {b} {q}'.format(f='fox', b='brown', q='quick')")
print('OUTPUT:\t The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

#! EXAMPLE FLOAT FORMATTING
#! SYNTAX "{VALUE:WIDTH.PRECISION f}"
#WIDTH is whitespace
# PRECISION places after decimal
print('\nSYNTAX "{VALUE:WIDTH.PRECISION f}"')
print("\float formatting\n\nWIDTH is whitespace\nPRECISION places after decimal")
result = 100/777
print("The result was {}".format(result))
print("The result was {r}".format(r=result))
print('\n"The result was {r:1.3f}".format(r=result)')
print("The result was {r:1.3f}".format(r=result))

#! EXAMPLE f-string
print('\nSYNTAX f-string')
name = "Geoff"
age = 29
print("\nf'Hello my name is {name}'")
print(f'Hello my name is {name}')
print("f'{name} is {age} years old'")
print(f'{name} is {age} years old')


#! Here are some basic argument specifiers you should know:

# * %s - String (or any object with a string representation, like numbers)

# * %d - Integers

# * %f - Floating point numbers

# * %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# * %x/%X - Integers in hex representation (lowercase/uppercase)

# https://www.learnpython.org/en/String_Formatting

#! %s - String (or any object with a string representation, like numbers)

# Formatting with placeholders

# You can use %s to inject strings into your print statements. The modulo % is referred to as a "string formatting operator".

print("I'm going to inject %s here." % 'something')

# ? You can pass multiple items by placing them inside a tuple after the % operator.

print("\nI'm going to inject %s text here, and %s text here." % ('some', 'more'))

# I'm going to inject some text here, and more text here.

# You can also pass variable names:
print('\n')
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here." % (x, y))

#! FORMAT CONVERSTION METHODS

# It should be noted that two methods %s and %r convert any python object to a string using two separate methods: str() and repr().

# * NOTE that %r and repr() deliver the string representation of the object, including quotation marks and any escape characters.

print('He said his name was %s.' % 'Fred')
print('He said his name was %r.' % 'Fred')

# ? OUTPUT He said his name was Fred.
# ?OUTPUT  He said his name was 'Fred'.

# As another example, \t inserts a tab into a string.

print('I once caught a fish %s.' % 'this \tbig')
print('I once caught a fish %r.' % 'this \tbig')

# ?OUTPUT:   I once caught a fish this 	big.
# ?OUTPUT:   I once caught a fish 'this \tbig'.

# todo       %s operator converts whatever it sees into a STRING, including integers and floats.

#! %d - Integers

#  The %d operator converts NUMBERS to INTEGERS first, WITOUTH ROUNDING rounding. Note the difference below:

print('I wrote %s programs today.' % 3.75)
print('I wrote %d programs today.' % 3.75)

# ?OUTPUT:      I wrote 3.75 programs today.
# ?OUTPUT:    I wrote 3 programs today.

#! %f - Floating point numbers


#! %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#! %x/%X - Integers in hex representation (lowercase/uppercase)


#! The .format() method has several advantages over the %s placeholder method:
# 1. Inserted objects can be called by index position:

print('\n Advantages of .format() over perents\nThe {2} {1} {0}'.format(
    'fox', 'brown', 'quick'))

# The quick brown fox

# 2. Inserted objects can be assigned keywords:

print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(
    a=1, b='Two', c=12.3))

# First Object: 1, Second Object: Two, Third Object: 12.3

# 3. Inserted objects can be reused, avoiding duplication:

print('\nA %s saved is a %s earned.' % ('penny', 'penny'))
# # vs.
print('A {p} saved is a {p} earned.'.format(p='penny\n'))

# A penny saved is a penny earned.
# A penny saved is a penny earned.

# Alignment, padding and precision with .format()

# Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

# Fruit    | Quantity
# Apples   |       3.0
# Oranges  |        10

# By default, .format() aligns text to the left, numbers to the right.
# ? You can pass an optional <,^, or > to set a left, center or right alignment:

print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))

# Left     |  Center  |    Right
# 11       |    22    |       33

# You can precede the aligment operator with a padding character

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))

# Left==== | -Center- | ...Right
# 11====== | ---22--- | ......33

# Field widths and float precision are handled in a way similar to placeholders. The following two print statements are equivalent:

print('This is my ten-character, two-decimal number:%10.2f' % 13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

# This is my ten-character, two-decimal number:     13.58
# This is my ten-character, two-decimal number:     13.58

# Note that there are 5 spaces following the colon, and 5 characters taken up by 13.58, for a total of ten characters.

# For more information on the string .format() method visit https://docs.python.org/3/library/string.html#formatstrings
# Formatted String Literals (f-strings)

#! Introduced in Python 3.6, f-strings offer several benefits over the older .format() string method described above.
# * For one, you can bring outside variables immediately into to the string rather than pass them as arguments through .format(var).

name = 'Fred'

print(f"\nf-string formatting method\nHe said his name is {name}.")

# He said his name is Fred.

# Pass !r to get the string representation:

print(f"\nHe said his name is {name!r}")

# He said his name is 'Fred'

#!SYNTAX
#! Float formatting follows "result: {value:{width}.{precision}}"

# Where with the .format() method you might see {value:10.4f}, with f-strings this can become {value:{10}.{6}}

num = 23.45678
print("\nMy 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# My 10 character, four decimal number is:   23.4568
# My 10 character, four decimal number is:   23.4568

# Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. This fits more closely with scientific notation and statistical analysis. Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# My 10 character, four decimal number is:   23.4500
# My 10 character, four decimal number is:     23.45

# * If this becomes important, you can always use .format() method syntax inside an f-string:

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")

# My 10 character, four decimal number is:   23.4500
# My 10 character, four decimal number is:   23.4500

# For more info on formatted string literals visit https://docs.python.org/3/reference/lexical_analysis.html#f-strings


# REVIEW NOTEBOOK FOR SECTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/00-Python%20Object%20and%20Data%20Structure%20Basics
