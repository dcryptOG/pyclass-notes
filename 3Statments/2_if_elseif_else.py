# =======================================================
#! if, elif, else Statements

# * CONTROL FLOW = use logic for async code execution

# elif and else statements, which allow us to tell the computer:

# if case1:
#     perform action1
# elif case2:
#     perform action2
# else:
#     perform action3

if True:
    print('It was true!')

x = False

if x:
    print('x was True!')
else:
    print('I will be printed in any case where x is not True')
print('/n')
if 3 > 2:
    print("It's True!")
#
hungry = True
if hungry:
    print('FEED ME!')
else:
    print("I'm not hungry")

#! ELIF multiple branches
# loc stand for location
print('\n')
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank, moneh is coo!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('Where are you?')
#######################################################################
person = 'George'
print('\n')
if person == 'Sammy':
    print('Welcome Sammy')
elif person == 'George':
    print('Welcome George')
else:
    print("Welcome, what's your name?")

# INDENTATION - itis important to understand how indentation works for Python code structure

print('understand how indentation works in python')
