
# Methods
# ?
# *
# TODO
# !asdf


# ! Methods are essentially FUNCTIONS built into OBJECTS.
# ! METHOD = FUNTION which is defined inside a CLASS BODY.
# ? If called as an attribute of an INSTANCE of that class, the INSTANCE OBJECT read as METHODS its FIRST ARGUMENT (which is usually called SELF).

# You'll later see that we can think of methods as having an argument 'self' referring to the object itself.

# Later create our own objects and methods using Object Oriented Programming (OOP) and classes.

# ?Methods are in the form:

# * object.method(arg1,arg2,etc...)

# # Create a simple list
lst = [1, 2, 3, 4, 5]
lst.reverse()
# *The methods for a list are:

#     ? append() equiv a[len(a):] = [x]
#     count
#     ? extend() eqiv a[len(a):] = iterable
#     ? insert(position, 'obj') append equiv a.insert(len(a), x)
#     pop
#     remove
#     reverse
#     sort

# Let's try out a few of them:

# append() allows us to add elements to the end of a list:


lst = [1, 2, 3, 4, 5, 6]
lst.append(8)

lst.insert(6, 7)

print(lst)

lst.append(9)


print(len(lst))

# Great! Now how about count()? The count() method will count the number of occurrences of an element in a list.

# # Check how many times 2 shows up in the list
x = lst.count(2)

# In general Python you can use the help() function:

help(lst.count)

rev = lst.reverse()

# Help on built-in function count:

# count(...) method of builtins.list instance
#     L.count(value) -> integer -- return number of occurrences of value
nums = [5, 2, 3, 4, 5]
print(nums[0]*nums[4])


def adjacentElementsProduct(inputArray):
    prod = []
    for i in range(1, len(inputArray)-1):
        prod.append(inputArray[i]*inputArray[i+1])
    return max(prod)


# def adjacentElementsProduct(inputArray):
#     prod = []
#     i = 0
#     while i < len(inputArray):
#         for i in inputArray:
#             prod.append(inputArray[i]*inputArray[i+1])
#             i += 1
#     return max(prod)


print(adjacentElementsProduct([1, 2, 456, 2]))
