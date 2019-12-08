# The type of the object is defined at the runtime and it can’t be changed afterwards. However, it’s state can be changed if it is a mutable object.

# Objects of built-in types like (int, float, bool, str, tuple, unicode, frozenset) are immutable. Objects of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable.


# Python code to test that
# tuples are immutable

tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
# print(tuple1)

# Traceback (most recent call last):
#   File "e0eaddff843a8695575daec34506f126.py", line 3, in
#     tuple1[0]=4
# TypeError: 'tuple' object does not support item assignment

color = ["red", "blue", "green"]
print(color)

color[0] = "pink"
color[-1] = "orange"
print(color)

''' Example 1 '''
x = "Holberton"
y = "Holberton"
id(x)
# 140135852055856
id(y)
# 140135852055856
print(x is y)
# True

# x = 10
# y = x

# We are creating an object of type int. identifiers x and y points to the same object.

# id(x) == id(y)id(y) == id(10)

# if we do a simple operation.

# x = x + 1

# Now

# id(x) != id(y)id(x) != id(10)

# The object in which x was tagged is changed. object 10 was never modified. Immutable objects doesn’t allow modification after creation

# In the case of mutable objects

# m = list([1, 2, 3])n = m

# We are creating an object of type list. identifiers m and m tagged to the same list object, which is a collection of 3 immutable int objects.

# id(m) == id(n)

# Now poping an item from list object does change the object,

# m.pop()

# object id will not be changed

# id(m) == id(n)


# ==========================#==========================

# Python handles mutable and immutable objects differently.
# Immutable are quicker to access than mutable objects.
# Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.
# Immutable objects expensive to change because it involves creating a copy
# Mutable objects are cheap to change

# ==========================#==========================

#! How objects are passed to Functions

# Its important for us to know difference between mutable and immutable types and how they are treated when passed onto functions .Memory efficiency is highly affected when the proper objects are used.

# For example if a mutable object is called by reference in a function, it can change the original variable itself. Hence to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by reference because its value cannot be changed anyways.

# def updateList(list1):
#     list1 += [10]n = [5, 6]
# print(id(n))                  # 140312184155336updateList(n)
# print(n)                      # [5, 6, 10]
# print(id(n))                  # 140312184155336

# As we can see from the above example, we have called the list via call by reference, so the changes are made to the original list itself.

# Lets take a look at another example:

# def updateNumber(n):
#     print(id(n))
#     n += 10b = 5
# print(id(b))                   # 10055680
# updateNumber(b)                # 10055680
# print(b)                       # 5

# In the above example the same object is passed to the function, but the variables value doesn’t change even though the object is identical. This is called pass by value. So what is exactly happening here? When the value is called by the function, only the value of the variable is passed, not the object itself. So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. Hence the change is not reflected.
