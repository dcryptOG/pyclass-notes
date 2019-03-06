# Statements C++

# if (a>b) {
#   a = 2;
#   b = 4;
# }

# PYTHON statements

# if a > b:
#     a = 2
#     b = 4

# PYTHON USES WHITESPACE
# PYTHON USES COLON

# Other Languages

# if (x)
#     if(y)
#         code-statement;
# else
#     another-code-statement;

# if x:
#     if y:
#         print('hello')
# else:
#     print('bye')

# =======================================================
# if, elif, else Statements

# CONTROL FLOW = use logic for async code execution

# if Statements in Python tellS the computer to perform alternative actions based on a certain set of results.

# elif and else statements, which allow us to tell the computer:

# "Hey if this case happens, perform some action. Else, if another case happens, perform some other action. Else, if none of the above cases happened, perform this action."


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
hungry = False
if hungry:
    print('FEED ME!')
else:
    print("I'm not hungry")

# MULTIPLE BRANCHES
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
