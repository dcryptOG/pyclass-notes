#! 7. Input and Output
#! 7. Input and Output

#! 7.1. Fancier Output Formatting

# ? So far, 2 ways of writing values:
#
# 1.    Expression Statements
# 2.    the print() function.
# 3.    (A third way is using the write() method of file objects; the standard output file can be referenced as sys.stdout.
#

# Often you’ll want more control over the formatting of your output than simply printing space-separated values.
#
# ? There are several ways to format output.

# * FORMATTED STRING LITERSLS string literals, begin a string with f or F before the opening quotation mark or triple quotation mark.

# Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

#     >>> year = 2016
#     >>> event = 'Referendum'
#     >>> f'Results of the {year} {event}'
#     'Results of the 2016 Referendum'

# *     The str.format() method need to provide the information to be formatted.
#     >>>

#     >>> yes_votes = 42_572_654
#     >>> no_votes = 43_132_495
#     >>> percentage = yes_votes / (yes_votes + no_votes)
#     >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
#     ' 42572654 YES votes  49.67%'

# ?     String handling by using string slicing and concatenation operations to create any layout you can imagine.
#
# The string type has some methods that perform useful operations for padding strings to a given column width.

# ? When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the:
# 1.    repr()
# 2.    str() functions.

# *     str() function is meant to return representations of values which are fairly human-readable,
#
# *    repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax).
#
# For objects which don’t have a particular representation for human consumption, str() will return the same value as repr().
#
#   Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function.
#
# *Strings have 2 distinct representations.

# ?examples:

# >>> s = 'Hello, world.'
# >>> str(s)
# 'Hello, world.'
# >>> repr(s)
# "'Hello, world.'"
# >>> str(1/7)
# '0.14285714285714285'
# >>> x = 10 * 3.25
# >>> y = 200 * 200
# >>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# >>> print(s)
# The value of x is 32.5, and y is 40000...
# ? >>> # The repr() of a string adds string quotes and backslashes:
# ... hello = 'hello, world\n'
# >>> hellos = repr(hello)
# >>> print(hellos)
# 'hello, world\n'
# >>> # The argument to repr() may be any Python object:
# ... repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))"


#! Template strings

# * The STRING MODULE contains a TEMPLATE CLASS that offers yet another way to substitute values into strings:
# using placeholders like $x and replacing them with values from a dictionary
#  offers much less control of the formatting.


# Template strings provide simpler string substitutions as described in PEP 292. A primary use case for template strings is for internationalization (i18n) since in that context, the simpler syntax and functionality makes it easier to translate than other built-in string formatting facilities in Python. As an example of a library built on template strings for i18n, see the flufl.i18n package.

# Template strings support $-based substitutions, using the following rules:

#     $$ is an escape; it is replaced with a single $.

#     $identifier names a substitution placeholder matching a mapping key of "identifier". By default, "identifier" is restricted to any case-insensitive ASCII alphanumeric string (including underscores) that starts with an underscore or ASCII letter. The first non-identifier character after the $ character terminates this placeholder specification.

#     ${identifier} is equivalent to $identifier. It is required when valid identifier characters follow the placeholder but are not part of the placeholder, such as "${noun}ification".

# Any other appearance of $ in the string will result in a ValueError being raised.

# The string module provides a Template class that implements these rules. The methods of Template are:

# class string.Template(template)

#     The constructor takes a single argument which is the template string.

#     substitute(mapping, **kwds)

#         Performs the template substitution, returning a new string. mapping is any dictionary-like object with keys that match the placeholders in the template. Alternatively, you can provide keyword arguments, where the keywords are the placeholders. When both mapping and kwds are given and there are duplicates, the placeholders from kwds take precedence.

#     safe_substitute(mapping, **kwds)

#         Like substitute(), except that if placeholders are missing from mapping and kwds, instead of raising a KeyError exception, the original placeholder will appear in the resulting string intact. Also, unlike with substitute(), any other appearances of the $ will simply return $ instead of raising ValueError.

#         While other exceptions may still occur, this method is called “safe” because it always tries to return a usable string instead of raising an exception. In another sense, safe_substitute() may be anything other than safe, since it will silently ignore malformed templates containing dangling delimiters, unmatched braces, or placeholders that are not valid Python identifiers.

#     Template instances also provide one public data attribute:

#     template

#         This is the object passed to the constructor’s template argument. In general, you shouldn’t change it, but read-only access is not enforced.

# Here is an example of how to use a Template:
# >>>

# >>> from string import Template
# >>> s = Template('$who likes $what')
# >>> s.substitute(who='tim', what='kung pao')
# 'tim likes kung pao'
# >>> d = dict(who='tim')
# >>> Template('Give $who $100').substitute(d)
# Traceback (most recent call last):
# ...
# ValueError: Invalid placeholder in string: line 1, col 11
# >>> Template('$who likes $what').substitute(d)
# Traceback (most recent call last):
# ...
# KeyError: 'what'
# >>> Template('$who likes $what').safe_substitute(d)
# 'tim likes $what'


#! 7.1.1. Formatted String Literals

