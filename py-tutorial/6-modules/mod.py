# Fibonacci numbers module


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacciseries up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

    # format result doesnt work in romt?
    #  ' '.join([str(x) for x in result])


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

    # Driver Program

    # python fibo.py <arguments>

    # the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

    # you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

    # $ python fibo.py 50
    # 0 1 1 2 3 5 8 13 21 34

    # If the module is imported, the code is not run:
    # >>>

    # >>> import fibo

#!      OS MODULE

# The os module contains 2 SUB-MODS
#   1. os.sys (same as sys)
#   2. os.path that are dedicated to the system and directories

#!   Module Search Path

# When a module named SPAM is imported, the interpreter first searches for a built-in module with that name.

#  If not found, it then searches for a file named SPAM.py in a list of directories given by the variable sys.path.

#! sys.path is initialized from these locations:

# *1.     The directory containing the input script (or the current directory when no file is specified).

# *2.     PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).

# *3.     The installation-dependent default.

# ? Note

# ? On file systems which support symlinks,

# ? the directory containing the input script is calculated after the symlink is followed.
#
# In other words the
#
# ? directory containing the symlink is not added to the module search path.

# * After initialization, Python programs can modify sys.path.

#!Compiled Python Files

#  Python caches the compiled version of each module in the __pycache__ directory under the name:

# module.verson.pyc

# where the version encodes the format of the compiled file

# ?Ex
#  CPython release 3.3 the compiled version of SPAM.py would be cached as

# *  __pycache__/spam.cpython-33.pyc.

# This naming convention allows compiled modules from different releases and different versions of Python to coexist.

# Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled.

#  This is a completely automatic process.

#! Python does not check the cache in 2 circumstances.
#
# * 1. it always recompiles and does not store the result for the module that’s loaded directly from the command line.

# *2. it does not check the cache if there is no source module.

# !To support a non-source (compiled only) distribution

# ? the compiled module must be in the source directory, and there must not be a source module.


#! Some tips for experts:

# You can use the -O or -OO switches on the Python command to reduce the size of a compiled module. The -O switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings. Since some programs may rely on having these available, you should only use this option if you know what you’re doing. “Optimized” modules have an opt- tag and are usually smaller. Future releases may change the effects of optimization.

# A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster about .pyc files is the speed with which they are loaded.

# The module compileall can create .pyc files for all modules in a directory.

#! 6.2. Standard Modules

# Python comes with a library of standard modules, described in a separate document, the Python Library Reference (“Library Reference” hereafter).

# *  Bult-In Interpreter MODs
# these provide access to operations that are not part of the core of the language, depend on underlying platform (0S)
# Allow for:
# 1.  Efficiency
# 2. Provide access to OS Primitives such as System Calls.


# ? For example
# * the winreg module (Windows Registry Access)
# These functions expose the Windows registry API to Python
# is only provided on Windows systems.


# *sys, which is built into every Python interpreter.

# 2 variables are only define strings if the interpreter is in interactive mode.

# ? sys.ps1
# Primary String Prompt
#
# ? sys.ps2
# Secondary String Prompts:

# >>> import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C> print('Yuck!')
# Yuck!
# C>


# *sys.path == is a list of strings that determines the interpreter’s search path for modules.
#
# It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set.
#
# You can modify it using standard list operations:
# >>>

# >>> import sys
# >>> sys.path.append('/ufs/guido/lib/python')

#! 6.3. The dir() Function

# * Without arguments, return the list of names in the current local scope.

# * With an argument, attempt to return a list of valid attributes for that object.

# * The default dir() mechanism behaves differently with different types of objects
#  as it attempts to produce the MOST RELEVANT, rather than complete, information:

# ? 1.     If object is MODULE OBJECT object,
#  the list contains the names of the module’s attributes (which names a module defines.).

# ? 2.     If the object is a TYPE or CLASS OBJECT,
# the list contains the names of its attributes,
#  recursively of the attributes of its bases.

# ? 3.     Otherwise, the list contains the OBJECT’S ATTRIBUTES names
# Names of its class’s attributes
# Recursively of the attributes of its class’s base classes.


# It returns a sorted list of strings:

# >>> import fibo, sys
# >>> dir(fibo)
# ['__name__', 'fib', 'fib2']
# >>> dir(sys)
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',...ect
# ...ect

# ? Without arguments, dir() lists the names you have defined currently:
# >>>

# >>> a = [1, 2, 3, 4, 5]
# >>> import fibo
# >>> fib = fibo.fib
# >>> dir()
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

# Note that it lists all types of names: variables, modules, functions, etc.

# ? dir() does not list the names of built-in functions and variables.
#  If you want a list of those, they are defined in the standard module builtins:

# >>> import builtins
# >>> dir(builtins)

