# LIST COMPREHENSIONS
# *[ EXPRESSION for item in list if conditional ]
# todo EXPRESSION is first instead of last in list comprehension
# This is equivalent to:

# * for item in list:
#     if conditional:
#  ?       expression
print('List Comprehensions - append is read as default\n')
print("mylist = []\nmystring = 'hello'\nfor letter in mystring:\n    mylist.append(letter)")

mylist = []
mystring = 'hello'
for letter in mystring:
    mylist.append(letter)
print(mylist)

# easier way to make list of string
# APPEND IS DEFAULT IN LIST COMPREHENSIONS

list1 = [letter for letter in mystring]

# letter is temporary var word
print("\nlist1 = [letter for letter in mystring]")
print(list1)

# built in for loop inside of brackets
lst = [x for x in 'word']
print("output: ", lst)

#! EX2
print("\nEX2\n", "lst = [x**2 for x in range(0, 11)]")
lst = [x**2 for x in range(0, 11)]
print("output: ", lst)
lst = [x**2 for x in range(0, 11) if x % 2 == 0]
print("\nx%2==0 check if even")
print("lst = [x**2 for x in range(0, 11) if x % 2 == 0]")
print("output: ", lst)
lst = [x if x % 2 == 0 else 'odd' for x in range(0, 11)]
print("lst = [x if x % 2 == 0 else 'odd' for x in range(0, 11)]")
print("output: ", lst)

#! Ex3
print("\nEX3\n", "lst = [x for x in range(0, 11)]")
lst = [x for x in range(0, 11)]
print("output: ", lst)


#! EX4
print("\nEX4\n", "celsius = [0, 10, 20.1, 34.5]\n",
      "fahrenheight = [((9/5)*temp + 32) for temp in celsius]")

celsius = [0, 10, 20.1, 34.5]
fahrenheight = [((9/5)*temp + 32) for temp in celsius]
print("output: ", fahrenheight)

#! EX5 NESTED LIST COMPREHENSIONS
print("\nEX5\n", "lst = [x**2 for x in [x**2 for x in range(11)]]")

lst = [x**2 for x in [x**2 for x in range(11)]]
print("output: ", lst)

#! EX 6
print("\nEX6\n", "mylist = []\nfor x in [2, 4, 6]:\n    for y in [1, 10, 1000]:\n        mylist.append(x*y)")
mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)
print("output: ", mylist)
print("\nmylist = [x*y for x in [2,4,6] for y in [1,10,1000]]")
mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print("output: ", mylist)

# for x in range(1, 101):
#     if x % 3 == 0 and x % 5 == 0:
#         print("Fizz Buzz")
#     elif x % 3 == 0 and x % 5 != 0:
#         print('Fizz')
#     elif x % 3 != 0 and x % 5 == 0:
#         print('Buzz')
#     else:
#         print(x)
