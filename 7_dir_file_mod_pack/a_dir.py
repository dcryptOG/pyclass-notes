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


import os

#  which provides us with many useful methods to work with directories (and files as well).

#! Get Current Directory

# *get CWD  os.getcwd() method.

os.getcwd()
# ?     'C:\\Program Files\\PyScripter'
# Returns CWD as a STRING.

# * The EXTRA BACKSLASH implies ESCAPE SEQUENCE.

# The print() function will render this properly.

print(os.getcwd())

# ==========================#==========================


# *get CWD as BYTES OBJECT

# print(os.getcwdb())
# ?     b'C:\\Program Files\\PyScripter'
# todo DeprecationWarning: The Windows bytes API has been deprecated, use Unicode filenames instead


# ==========================#==========================

print('Passing an ASCII string')
print(list(os.walk(r'C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples')))

print('\nPassing a Unicode string')
print(list(os.walk(u'C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples')))
# [(u'C:\\example', [], [u'file.txt'])]

# ==========================#==========================


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
# os.listdir()

print('\nos.listdir\n')
print(os.listdir())

# ? listdir()  lists all FILES and SUB-DIRs inside a DIR

# todo        input path
# todo       returns a list of sub directories and files in that path.

# ? If NO PATH is specified, it returns from the CWD(current working directory).

#     >>> print(os.getcwd())

print(os.listdir('C:\\Users'))
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
# *need full path

os.mkdir('C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples\\test')

print(os.listdir('C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples'))
#     ['test']


# !Renaming a Directory or a File


# * The rename()
# ? method can rename a directory or a file.
# 1st ARG is the OLD NAME and 2nd ARG is the NEW NAME.


data_folder = "dir_examples\\"

file_to_open = data_folder + "raw_data.txt"

f = open(file_to_open, 'w')

f.write('Hello World')
f.write('\nThis is our new text file')

# FILE PATH open("C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples")
# can also use file.writelines() METHOD

print(f.read())

f.close()

# * remove() ==  A FILE can be REMOVED (deleted)

#     >>> os.listdir()
#     ['new_one', 'old.txt']
#     >>> os.remove('old.txt')
#     >>> os.listdir()

# *rmdir() method removes an empty directory.

os.rmdir('C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples\\new_one')

print(os.listdir('C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples'))
print(os.listdir('C:\\Users\\Geoff\\Desktop\\python-class\\pyclass-notes\\7_dir_file_mod_pack\\dir_examples'))
#     ['new_one']

# NOTE that rmdir() method can ONLY REMOVE EMPTY DIR.

# *rmtree() == (inside the shutil module removes a NON-EMPTY DIR.

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