#! 6.4. Packages

# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
# For example, the module name A.B designates a submodule named B in a package named A.
#  Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

# ?EX Design a collection of modules (a “package”) for the uniform handling of sound files and sound data.

#  There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au). So you need to create a collection of modules for the conversion between the various file formats.
#
#  There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), So you will be writing a never-ending stream of modules to perform these operations.
#
# A possible structure for your package
# (expressed in terms of a hierarchical filesystem):


# *Top-level package
# sound/
# *Initialize sound package
#       __init__.py
# *Subpackage for file format conversions
#       formats/
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
# *Subpackage for sound effects
#       effects/
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
# *Subpackage for filters
#       filters/
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# ? When importing the package, Python searches through the directories on:
# * sys.path
#  looking for the package subdirectory.

# * The __init__.py
# ? files are REQUIRED to make Python treat directories containing the file as packages.

# This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path.

# *__init__.py can
# 1.     __init__.py can just be an empty file
#
# 2.     It can also execute initialization code for the package
# 3.    Set the __all__ variable, described later.

# ?EXAMPLE

# ?     Users of the package can import individual modules from the package

# import sound.effects.echo

# ?     This loads the submodule sound.effects.echo. It must be referenced with its full name.

# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# ? An alternative way of importing the submodule is:

# from sound.effects import echo

# ?    Loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

# echo.echofilter(input, output, delay=0.7, atten=4)

# ?    Import the desired function or variable directly:

# from sound.effects.echo import echofilter

# ?    Loads the submodule echo, but this makes its function echofilter() directly available:

# echofilter(input, output, delay=0.7, atten=4)

#! Note
# When using
# * from package import item
# The item can be either a:

# 1.     Submodule (or subpackage) of the package
# 2.    Some other name defined in the package, like a function, class or variable.

#  The import statement first tests whether the item is
# 1.    Item defined in the Package;
# 2.    Then assumes item is a module and attempts to load it. #3.    If it fails to find it, an ImportError exception is raised.

# *Using syntax like import item.subitem.subsubitem,

# EACH item must be a package
# EXCEPT the last can be
# 1.    MODULE
# 2.    PACKAGE
#
# CANNOT be a class or function or variable defined in the previous item.

#! 6.4.1. Importing * From a Package

# Now what happens when the user writes from sound.effects import *?
#
# Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all.
#
# 1.    This could take a LONG TIME
# 2.    Importing sub-modules might have unwanted SIDE-EFFECTS that should only happen when the sub-module is explicitly imported.

# The only SOLUTION is for the package author to provide an EXPLICIT INDEX of the PACKAGE

# The import statement uses the following convention:
#
# if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered.
# It is up to the package author to keep this list up-to-date when a new version of the package is released.
# Package authors may also decide not to support it, if they don’t see a use for importing * from their package.

# ?For example, the file sound/effects/__init__.py could contain the following code:

# __all__ = ["echo", "surround", "reverse"]

# This would mean that from sound.effects import * would import the three named submodules of the sound package.

# If __all__ is not defined,
#  the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace
# ONLY ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes
# 1.  names defined (and submodules explicitly loaded) by __init__.py.
# 2.   Any submodules of the package that were explicitly loaded by previous import statements.
#
# ?Consider this code:

# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# In this example, the echo and surround modules are imported in the current namespace because they are defined in the sound.effects package when the from...import statement is executed. (This also works when __all__ is defined.)

# Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.

# * RECOMMENDED NOTATION Using from package import specific_submodule!
# ? UNLESS the importing module needs to use submodules with the same name from different packages.

#! 6.4.2. Intra-package References

# When packages are structured into subpackages (as with the sound package in the example), you can use

# *ABOSOLUTE IMPORTS to refer to submodules of siblings packages.
#
# ?FOR EXAMPLE
#  if the module
#  sound.filters.vocoder
#  needs to use the echo module in the sound.effects package, it can use
#
# from sound.effects import echo.

# * RELATIVE IMPORTS, with the from module import name form of import statement.

# use leading DOTS to indicate:
# 1.  CURRENT PACKAGE
# 2.  PARENT PACKAGES
#
# involved in the relative import.
#
# From the surround module for example, you might use:

# SYNTAX
# from . import echo
# from .. import formats
# from ..filters import equalizer

# *NOTE that RELATIVE IMPORTS are based on the name of the CURRENT MODULE.
#  Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application
# MAIN MODULE MUST ALWAYS USE ABSOLUTE IMPORTS.

#! 6.4.3. Packages in Multiple Directories

# * Packages support one more SPECIAL ATTRIBUTE, __path__.
# This is initialized to be a list containing the name of the directory holding the package’s __init__.py before the code in that file is executed.

# This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.

# While this feature is not often needed, it can be used to extend the set of modules found in a package.
