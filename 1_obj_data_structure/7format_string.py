# STRING INTERPOLATION: placing variable into a string
# TODO ADD MORE AT END LINKS
#! 2 STRING INTERPOLATION methods

# * 1: .format()
# * 2: f-strings(formatted string liaterals)

# EXAMPLE .format()
print("INPUT: \t'This is a string {}'.format('inserted')")
print('OUTPUT:\t This is a string {}'.format('inserted'))

print("'\nINPUT:\t The {2} {1} {0}'.format('fox', 'brown', 'quick')")
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print("'\nINPUT:\tThe {0} {0} {0}'.format('fox', 'brown', 'quick')")
print('OUTPUT\t The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print("'\nINPUT:\t The {f} {b} {q}'.format(f='fox', b='brown', q='quick')")
print('OUTPUT:\t The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

#! EXAMPLE FLOAT FORMATTING
#! SYNTAX "{VALUE:WIDTH.PRECISION f}"
#WIDTH is whitespace
# PRECISION places after decimal
print('\nSYNTAX "{VALUE:WIDTH.PRECISION f}"')
print("\float formatting\n\nWIDTH is whitespace\nPRECISION places after decimal")
result = 100/777
print("The result was {}".format(result))
print("The result was {r}".format(r=result))
print('\n"The result was {r:1.3f}".format(r=result)')
print("The result was {r:1.3f}".format(r=result))

#! EXAMPLE f-string
print('\nSYNTAX f-string')
name = "Geoff"
age = 29
print("\nf'Hello my name is {name}'")
print(f'Hello my name is {name}')
print("f'{name} is {age} years old'")
print(f'{name} is {age} years old')


#! Here are some basic argument specifiers you should know:

# https://www.learnpython.org/en/String_Formatting

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# REVIEW NOTEBOOK FOR SECTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/00-Python%20Object%20and%20Data%20Structure%20Basics
