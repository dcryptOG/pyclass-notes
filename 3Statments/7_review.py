
# Statements Assessment Test

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
print(st.split())
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# #Code here

# Use range() to print all the even numbers from 0 to 10.

# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         print(x)
#     else:
#         pass

print(list(range(0, 11, 2)))
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list1 = [x for x in range(0, 51, 3)][1:]
# [x for x in range(1,51) if x%3 == 0]
print(list1)

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(f'{word} - has an even length')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


# x = 0
# while x < 100:
#     x += 1
for x in range(1, 101):
    if x % 5 == 0 and x % 3 == 0:
        print('Fizz Buzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

list1 = [word[0] for word in st.split()]
print(list1)
