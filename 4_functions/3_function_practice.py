# WARMUP SECTION:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5


def even_odds(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(even_odds(3, 9))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

test_string = 'Hello you'


def str_two(st):
    words = st.split()
    if words[0][0].lower() == words[1][0].lower():
        return True
    else:
        return False


print('What', str_two('fuck Fuck'))


def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


print(animal_crackers('fuck Fuck'))
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#     pass

# animal_crackers('Levelheaded Llama')

# animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


def add(x1, x2):
    if (x1 + x2) == 20 or x1 == 20 or x2 == 20:
        return True
    else:
        return False


def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20


print(add(10, 20))
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# def makes_twenty(n1,n2):
#     pass

# makes_twenty(20,10)

# makes_twenty(2,3)

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

st = 'helloyou'


def caps(st):
    if len(st) > 3:
        return st[:3].capitalize() + st[3:].capitalize()
    else:
        return 'String too short'


print(caps(st))


# ! MASTER YODA: Given a sentence, return a sentence with the words reversed
# todo FINISH DIS ONE NOW
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string.
#  For example, some uses of the .join() method:

# sen = 'I am home'

# words = sen.split()


# new = words.pop()


# words.insert(0, new)

def yoda(sen):
    words = sen.split()
    words.insert(0, words.pop())
    return ' '.join(words)
# ! better returns string


def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(yoda('I am home'))
# >>> "_0_".join(['a','b','c'])
# >>> 'a_0_b_0_c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

# def master_yoda(text):
#     pass

# master_yoda('I am home')

# master_yoda('We are ready')

# ! ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True


def almost(n):
    if abs(n) in range(90, 111) or range(190, 211):
        return True
    else:
        return False


def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# LEVEL 2 PROBLEMS
# FIND 33:

# ! Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# new = list(enumerate(lst))

def adj3(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


def has_33(nums):
    for i in range(0, len(nums)-1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i+2] == [3, 3]:
            return True

    return False


print(adj3([3, 1, 2, 3, 3, 4, 5]), 'nice')

#     x = lst.index()
# i for i in enumerate(lst):
#     if lst.count(3) > 1:
#         for lst
#     return lst.index(3, 0, stop)

# has_33([1, 3, 3])

# has_33([1, 3, 1, 3])

# has_33([3, 1, 3])

# ! PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def extra(str):
    result = ''
    for char in str:
        result += char*3
    return result


print(extra('MMMiiissssssiiippppppiii'))

# paper_doll('Hello')

# paper_doll('Mississippi')

# print(extra('hello')
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# numbers = [2.5, 3, 3, 4, -5]

# numbers.remove(3)
# print(numbers)
# ! BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# print('numbers', numbers)
# start parameter is not provided
# numbersSum = sum(numbers)
# print(numbersSum)

# start = 10
# numbersSum = sum(numbers, 10)
# print(numbersSum)
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

#! more complete uses lists of nums and prepares for multiple 11sw


def blackjack(nums):
    amt = sum(nums)
    if amt > 21 and nums.count(11) > 0:
        while amt > 21 and nums.count(11) > 0:
            nums.remove(11)
            nums.append(1)
            amt = sum(nums)
        return"Total: {}".format(amt)
    if amt > 21 and nums.count(11) == 0:
        return "BUST: {}".format(amt)
    if amt <= 21:
        return "Total: {}".format(amt)

# blackjack(5,6,7)

# blackjack(9,9,9)


# def blackjack(a, b, c):

#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
#         return sum((a, b, c)) - 10
#     else:
#         return 'BUST'

nums = [11, 11, 10]
print(blackjack(nums))

# ! SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


arr = [2, 1, 6, 1, 3, 9, 11]
print(summer69(arr))
# summer_69([1, 3, 5])

# summer_69([4, 5, 6, 7, 8, 9])
# print(sum([4, 5, 6, 7, 8, 9][0:2]))
# summer_69([2, 1, 6, 9, 11])

# *CHALLENGING PROBLEMS
# !SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


# TODO FIND FIRST ZERO,
# arr = [1, 7, 2, 0, 4, 5, 0, 2]
# x = 0
# arr[x:].index(0)
# print(arr.index(0) > 0)
# todo if second zero SET RANGE
# print('hi', arr[4:].index(0))
# todo IF 7 AFTER RANGE PRINT TRUE


def spy007(arr):
    if 2 <= arr.count(0):
        if 0 <= arr[arr.index(0)+1:].index(0) < arr[arr.index(0)+1:].index(7):
            return True
        else:
            return False
    else:
        return False
# ?


def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1


print(spy_game([1, 0, 2, 4, 0, 5, 7]))
#! find indexes of first two zeros

# spy_game([1,2,4,0,0,7,5])

# spy_game([1,0,2,4,0,5,7])

# spy_game([1,7,2,0,4,5,0])

# ! COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

# count_primes(100) --> 25


# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3, x, 2):  # test all odd factors up to x-1
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)

#         for y in range(3, x, 2):  # test all odd factors up to x-1

#! faster version
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2  # all odds
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


lower = 1
upper = 10
# ! Prime is a number that is only divisible by 1 and ITSELF
# * in terms of whole numbers
# uncomment the following lines to take input from the user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
# By convention, 0 and 1 are not prime.

# def count_primes(num):
#     pass

# count_primes(100)


# ! CHECK IF NUM PRIME

def check_prime(num):
    for i in range(2, num):
        if(num % i) == 0:
            break
        else:
            return "{} is prime.".format(num)


print(check_prime(9))


################


#! Function return every other letter capitalize string

def foo(s):
    ret = ""
    i = True  # capitalize
    # ! i = True EQUIV i = 1
    # i = 1
    for char in s:
        if i:
            ret += char.lower()
        else:
            ret += char.upper()
        if char != ' ':
            i = not i
    return ret


def myfunc10(str):
    ret = ""
    i = 0
    for c in str:
        if(i % 2 == 0):
            ret += c.lower()
        else:
            ret += c.upper()
        i += 1
    return ret


x = "seMi Long StRing WiTH COMPLetely RaNDOM CasINg"
print(myfunc10(x))

print(foo('gkvkafdsgjg'))

x = x.split()

# ! print alphabet big letter
print(x)


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****',
                5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [
        4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')
