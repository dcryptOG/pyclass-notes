#!Using Python Interpreter
#! Invoking python interpreter

# On UNix
# py interpreter usually installed as /usr/local/bin/python3.7

# putting  in search path
# /usr/local/bin

# pupular alternative location
# /usr/local/python

# ?WIndows

# python3.7 command abialable

# If you have the py.exe launcher
# you can use command
# py

# set
# set temporarily sets enviorment variables

# C:\> set PATH=C:\pRogram Files\Python 3.7;%PATH%
# C:\>set PYTHONPATH=%PYTHONPATH%;C:\My_python_
# C:\>python

# Windows will concat User variables after System vairables, which may cause unexpected results when modifying path
# PYTHONPATH var is used by all versions of Py2 and Py3, so you should not permanently config this var unless it only includes code that is compatible with ALL OF YOUR INSTALLED PY VERSIONS

# ?End of file character

# Conrol-D on uniz
# Control-Z on windows
# quit()

# ? Command line editing

# Interpreter's line-editing features indclude inteerative editing,
#  history substitution
# and code completion on systems that support the GNU Readline Library

# Conrol-P to check if command line editing supported

# Interpreter operates like the Unix shell: when called with standard input connected to atty device, it reads and executes commands interactively

# When called witha file name arg or with afile as standard input it reads and executes a script from that file

#! command line

# https://docs.python.org/3.7/using/cmdline.html#cmdoption-c

# ? 2nd way of starting intrepeter

# *python -c command [arg]...
# executes the satements in command, analogus to the chell's -c option

# ? -c <command>

# Execute python code in command.

# command can be one or more statements separted by new lines. Leading whitespace.

# If -c given the first lement of sys.argv will be "-c" and the current directory will be added to the start of sys.path (allowing mods in that directory to be imported as top level modules)

#! python [-bBdEhiIOqsSuvVwx?] [-c command | -m module-name | script | -] [args]

# ? when called with standard input connected to a tty device it promts for command and executes them until an EOF (an end-of-file character Control-Z on windows, Control-D Unix)

# ? When called with a file name arg or file as standard input, it reads and executes a script from that file

# ?When called with a directory name arg, it reads and exectures appropriately named script from that directory

# ? # Execute python code in command. command can be one or more statements separted by new lines. Leading whitespace.

# ? WHen called with -m module-name, the given module is located on the Python module path and exectued as a script...Search sys.path for named module and execute its contents as the __main__ module
# Since arg is module name, MUST NOT give file extension .py

# -I option can be used to run script in isolated mode where sy.path contains neither the current directory nor the user's site-packages directory. All PYTHON* env vars are ignored too.

# NOTE in non-interactive mode, the entire input is parsed before it is executed

# ? -i
# Write -i before script to enter interactive mode after running script

#!sys.argv

# The list of command line args passed to a python script.
# argv[0] is the script name (it is OS dependent wheter this a full pathname or not)

# If the command was executed using the-c command line option to the interpreter, argv[0] is set to tthe string '-c'.

# if no script name was passed to Py interpreter argv[0] is the empty string

#!fileinput

# MODULE implements a helper class and functions to quicly write a loop over standard input or a lsit of files.
#
# If you just want to read or write one file see open()

# ?Standard use
#import fileinput
# for line in fileinput.input():
#    process(line)

# this iterates over the lines of all files listed in sys.argv[1:], defaulting to sys.stdin

# If a filename is '-' it is also replaced by sys.stdin and the optional args mode and openhook are ignored.

# To specify an alt list of filenames pass it as the first arg to input().

# All files are opened in text mode by default

# Change this mode by specifying mode parameter in call to input() or FileInput

# To loop over standard input, or list the list of files given on command line, see fileinput module

# On Unix command line args are passed by bytes from OS. Python decodes them with filesystem encoding and "surrogateescape" error handler. When you neeed original bytes, you can get it by [os.fsencode(arg) for arg in sys.argv]


# ==========================#==========================

#!2.1                        ARG passing

# argv == list of strings containing script name and args
# You can access list by executing
#import sys

# When no args given sys.argv[0] is empy string

# when script naem given as
# '-' == standard input
# sys.argv[0] set to '-c'

# '-m' module
# sys.argv[0] set to full module name

# options are found after -c or -m are not consumed by Py interpretres option processing, but left in sys.arv for command or module to handle.

# ==========================#==========================

#!2.1                     INTERACTIVE MODE

# interactive mode == commands are read from a tty

# >>>COMMAND
# ...    continuation line

# https://docs.python.org/3.7/tutorial/appendix.html#tut-interac
