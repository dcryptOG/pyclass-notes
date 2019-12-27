# Notice that I’ve hardcoded the path using Unix-style forward slashes since I’m on a Mac. This will make Windows users angry.

from pathlib import Path, PureWindowsPath

# Technically this code will still work on Windows because Python has a hack where it will recognize either kind of slash when you call open() on Windows.
# But even still, you shouldn’t depend on that.
#  Not all Python libraries will work if you use wrong kind of slash on the wrong operating system — especially if they interface with external programs or libraries.

# And Python’s support for mixing slash types is a Windows-only hack that doesn’t work in reverse. Using backslashes in code will totally fail on a Mac:
# todo python for loop to make multiple directories

import os

data_folder = "file_examples"

# file_to_open = data_folder + "raw_data.txt"

# f = open(file_to_open)

# print(f.read())

# For all these reasons and more, writing code with hardcoded path strings is the kind of thing that will make other programmers look at you with great suspicion. In general, you should try to avoid it.


#! The Old Solution: Python’s os.path module

# Python's os.path module has lots of tools for working around these kinds of operating system-specific file system issues.

# You can use os.path.join() to build a string using the rightkind of slash for the current os

# import os.path

# data_folder = os.path.join("source_data", "text_files")

# file_to_open = os.path.join(data_folder, "raw_data.txt")

# f = open(file_to_open)

# print(f.read())

# This code will work perfectly on both Windows or Mac. The problem is that it’s a pain to use. Writing out os.path.join() and passing in each part of the path as a separate string is wordy and unintuitive.

# Since most of the functions in the os.path module are similarly annoyint to use, developers often forget to use them even when they know better. This leads to a lot of cross-platform bugs.

# The Better Solution: Python 3’s pathlib!

#! Python 3.4 introduced a new standard library for dealing with files and paths called pathlib — and it’s great!

# To use it, you just pass a path or filename into a new Path() object using forward slashes and it handles the rest:

# from pathlib import Path

# data_folder = Path("source_data/text_files/")

# file_to_open = data_folder / "raw_data.txt"

# f = open(file_to_open)

# print(f.read())

# notice two things here:

# 1 Use forward slashes with pathlib functions. The path() object will convert forward slashes into the correct kind of slash for the current os.

# 2 If yo8uw ant to add on to the path, you can use the / operator directly in your code. Say goodby to typing out os.path.join(a,b) over and over

# And if that’s all pathlib did, it would be a nice addition to Python — but it does a lot more!

# For example, we can read the contents of a text file without having to mess with opening and closing the file:

# from pathlib import Path

# data_folder = Path("source_data/text_files/")

# file_to_open = data_folder / "raw_data.txt"

# print(file_to_open.read_text())

# in fact pathlib makes most  standard file operations quick and easy

# from pathlib import Path

# filename = Path("source_data/text_files/raw_data.txt")

# print(filename.name)
# # prints "raw_data.txt"

# print(filename.suffix)
# # prints "txt"

# print(filename.stem)
# # prints "raw_data"

# if not filename.exists():
#     print("Oops, file doesn't exist!")
# else:
#     print("Yay, the file exists!")

# ?Use pathlib to explicitly convert a unix path into a windows formattted path

# from pathlib import Path, PureWindowsPath

# filename = Path("source_data/text_files/raw_data.txt")

# # Convert path to Windows format
# path_on_windows = PureWindowsPath(filename)

# print(path_on_windows)
# # prints "source_data\text_files\raw_data.txt"

# ?And if you really want to use backslashes in your code safely, you can declar your path as windows-formatted and pathlib can convert it to work on the current os:

# from pathlib import Path, PureWindowsPath

# # I've explicitly declared my path as being in Windows format, so I can use forward slashes in it.
# filename = PureWindowsPath("source_data\\text_files\\raw_data.txt")

# # Convert path to the right format for the current operating system
# correct_path = Path(filename)

# print(correct_path)
# # prints "source_data/text_files/raw_data.txt" on Mac and Linux
# # prints "source_data\text_files\raw_data.txt" on Windows

# ? If you want to get fancy, you can even use pathlib to do things like resolve relative file paths, parse network share paths and generate file:// urls. Here’s an example that will open a local file in your web browser with just two lines a code:

# from pathlib import Path
# import webbrowser

# filename = Path("source_data/text_files/raw_data.txt")

# webbrowser.open(filename.absolute().as_uri())