# FORMATTED STRING LITERALS (AKA F-STRINGS) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

# An OPTIONAL FORMAT SPECIFIER can follow the expression. This allows greater control over how the value is formatted.
#
# ? The following example rounds pi to three places after the decimal:
# >>>

# >>> import math
# >>> print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

# ? Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
# >>>

# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# >>> for name, phone in table.items():
# ...     print(f'{name:10} ==> {phone:10d}')
# ...
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# ? Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
# >>>

# >>> animals = 'eels'
# >>> print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
# >>> print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.

# For a reference on these format specifications, see the reference guide for the Format Specification Mini-Language.

#! 7.1.2. The String format() Method

# ? Basic usage of the str.format() method looks like this:
# >>>

# >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

# * The brackets and characters within them (called FORMAT FIELDS) are replaced with the objects passed into the str.format() method.

# ? A NUMBER in the brackets can be used to refer to the position of the object passed into the str.format() method.

# >>> print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
# >>> print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

# ? If KW ARGS are used in the str.format() method, their values are referred to by using the name of the argument.

# >>> print('This {food} is {adjective}.'.format(
# ...       food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

# ? POSITIONAL ARGS and KW ARGS can be arbitrarily combined:

# >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
#                                                        other='Georg'))
# The story of Bill, Manfred, and Georg.

# ? Formatted by NAME if you have a really long format string that you don’t want to split up. Done by simply passing the dict and using square brackets '[]' to access the keys

# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
# ...       'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# ? This could also be done by passing the table as keyword arguments with the ‘**’ notation.

# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# * This is particularly useful in combination with the BUILT-IN FUNCTION VARS(), which returns a dictionary containing all local variables.

# ? As an example, the following lines produce a tidily-aligned set of columns giving integers and their squares and cubes:

# >>> for x in range(1, 11):
# ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# ...
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# For a complete overview of string formatting with str.format(), see Format String Syntax.

#! 7.1.3. Manual String Formatting

# ? Here’s the same table of squares and cubes, formatted manually:

# >>> for x in range(1, 11):
# ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# ...     # Note use of 'end' on previous line
# ...     print(repr(x*x*x).rjust(4))
# ...
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# * (Note that the one space between each column was added by the way print() works: it ALWAYS adds spaces BETWEEN its ARGS.)

# *STR.RJUST() method of string objects RIGHT-JUSTIFIES a string in a field of a given width by PADDING it with SPACES on the LEFT.

# ?  There are similar methods str.ljust() and str.center().

# These methods do not write anything, they just return a new string.
#
# If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but
# If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

# ? There is another method, STR.ZFILL(), which PADS a numeric string on the LEFT w/ ZEROS. It understands about plus and minus signs:

# >>> '12'.zfill(5)
# '00012'
# >>> '-3.14'.zfill(7)
# '-003.14'
# >>> '3.14159265359'.zfill(5)
# '3.14159265359'

#! 7.1.4. Old string formatting

# * The % operator can also be used for string formatting.
# It interprets the left argument much like a sprintf()-style format string to be applied to the right argument, and returns the string resulting from this formatting operation.
#
# ?For example:

# >>> import math
# >>> print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.

# More information can be found in the printf-style String Formatting section.

#! 7.2. Reading and Writing Files

# * OPEN() returns a file object, and is most commonly used with two arguments: open(FILENAME, MODE).
# >>>import os
# ? GET CURRENT WORKING DIR
# *>>> os.getcwd()
# ? LIST ALL DIR
# *>>> os.listdir()
# ? MKDIR DIR
# *>>> os.mkdir('test')
# ? CHANGE DIR
# *>>> os.chdir('test')
# ? WRITE FILE
# >>> f = open('workfile', 'w')

# *open('arg1', 'arg2')
# ? FIRST ARG
# a STRING containing the filename.
# ? SEVOND ARG -MODE
# a STRING containing a few characters describing the way in which the file will be used.

# todo                               MODE can be

# ?       1. 'r' == READ FILE ONLY

# ?       2.  'w' == WRITE FILE ONLY
# (an existing file with the same name will be erased)

# ?       3. 'a' == opens the file for APPENDING;
# data written to the file is ADDED to END, automatically.
# ?       4.  'r+' opens the file for both reading and writing.
#  The mode argument is optional
#  'r' will be assumed if it’s omitted.

# Normally, files are opened in

# * TEXT MODE == you read and write strings from and to the file, which are encoded in a specific encoding.
#
# If encoding is not specified, the default is PLATFORM DEPENDENT (see open())

# ?       5.  'b' appended to the mode opens the file in BINARY MODE

# * BINARY MODE == now the data is read and written in the form of BYTES OBJ.
# This mode should be used for all files that don’t contain text.

# todo =======================

# NOTE DEFAULT TEXT MODE, when READING is to convert platform-specific line endings to:
# ?      1. \n on Unix
# ?      2. \r\n on Windows) to just \n.
#
# NOTE DEFAULT TEXT MODE, when WRITING  is to convert occurrences of \n back to platform-specific line endings.

