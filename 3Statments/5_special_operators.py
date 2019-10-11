# few built-in functions and "operators" in Python that don't fit well into any category,\
# range

#! RANGE function
# The range function allows you to quickly generate a list of integers
# There are 3 parameters you can pass, a start, a stop, and a step size.

from random import shuffle
from random import randint
print('EX1')
mylist = [1, 2, 3]
for num in range(10):
    print(f'output ex1: {num}')

print('\nrange function allows you to quickly generate a list of integers')
print('3 parameters\nstart\nstop\nstep size')
print('range(0, 11)')
print('up to not including 11')
range(0, 11)
#
print('Range is Generator function so to cast list list()\n')
print('list(range(0, 11)')
print(list(range(0, 11)))
list(range(0, 12))
print('\nlist(range(0, 11, 2))')
print(list(range(0, 11, 2)))
list(range(0, 100, 10))

#! ENUMERATE
print('\nEnumerate')
index_count = 0
word = 'abcde'
print('for letter in "abcde":\n    print("".format(index_count, letter)\n    index_count+=1')

for letter in word:
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

print('\nvs. enumerate')

print('for i, letter in enumerate("abcde"):\n    print("".format(i, letter))')

for i, letter in enumerate(word):
    print("At index {} the letter is {}".format(i, letter))

print("\nlist(enumerate('abcde'))")
print(list(enumerate('abcde')))

#! ZIP - create list of tuples
# * zip is opposite of enumerate

print('\n\t\tZIP opposite of ENUMERATE')
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print("list1 = {}\nlist2 = {}".format(list1, list2))

print('\nzip(list1, list2)\n output:')
print("output:", zip(list1, list2))
print('\nlist(zip(list1, list2))')
print("output:", list(zip(list1, list2)))

print('\nfor item1, item2 in zip(list1, list2):\n    print("".foramt(item1, item2))')

for item1, item2 in zip(list1, list2):
    print('For this tiple, first item was {} and second item was {}'.format(item1, item2))

#! IN operator - can also use to check if object is in list
print('\n in OPERATOR********************')
print('"x" in ["x", "y", "z"]\n returns Boolean')
print('x' in ['x', 'y', 'z'])
print('x' in [1, 2, 3, ])
# useful for dictionaries
print('\n in operator & dictionaries')
d = {'key1': 345}
print(d)
print("345 in d.keys()", "\noutput:", 345 in d.keys())
print("345 in d.values()", "\noutput:", 345 in d.values())

#!Min and max
print('\nmin() and max()')
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

#! Random Python includes random libararies
print('\nrandom')
print("randint(0,100)")
# print(shuffle(mylist))
print(randint(0, 100))
print('RANDINT - oputput can be saved as var')

print('\nshuffle')
shuffle(mylist)
print('shuffle(mylist)\nprint(mylist)')
print("output:", mylist)
print('*Shuffle is INPLACE FUNCITON - operates in place on that list')
# input

result = input('\nEnter something into this box: ')
print(result)
print(type(result))
favnum = int(input('What is your favorite number? '))
print("favnum = int(input('What is your favorite number? '))")
print("output:", favnum)
print(type(favnum))
