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
# FILE PATH open("C:\\Users\\UserName\\Folder\\test.txt")
# can also use file.writelines() METHOD
file.close()
print('file.close()')

# READ FILE
print('\n file=open("testfile.txt", "r"')
file = open('testfile.txt', 'r')
print(file.read())
# print(file.read(3))
print('\nRESET TO REREAD FILE file.seek(0)')
# RESESETS TO REREAD FILE
file.seek(0)
print(file.read())
file.seek(0)
# .READLINES METHOD returns LIST of STRINGS
print(file.readlines)
file.seek(0)
file.close

#! WITH STATEMENT
# NO NEED TO CLOSE
print('\nWITH STATEMENT')
with open('testfile.txt', 'r') as my_file:
    contents = my_file.read()
print(contents)
# write with with
with open('text.txt', 'r') as f:
    print(f.read())
with open('text.txt', 'a') as f:
    f.write('\nAPPEND')
with open('text.txt', 'r') as f:
    print(f.read())

#! add notes Method Name Use Explanation
#!Add notes that for loops for accessing files is most common
# *this mehtod returns a file obj