# NOTE This behind-the-scenes modification to file data is FINE for TEXT FILES but...
# ? WILL CORRUPT BINARY DATA
#  Like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

# *BEST PRACTICEe to use the WITH KEYWORD when dealing with FILE OBJECTS.

# ? The ADVANAGE is of of with:
# 1.    the file is PROPERLY CLOSED after its SUITE finishes, even if an exception is raised at some point.
# 2.     much SHORTER CODE vs writing equivalent try-finally blocks:
# >>>

# todo=== DO ACTIVITY IN INTERPRETER
# NOTE first
#  >>>import os
# ? GET CURRENT WORKING DIR
# *>>> os.getcwd()
# ? LIST ALL DIR
# *>>> os.listdir()
# ? MKDIR DIR
# *>>> os.mkdir('test')
# ? CHANGE DIR
# *>>> os.chdir('test')
# ? WRITE FILE

# NOTE example with
# >>> f = open('workfile', 'w')
# >>> with open('workfile') as f:
# ...     read_data = f.read()
# >>> f.closed
# True

# ? If you’re NOT USING WITH call F.CLOSE() to CLOSE the file
# (immediately free up any system resources used by it.)

# ?  If you DON'T CLOSE a file, Python’s GARBAGE COLLECTOR collector will eventually DESTROY OBJ and CLOSE FILE for you, but...
#       1. the file may STAY OPEN a WHILE.
#       2. Another risk is that different Python implementations will do            this CLEAN-UP at DIFFERENT TIMES.

# NOTE AFTER a FILE OBJECT is CLOSED  attempts to use the file object will automatically FAIL.

# >>> f.close()
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.

#! 7.2.1. Methods of File Objects

# TODO DO EXAMPLES
# * The rest of the examples in this section WILL ASSUME file object called f has already been created.

# ? To read a file’s contents, call
# *  f.read(size)

#  READS some quantity of data RETURNS it as
#                               1.     string (in text mode)
#                               2.     bytes object (in binary mode).

#  size is an OPTIONAL numeric argument.
# IF SIZE IS OMITTED or NEGATIVE, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory.
# IF SIZE IS SPECIFIED, at most size bytes are read and returned.
# IF the end of the file has been reached, f.read() will return an empty string ('').

#NOTE EX
# >>> f.read()
# 'This is the entire file.\n'
# >>> f.read()
# ''

# * f.readline() reads a single line from the file
# A newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous;

# IF f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

#NOTE EX
# >>> f.readline()
# 'This is the first line of the file.\n'
# >>> f.readline()
# 'Second line of the file\n'
# >>> f.readline()
# ''

# ? For reading lines from a file, you can LOOP over the file object.
# *This is memory efficient, fast, and leads to simple code:

#NOTE EX
# >>> for line in f:
# ...     print(line, end='')
# ...
# This is the first line of the file.
# Second line of the file

# ? If you want to read all the lines of a file in a list you can also use
# *1.   list(f)
# *2.    f.readlines().

# f.write(string) writes the contents of string to the file
#  returning the number of characters written.

# >>> f.write('This is a test\n')
# 15

# ? OTHER of OBJECTS NEED to be CONVERTED – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

# >>> value = ('the answer', 42)
# >>> s = str(value)  # convert the tuple to string
# >>> f.write(s)
# 18

# * f.tell() returns an integer giving the FILE OBJ CURRENT POSITION in the file represented as
# ?      1. Number of bytes from the beginning of the file when in binary mode
# ?      2. an opaque number when in text mode.

# * f.seek(offset, from_what) To CHANGE the FILE OBJ POSITON.

# The position is computed from adding OFFSET to a REFERENCE POINT
# REFERENCE POINT is selected by the from_what ARG.

#                   0 measures from the beginning of the file
#                   1 uses the current file position
#                   2 uses the end of the file as the reference point.
#
# from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.

# NOTE EX

# >>> f = open('workfile', 'rb+')
# >>> f.write(b'0123456789abcdef')
# 16
# >>> f.seek(5)      # Go to the 6th byte in the file
# 5
# >>> f.read(1)
# b'5'
# >>> f.seek(-3, 2)  # Go to the 3rd byte before the end
# 13
# >>> f.read(1)
# b'd'

# In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values are those returned from the f.tell(), or zero.
#  Any other offset value produces undefined behaviour.

# File objects have some additional methods, such as isatty() and truncate() which are less frequently used; consult the Library Reference for a complete guide to file objects.

#! 7.2.2. Saving structured data with json

# Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

# Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

# NOTE

# The JSON format is commonly used by modern applications to allow for data exchange. Good choice for interoperability.

# ? dumps() function,
#  If you have an object x, you can view its JSON string representation with a simple line of code:
# >>>

# >>> import json
# >>> json.dumps([1, 'simple', 'list'])
# '[1, "simple", "list"]'

# ? dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

# json.dump(x, f)

# To decode the object again, if f is a text file object which has been opened for reading:

# x = json.load(f)

# This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort. The reference for the json module contains an explanation of this.

# See also

# pickle - the pickle module

# Contrary to JSON, pickle is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.
