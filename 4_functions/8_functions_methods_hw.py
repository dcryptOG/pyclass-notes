
# Functions and Methods Homework

# Complete the following questions:

#! Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as $$\frac{4}{3} πr^3$$


import string


def vol(rad):
    return (4/3)*(3.14)*(rad**3)


print(vol(2))

#! Write a function that checks whether a number is in a given range (inclusive of high and low)
# In [3]:


def ran_check(num, low, high):
    if low < num < high:
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is in not the range between {low} and {high}"

# In [4]:


# # Check
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
    if low < num < high:
        return True
    else:
        return False


print(ran_bool(3, 1, 10))

# True

# !Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# ? HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!
# In [7]:


# def up_low(s):
#     up = 0
#     low = 0
#     for c in s:
#         if c.isupper() is True:
#             up += 1
#         else:
#             low += 1
#     return "Totall upper {} total lower {}".format(up, low)


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))

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
# In [10]:

# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# Out[10]:

# [1, 2, 3, 4, 5]

# ! Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

# In [11]:


def multiply(nums):
    total = 1
    for x in nums:
        total *= x
    return total


nums = [1, 2, 3, 4]
print(multiply([1, 2, 3, 4]))


# ! Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# In [13]:


# ! def palindrome(s):
#     if s[::-1] == s:
#         return True
#     else:
#         return False
# !OR
# def palindrome(s):
#         return s == s[::-1]

def palindrome(s):

    # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('helleh'))

# Out[14]:

# True

# Hard:

# ! Write a Python function to check whether a string is pangram or not.

# ? Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# ? Hint: Look at the string module

# * try without making list and sort


# def ispangram(str1, alphabet=string.ascii_lowercase):
#     lst = set(str1.lower())
#     str = ''.join(lst).lower()
#     abc = set(alphabet)
#     if lst <= abc:
#         return True
#     else:
#         return f'False {lst} vs/n ------ {abc}'


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram('abcdefghijklmnopqrstuvwxyz'))
print(ispangram('The quick brown fox jumps over the lazy dog'))
# Out[16]:

# True

# In [17]:

# string.ascii_lowercase

# Out[17]:

# 'abcdefghijklmnopqrstuvwxyz'
