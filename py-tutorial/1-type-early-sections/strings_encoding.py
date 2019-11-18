# https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686


# \ escape single quote
print('doesn\'t')
print('I\'m')

# \a

# ASCII Bell
# \b 	ASCII Backspace
# \f 	ASCII Formfeed
# \n 	ASCII Linefeed
# \r 	ASCII Carriage Return
# \t 	ASCII Horizontal Tab
# \v 	ASCII Vertical Tab
# \ooo 	Character with octal value ooo
# \xHH 	Character with hexadecimal value HH

#! Python Raw String

# Let’s say we want to create a string Hi\nHello in python. If we try to assign it to a normal string, the \n will be treated as a new line.


# s = 'Hi\nHello'
# print(s)

# Output:


# Hi
# Hello

# Let’s see how raw string helps us in treating backslash as a normal character.


# raw_s = r'Hi\nHello'
# print(raw_s)

# Output: Hi\nHello

# Let’s see another example where the character followed by backslash doesn’t have any special meaning.


# >>> s = 'Hi\xHello'
#   File "<input>", line 1
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \xXX escape

# We got the error because python doesn’t know how to decode ‘\x’ as it doesn’t have any special meaning. Let’s see how we can create the same string using raw strings.


# >>> s = r'Hi\xHello'
# >>> print(s)
# Hi\xHello

# If you are on Python console and create a raw-string like below.


# >>> r'Hi\xHello'
# 'Hi\\xHello'

# Don’t get confused with the output having two backslashes. It’s just to show it as a normal python string where backslash is being escaped.
# Python Raw String and Quotes

# When a backslash is followed by a quote in a raw string, it’s escaped. However, the backslash also remains in the result. Because of this feature, we can’t create a raw string of single backslash. Also, a raw string can’t have an odd number of backslashes at the end.

# Some of the invalid raw strings are:


# r'\'  # missing end quote because the end quote is being escaped
# r'ab\\\'  # first two backslashes will escape each other, the third one will try to escape the end quote.

# Let’s look at some of the valid raw string examples with quotes.


# raw_s = r'\''
# print(raw_s)

# raw_s = r'ab\\'
# print(raw_s)

# raw_s = R'\\\"'  # prefix can be 'R' or 'r'
# print(raw_s)

# Output:


# \'
# ab\\
# \\\"

# That’s all for a quick introduction of python raw string.
