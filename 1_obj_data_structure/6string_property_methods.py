#name = "Geoff"
#name[0] = 'P'
# error

# STRINGS IMMUTABLE cannot reassign letter

# concat 2 steps
name = "Sam"
# 1. REASSIGN VARAIBLE
last_letters = name[1:]
print(last_letters)
# 2. CONCAT
print('P' + last_letters)

# ex 2  CONCAT

x = 'Hello World'
x = x + " it is beautiful outside!"
print(x)

# string multiplcation

letter = 'z'
print('letter*10')
print(letter*10)

# USEFUL METHODS

# UPPER METHOD
x = 'Hello Word'
print('x.upper()')
print(x.upper())
print('x.lower()')
print(x.lower())

# STRING METHOD converts a string to a list
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
