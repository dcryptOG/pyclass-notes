#name = "Geoff"
#name[0] = 'P'
# error

#! STRINGS IMMUTABLE cannot reassign letter

# ? concat 2 steps
name = "Sam"

# * 1. REASSIGN VARAIBLE
last_letters = name[1:]
print(last_letters)

# * 2. CONCAT
print('P' + last_letters)

# todo EX2  CONCAT
print('\n')
x = 'Hello World'
x = x + " it is beautiful outside!"
print(x)

#!STRING MULTIPLICATION

print('\nEX String multiplcation')
letter = 'z'
print('letter*10')
print(letter*10)

#! USEFUL METHODS

# * UPPER METHOD
x = 'Hello Word'
print('\nSTING METHODS')
print('\nx.upper()')
print(x.upper())
print('\nx.lower()')
print(x.lower())

#! SPLIT METHOD converts a STRING into a LIST
x = 'Hi this is a string'
print('\nSPLIT METHOD')
print('x')
print('x.split()')
print("output: ", x.split())
print('.SPLIT() selects each wrod turns into a list of strings')
print("\nx.split('i')")
#output: ['Hi', 'this', 'is', 'a', 'string']
print(x.split('i'))
#output: ['H', ' th', 's ', 's a str', 'ng']
# HAS WHITESPACE
