# FILES
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
print('FILES I/O input output')
# open files
print('Python has a built-in open function that allows us to open and play with basic file types. First we will need a file though. ')
print('\n SYNTAX \n r = read mode \n w = write mode \n a = appending mode \n r+ = special read and write mode \n mode w+ = for writing and readin \n x for creating writing new file')

#!open() WRITE FILE PYTHON

#! w can OVERWRITE EXISTING FILE or CREATE NEW

print('\n file = open("testfile.txt", "w"')
file = open('testfile.txt', 'w')
file.write('Hello World')
file.write('\nThis is our new text file')
# *writes in string

# ? Add a string to the endof the file. filevar must refer to a file that has been opened for writing
# FILE PATH open

# ("C:\\Users\\UserName\\Folder\\test.txt")
# can also use file.writelines() METHOD

file.close()
print('file.close()')

# * READ FILE
print('\nREAD FILE')
# ?Read and return a string of n characters, or the entire file as a string if n is not provided

print('\n file=open("testfile.txt", "r"')
file = open('testfile.txt', 'r')
# *contents = file.read()
# *Method makes file a list instead of File Obj
#!print(f'first 10 chars:\n {contents[:10]}')
print('file.read()\n', file.read())
# ?Read part of a file
# first 10 chars
#!most common method to read file is for loop
# * for lin in file:
# *    print(lin.strip())

# print(file.read(n))
print('\nRESET TO REREAD FILE file.seek(0)')
# * RESESETS TO REREAD FILE
file.seek(0)
print(file.read())
file.seek(0)
# .READLINES METHOD returns LIST of STRINGS
print(file.readlines)
file.seek(0)
file.close

# *file.readline(n)
# Read and return the hext line of afile with all text up to and including the newline character. If n is provided as a parameter, the only n characters will be returned if the line is longer than n. NOe the parameter n is not supported int he browser version of Python, and is rarely used in practice

# *file.readlines(n)
# Returns a list of strings, each representing a single ine of the file. If n is not provided then all lines of the file are returned. If n is provcided the n characters are read but n is rounded up so that an entire line is returned. Note like readline readlines ignores the parameter n in browser

#! WITH STATEMENT
# NO NEED TO CLOSE
print('\nWITH STATEMENT')
with open('testfile.txt', 'r') as my_file:
    contents = my_file.read()
print(contents)
print(type(contents))
# write with with
with open('text.txt', 'r') as f:
    print(f.read())
    print(len(f.read()))
with open('text.txt', 'a') as f:
    f.write('\nAPPEND')
with open('text.txt', 'r') as f:
    print(f.read())
with open('text.txt', 'r') as f:
    for line in f:
        print(line)
        print(line.split()[0])
        # print first word
# *work with any file
fname = "squares.txt"
with open(fname, 'r') as f:
    f.readlines()
    f.read()
    for line in f:
        pass
    # do something with each line


#!Fastest processing time for reading a file
print('\nFastest')

file = open("fastest.txt", "r")
num_lines = 0
for aline in file:
    values = aline.split()
    print(values)
    num_lines += 1
print(num_lines)
# count number of lines fast


#! add notes Method Name Use Explanation
#!Add notes that for loops for accessing files is most common
# *this mehtod returns a FILE OBJ

# ?Note that Python pathnames follow the UNIX conventions (Mac OS is a UNIX variant), rather than the Windows file pathnames that use : and \. The Python interpreter will translate to Windows pathnames when running on a Windows machine; you should be able to share your Python program between a Windows machine and a MAC without having to rewrite the file open commands.

# *absolute path begins with a /

#! INFILE OUTFILE EX
filename = "squares.txt"
outfile = open(filename, "w")
for number in range(13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
