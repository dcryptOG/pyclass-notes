# for loop acts as an iterator in Python

# SYNTAX
print('for item in seq-obj:\n    statements...do stuff')

# Iterating over a sequence is called traversal.
#! There are TWO types of LOOPS in Python,
# todo                           1.  for
# todo                           2 while.

#! The "for" loop

#!SYNTAX
# ? for item in items:
#    do stuff...

# *EX

print('Less efficient range method')

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# For loops can iterate over a sequence of numbers using the
# * "RANGE" and "XRANGE" functions.
#! RANGE vs XRANGE is that the

# ? RANGE FUNCTION returns a NEW LIST with numbers of that specified range,
#!  whereas XRANGE returns an ITERATOR, which is MORE EFFICIENT.

#! (Python 3 uses the RANGE FUNCTION, which acts like XRANGE.
# Note that the range function is zero based.

print('\nMore Efficient range() or xrange method')

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

print('\n')

#! Program to iterate through a list using indexing


print('EX for loop used with range')
genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])

#######################################################

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    print(num)
print('\nfor num in list1: \n if num 2 % == 0: \n print(num)\n else: \n print(f"odd number: ")')
########################################################

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number: {num}')
print('\n')
########################################################
list_sum = 0

for num in list1:
    list_sum = list_sum + num
    print(list_sum)

# using shorthand +=

list_sum = 0

for num in list1:
    list_sum += num
    print(list_sum)
# *
print('\n')
print(list_sum)
#! ex 4 LOOPS in STRINGS
print('\n EX4 Loops in Strings')

for letter in 'This is a string.':
    print(letter)

for _ in 'Hello World':
    print('no variable')

#! EX5 LOOPS in TUPLES
print('\nEX 5 Tuples in loops')
tup = (1, 2, 3, 4, 5)
print('for t in tup:\n    print(t)')
for t in tup:
    print(t)

#! EX 6 TUPLE UNPACKING LIST  with TUPLES
print('\n EX 6 List with Tuples UNPACKING - ')

list2 = [(2, 4), (6, 8), (10, 12)]
for tup in list2:
    print(tup)
print('\n TUPLE UNPACKING')
for a, b in list2:
    print(a)
    print(b)

#! EX7 Dictionaries
print('\nEX7 Dictionaries')

print("d = {'k1': 1, 'k2': 2, 'k3': 3}\nforitem in d:\n\tprint(item)")

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

print('\nThis only prints out keys')
# * only prints out keys

# include 3 dicitonary methods
print(d)

print('\nTo print out key valuese use k,v\n')
print('for k, v in d.items():\nlist(d.keys())\nsorted(d.values())')

for k, v in d.items():
    print(k)
    print(v)

list(d.keys())

sorted(d.values())
