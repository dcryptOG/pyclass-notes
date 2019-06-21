
# Functions and Methods Homework

# Complete the following questions:

#! Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as $$\frac{4}{3} πr^3$$


import string


import string
import math


def vol_sphere(rad):
    return round(((4/3)*(math.pi)*(rad**3)), 2)


print(vol_sphere(2))


def vol_sphere2(rad):
    # return '{:0.2f}'.format((4/3)*(math.pi)*(rad**3))
    return "%.2f" % ((4/3)*(math.pi)*(rad**3))


print(vol_sphere2(2))


#! Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if low < num < high:
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is outside the range {low} and {high}'


print(ran_check(3, 1, 10))


print(ran_check(5, 2, 7))

# 5 is in the range between 2 and 7

# If you only wanted to return a boolean:
# ? alt

#! def ran_check(num,low,high):
#     #Check if num is between low and high (including low and high)
#     if num in range(low,high+1):
#         print('{} is in the range between {} and {}'.format(num,low,high))
#     else:
#         print('The number is outside the range.')


def ran_bool(num, low, high):
    return low < num < high


print(ran_bool(3, 1, 10))

# True

# !Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# ? HINT: Two string methods that might prove useful: .isupper() and .islower()

# No. of Upper case characters : 4
# No. of Lower case Characters : 33
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print([c for c in s if c.isupper()])
print([c for c in s if c.islower()])


def up_low(s):
    return f'No. of upper case: {len(list(filter(lambda x: x.isupper(), s)))}\n No. of lower case: {len(list(filter(lambda x: x.islower(), s)))}'

# *filter() faster? check process time


def up_low_2(s):
    return f'No. of upper case: {len([c for c in s if c.isupper()])} \n No. of lower case: {len([c for c in s if c.islower()])}'


print(up_low_2('Hello Mr. Rogers, how are you this fine Tuesday?'))


# def up_low(s):
#     up = 0
#     low = 0
#     for c in s:
#         if c.isupper() is True:
#             up += 1
#         else:
#             low += 1
#     return "Totall upper {} total lower {}".format(up, low)


def up_low_3(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    return d


print(up_low_3('Hello Mr. Rogers, how are you this fine Tuesday?'))

# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33

#! Write a Python function that takes a list and returns a new list with unique elements of the first list.

lst1 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(lst):
    return list(set(lst1))


print(unique_list(lst1))

#! alt
#! def unique_list(lst):
#     # Also possible to use list(set())
#     x = []
#     for a in lst:
#         if a not in x:
#             x.append(a)
#     return x

# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# [1, 2, 3, 4, 5]

# ! Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    return list(map(lambda x: x*2, numbers))
#     pass


print(multiply([1, 4, 5, -3]))

print(multiply([1, 2, 3, -4]))


def multiply_2(nums):
    total = 1
    for x in nums:
        total *= x
    return total


nums = [1, 2, 3, 4]
print(multiply_2([1, 2, 3, 4]))


# ! Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def palindrome(s):

    # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('helleh'))


def palindrome_2(s):
    table = str.maketrans(dict.fromkeys(' .!#&,'))
    return s.translate(table) == s[::-1].translate(table)


print(palindrome('helleh'))
print(palindrome('nurses run'))
# True

# Hard:

# ! Write a Python function to check whether a string is pangram or not.

# ? Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# ? Hint: Look at the string module

# * try without making list and sort

# *help(string)

# * string.ascii_lowercase
# * 'abcdefghijklmnopqrstuvwxyz'

# If you really need a list:

# *list(string.ascii_lowercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# And to do it with range

abcs = list(map(chr, range(97, 123)))
abcs_2 = list(map(chr, range(ord('a'), ord('z')+1)))

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Hint: Look at the string module

# import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    table = str.maketrans(dict.fromkeys(' .'))
    return list(alphabet) == sorted(set(str1.translate(table).lower()))
# *could also use len() instead of sorted


print(ispangram("The quick brown fox jumps over the lazy dog"))


def is_pangram_2(sentence):
    lookup = [0] * 26
    sentence = sentence.lower()
    for char in sentence:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            lookup[index] += 1
    # All function checks and returns True only if all the elements in the
    # given array is 'Truthy'. Here, 0 will be evaluated as 'Falsy' and any
    # occurrance greater than 0 will evaluate as 'Truthy'
    return f'{all(lookup)} has {len(lookup)}'
# True


print(is_pangram_2("The quick brown fox jumps over the lazy dog"))
# string.ascii_lowercase


# 'abcdefghijklmnopqrstuvwxyz'
print(ispangram('abcdefghijklmnopqrstuvwxyz'))
print(ispangram('The quick brown fox jumps over the lazy dog'))
