# Python Directory and Files Management

# In this article, you'll learn about file and directory management in Python

#  creating a directory
#  renaming dir
#  listing all directories
# working with dir

#! What is Directory in Python?

# If there are a large number of files to handle in your Python program,
# Arrange your code within different directories to make things more manageable.

#! Directory or Folder = is a collection of files and sub directories.

# Python has the

# * os module

#  which provides us with many useful methods to work with directories (and files as well).

#! Get Current Directory

# We can get the present working directory using the getcwd() method.

# This method returns the current working directory in the form of a string. We can also use the getcwdb() method to get it as bytes object.

import os

os.getcwd()
#     'C:\\Program Files\\PyScripter'
os.getcwdb()
#     b'C:\\Program Files\\PyScripter'

# * The EXTRA BACKSLASH implies ESCAPE SEQUENCE.

# The print() function will render this properly.

print(os.getcwd())
#     C:\Program Files\PyScripter

#! Changing Directory

# We can change the current working directory using the
# *chdir() method.

# The new path that we want to change to must be supplied as a string to this method.

# ?To return to C:\\

# forward slash chdir(/)
#  the backward slash (\) to separate path elements.

# * It is SAFTER to use ESCAPE SEQUENCE(\\) when using the BACKSLASH(\).

#     >>> os.chdir('C:\\Python33')
#     >>> print(os.getcwd())
#     C:\Python33

#! Previous directory

# os.chdir('..')
# os.chdir('..\\..')

#! List Directories and Files

# * listdir() method

# ? listdir()  lists all files and sub directories inside a directory

# todo        input path
# todo       returns a list of sub directories and files in that path.

# ? If NO PATH is specified, it returns from the CWD(current working directory).

#     >>> print(os.getcwd())

#     C:\Python33

os.listdir()
#     ['DLLs',
#     'Doc',
#     'include',
#     'Lib',
#     'libs',
#     'LICENSE.txt',
#     'NEWS.txt',
#     'python.exe',
#     'pythonw.exe',
#     'README.txt',
#     'Scripts',
#     'tcl',
#     'Tools']

os.listdir('C:\\Users')
#     ['$RECYCLE.BIN',
#     'Movies',
#     'Music',
#     'Photos',
#     'Series',
#     'System Volume Information']

#! Making a New Directory

# *mkdir() method.

# make a new directory

# This method takes in the path of the new directory.
#  If the FULL PATH is NOT specified, the NEW DIR is created in the CWD (current working directory)

#     >>> os.mkdir('test')
#     >>> os.listdir()
#     ['test']

# !Renaming a Directory or a File

# The rename() method can rename a directory or a file.

# The first argument is the old name and the new name must be supplies as the second argument.

#     >>> os.listdir()
#     ['test']
#     >>> os.rename('test','new_one')
#     >>> os.listdir()
#     ['new_one']

#! Removing Directory or File

# A file can be removed (deleted) using the remove() method.

# Similarly, the rmdir() method removes an empty directory.

#     >>> os.listdir()
#     ['new_one', 'old.txt']
#     >>> os.remove('old.txt')
#     >>> os.listdir()
#     ['new_one']
#     >>> os.rmdir('new_one')
#     >>> os.listdir()
#     []

# However, note that rmdir() method can only remove empty directories.

# In order to remove a non-empty directory we can use the rmtree() method inside the shutil module.

#     >>> os.listdir()
#     ['test']
#     >>> os.rmdir('test')
#     Traceback (most recent call last):
#     ...
#     OSError: [WinError 145] The directory is not empty: 'test'
#     >>> import shutil
#     >>> shutil.rmtree('test')
#     >>> os.listdir()
#     []
