# What is recursion in Python?

# Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing each other.
#  Any object in between them would be reflected recursively.

# ! Python Recursive Function

# *RECURSIVE FUNCTION =  function to call itself.

# Following is an example of recursive function to find the factorial of an integer.

# Factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

# An example of a recursive function to find the factorial of a number


def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))


num = 4
print("The factorial of", num, "is", calc_factorial(num))

#! In the above example, calc_factorial() is a recursive functions as it calls itself.

# When we call this function with a positive integer, it will recursively call itself by decreasing the number.

# Each function call multiples the number with the factorial of number 1 until the number is equal to one. This recursive call can be explained in the following steps.


# calc_factorial(4)              # 1st call with 4
# 4 * calc_factorial(3)          # 2nd call with 3
# 4 * 3 * calc_factorial(2)      # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1                  # return from 4th call as number=1
# 4 * 3 * 2                      # return from 3rd call
# 4 * 6                          # return from 2nd call
# 24                             # return from 1st call

# * BASE CONDTION = Our recursion ends when the number reduces to 1.

# Every recursive function MUST HAVE BASE CONDTION that stops the recursion OR else the function calls itself INFINITELY.

# ? Advantages of Recursion

#     Recursive functions make the code look clean and elegant.
#     A complex task can be broken down into simpler sub-problems using recursion.
#     Sequence generation is easier with recursion than using some nested iteration.

# ! Disadvantages of Recursion

#     Sometimes the logic behind recursion is hard to follow through.
# *     Recursive calls are EXPENSIVE (INEFFICIENT) as they use a lot of MEMORY and TIME.
# *     Recursive functions are hard to debug.
