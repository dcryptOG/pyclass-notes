# Object Oriented Programming
# Homework Assignment
# Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


class Line(object):

    def __init__(self, c1, c2, *args, **kwargs):
        self.c1 = [c1, c1]
        self.c2 = [c2, c2]

    def distance(self):
        return (((c2[1]-c1[1])**2)+((c2[0]-c1[0])**2))**0.5

    def slope(self):
        return (c2[1]-c1[1])/(c2[0]-c1[0])

    # EXAMPLE OUTPUT


c1 = (3, 2)

c2 = (8, 10)

li = Line(c1, c2)
print(li.distance())


# 9.433981132056603


print(li.slope())


# 1.6

# Problem 2

# Fill in the class

class Cylinder:
    def __init__(self, height, radius):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14*self.height*self.radius*self.radius

    def surface_area(self):
        return (2*3.14*self.radius*self.height) + 2*3.14*(self.radius**2)

        # EXAMPLE OUTPUT
c = Cylinder(2, 3)


print(c.volume())


# 56.52


print(c.surface_area())


# 94.2


# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account Onwer: %s\nAccount Balance: %s' % (self.owner, self.balance)

    def deposit(self, amt):
        self.balance += amt
        return f'Deposit Successful\nAccount Balance: {self.balance}'

    def withdraw(self, amt):
        if self.balance > amt:
            self.balance -= amt
        return f'Withdraw Successful!\nAccount Balance: {self.balance}'

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

#     def deposit(self,dep_amt):
#         self.balance += dep_amt
#         print('Deposit Accepted')

#     def withdraw(self,wd_amt):
#         if self.balance >= wd_amt:
#             self.balance -= wd_amt
#             print('Withdrawal Accepted')
#         else:
#             print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose', 100)


# 2. Print the object
print(acct1)

# Account owner:   Jose
# Account balance: $100


# 3. Show the account owner attribute
# acct1.owner


'Jose'


# 4. Show the account balance attribute
# acct1.balance


# 100


# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))

print(acct1.balance)
# Deposit Accepted


print(acct1.withdraw(75))

# Withdrawal Accepted


# 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500)
