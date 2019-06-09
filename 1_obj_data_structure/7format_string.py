# STRING INTERPOLATION: placing variable into a string

# 2 STRING INTERPOLATION methods

# 1: .format()
# 2: f-strings(formatted string liaterals)

# EXAMPLE .format()
print("'This is a string {}'.format('inserted')")
print('This is a string {}'.format('inserted'))

print("'The {2} {1} {0}'.format('fox', 'brown', 'quick')")
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print("'The {0} {0} {0}'.format('fox', 'brown', 'quick')")
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print("'The {f} {b} {q}'.format(f='fox', b='brown', q='quick')")
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

# EXAMPLE float formatting
# SYNTAX "{VALUE:WIDTH.PRECISION f}"
#WIDTH is whitespace
# PRECISION places after decimal
print('\nSYNTAX "{VALUE:WIDTH.PRECISION f}"')
print("float formatting\nWIDTH is whitespace \nPRECISION places after decimal")
result = 100/777
print("The result was {}".format(result))
print("The result was {r}".format(r=result))
print('"The result was {r:1.3f}".format(r=result)')
print("The result was {r:1.3f}".format(r=result))

# EXAMPLE f-string
print('\nSYNTAX f-string')
name = "Geoff"
age = 29
print("\nf'Hello my name is {name}'")
print(f'Hello my name is {name}')
print("f'{name} is {age} years old'")
print(f'{name} is {age} years old')


# REVIEW NOTEBOOK FOR SECTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/00-Python%20Object%20and%20Data%20Structure%20Basics
