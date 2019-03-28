# while Loops
# while statement will repeatedly execute a single statement or group of statements as long as the condition is true.

# Program to iterate through a list using indexing

# In while loop, test expression is checked first.
# The body of the loop is entered only if the test_expression evaluates to True.
# After one iteration, the test expression is checked again.
# This process continues until the test_expression evaluates to False.
# TODO ELSE in WHILE IS WHEN CONDITION IS FALSE
# Program to add natural
# numbers upto
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

# The else part is executed if the condition in the while loop evaluates to False.
# The while loop can be terminated with a break statement. In such case, the else part is ignored.
# Hence, a while loop's else part runs if no break occurs and the condition is false.
# Here is an example to illustrate this.

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

########################################################

print('while statement will repeatedly execute\n a single statement or group of statements\n as long as the condition is true. ')
# Ex1
x = 0
print("while x < 10:\n    print('x is currently: ', x)\n    print(' x is still less than 10, adding 1 to x')\n    x += 1")
while x < 10:
    print('x is currently:', x)
    print(' x is still less than 10, addint 1 to x')
    x += 1

x = 0

# while else
print('\nWHILE ELSE statement')
print("while x < 10:\n    print('x is currently: ', x)\n    print('format string')\n    x += 1")
print('else:\n    print(ALL DONE')
while x < 10:
    print(f'The current value of x is {x}')
    x += 1

else:
    print('ALL DONE')

# BREAK CONTINUE PASS
print('\n creak continue pass')
# BREAK breaks out of the current closest enclosing loop
# CONTINUE: goes to the top of the closest enclosing loop
# pass: does nothing... results NO OPERATION (NOP).
print('break: breaks out of the current closest enclosing loop')
print('continue: re-iterates TOP of enclosing loop')
print('pass: Does nothing at all')

# GENERAL SYNTAX
# while test:
#     code statement
#     if test:
#         break
#     if test:
#         continue
# else:

# IF ELSE CONTINUE
y = [1, 2, 3]

for item in y:
    pass
# use pass keyword as placeholder for a codeblock
print('end of my script')

print('adding statements\nif x==3:\n    print("x==3")\nelse:\n    continue')

x = 0

while x < 10:
    print(f'x = {x}')
    x += 1
    if x == 3:
        print('x==3')
    else:
        print('continuing...')
        continue

print('\n while as string')

# WHILE STATEMENTS can run INFINITELY...AVOID
# AVOID INFINTITELY RUNNING HWILE STATEMENTS

print('DONT RUN THIS INFINITE CODE\nwhile True:\n    print("fuck infinte loop broked"')

print('\n if letter =="a":\n    print(letter)\nelse:\n    continue')
mystring = 'abcdefghijklmnopqrstuvwxyz'

for letter in mystring:
    if letter == 'a':
        print(f'output: {letter}')
    else:
        continue

print('\nBREAK STATEMENT')
print("while x < 5:\n    if x == 2:\n        break\n    print(x)\n    x+=1")
x = 0
while x < 5:
    if x == 2:
        break
    print(f'output: {x}')
    x += 1
