# for loop acts as an iterator in Python

# SYNTAX
print('for item in seq-obj:\n    statements...do stuff')
# Iterating over a sequence is called traversal.
# for val in sequence:
# 	Body of for
# Loop continues until we reach the last item in the sequence.
print('\n')

###############################################################

# Program to iterate through a list using indexing
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
# ex 4 LOOPS in STRINGS
print('\n Loops in Strings')
########################################################
for letter in 'This is a string.':
    print(letter)
for _ in 'Hello World':
    print('no variable')

# LOOPS in TUPLES
print('\nTuples in loops')
tup = (1, 2, 3, 4, 5)
print('for t in tup:\n    print(t)')
for t in tup:
    print(t)

# EX 6 LIST  with TUPLES
print('\n List with Tuples - ')
########################################################
list2 = [(2, 4), (6, 8), (10, 12)]
for tup in list2:
    print(tup)
print('\n TUPLE UNPACKING')
for a, b in list2:
    print(a)
    print(b)

# EX7 Dictionaries
print('\n Dictionaries')
########################################################
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

# include 3 dicitonary methods
print(d)
print('for k, v in d.items():\nlist(d.keys())\nsorted(d.values())')

for k, v in d.items():
    print(k)
    print(v)

list(d.keys())

sorted(d.values())
