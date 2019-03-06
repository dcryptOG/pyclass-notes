# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

# The first two terms are 0 and 1.
# All other terms are obtained by adding the preceding two terms.
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
import random
import itertools
import cmath
import calendar
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto", nterms, ":")
    while count < nterms:
        print(n1, end=' , ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

# Note: To test this program, change the value of nterms.

# Here, we store the number of terms in nterms. We initialize the first term to 0 and the second term to 1.

# If the number of terms is more than 2, we use a while loop to find the next term in the sequence by adding the preceding two terms. We then interchange the variables(update it) and continue on with the process.

# You can also solve this problem using recursion: Python program to print the Fibonacci sequence using recursion.

# Python program to display the Fibonacci sequence up to n-th term using recursive functions


def recur_fibo(n):
    """Recursive function to
    print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


# Change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

# In this program, we store the number of terms to be displayed in nterms.

# A recursive function recur_fibo() is used to calculate the nth term of the sequence. We use a for loop to iterate and calculate each term recursively.

# Visit here to know more about recursion in Python.

# A positive integer is called an Armstrong number of order n if

# abcd... = an + bn + cn + dn + ...

# In case of an Armstrong number of 3 digits, the sum of cubes of each digits is equal to the number itself. For example:

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

# Source Code: Check Armstrong number (for 3 digits)

# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Output 1

# Enter a number: 663
# 663 is not an Armstrong number

# Output 2

# Enter a number: 407
# 407 is an Armstrong number

# Here, we ask the user for a number and check if it is an Armstrong number.

# We need to calculate the sum of cube of each digit. So, we initialize the sum to 0 and obtain each digit number by using the modulus operator %. Remainder of a number when it is divide by 10 is the last digit of that number. We take the cubes using exponent operator.

# Finally, we compare the sum with the original number and conclude that it is Armstrong number if they are equal.
# Source Code: Check Armstrong number of n digits

num = 1634

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# You can change the value of num in the source code and run again to test it.

# Program to check Armstrong numbers in certain interval

lower = 100
upper = 2000

# To take input from the user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):

    # order of number
    order = len(str(num))

    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)

# Output

# 153
# 370
# 371
# 407
# 1634

# Here, we have set the lower limit 100 in variable lower and upper limit 2000 in variable upper. We have used for loop to iterate from variable lower to upper. In iteration, the value of lower is increased by 1 and checked whether it is an Armstrong number or not.

# You can change the range and test out by changing the variables lower and upper. Note, the variable lower should be lower than upper for this program to work properly.

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)

# Note: To test the program, change the value of num. Try negative numbers as well.

# Here, the number whose factorial is to be found is stored in num and we check if the number is negative, zero or positive using if...elif...else statement. If the number is positive, we use for loop and range() function to calculate the factorial.

# Python program to find the factorial of a number using recursion


def recur_factorial(n):
    """Function to return the factorial
    of a number using recursion"""
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


# Change this value for a different result
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

# check is the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))

# Here, the number is stored in num and use recursive function recur_factorial() to compute the product up to that number.

# FIND FACTORS

# Python Program to find the factors of a number

# define a function


def print_factors(x):
    # This function takes a number and prints the factors

    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)

# Then we display its factors using the function print_factors().
#  In the function, we use a for loop to iterate from 1 to that number and only print it if, it perfectly divides our number.
# Here, print_factors() is a user-defined function.

###############
# Python program to check if the input year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# Python program to display calendar of given month of the year

# import module

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

# The standard form of a quadratic equation is:

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module

a = 1
b = 5
c = 6

# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1, sol2))

# Enter a: 1
# Enter b: 5
# Enter c: 6
# The solutions are (-3+0j) and (-2+0j)

# We have imported the cmath module to perform complex square root. First we calculate the discriminant and then find the two solutions of the quadratic equation.

# You can change the value of a, b and c in the above program and test this program.

# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules

# make a deck of cards
deck = list(itertools.product(range(1, 14), [
            'Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

# Output

# You got:
# 5 of Heart
# 1 of Heart
# 8 of Spade
# 12 of Spade
# 4 of Spade

# Note: Run the program again to shuffle the cards.

# In program, we used the product() function in itertools module to create a deck of cards. This function performs the Cartesian product of the two sequence.

# The two sequence are, numbers from 1 to 13 and the four suits. So, altogether we have 13 * 4 = 52 items in the deck with each card as a tuple. For e.g. deck[0] = (1, 'Spade').

# Our deck is ordered, so we shuffle it using the function shuffle() in random module.

# Finally, we draw the first five cards and display it to the user. We will get different output each time you run this program as shown in our two outputs.

# Here we have used the standard modules itertools and random that comes with Python.
