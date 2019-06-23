
#! Object Oriented Programming

# *OOP create your own:
#!  Objects w/
# *METHODS and ATTRIBUTES

# ? OOP allows to reate code thatis repeatable and organized

#!OOP KEYWORDS

#! CLASS - to create own object types

#! SELF - keyword to creae attributes and methods

# todo SYNTAX
#! class NameOfClass():
# *special method NOT function
# ?self kw used signify that this is method not a function
#! def __init__(self,param1,param2):
#!    self.param1 = self.param1
# *self.attribute = self.attribute

# todo create methods
# def method(self)


# todo CLASS USES CAMEL CASE SYNTAX


class Car(object):
    """blueprint for car"""
# ? __INIT__ == INSTANCE

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print('started')

    def stop(self):
        print('stopped')

    def accellerate(self):
        print('accelerating')

    def change_gear(self):
        print('gear changed')


maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)


# For this lesson we will construct our knowledge of OOP in Python by building on the following topics:

#     Objects
#     Using the class keyword
#     Creating class attributes
#     Creating methods in a class
#     Learning about Inheritance
#     Learning about Polymorphism
#     Learning about Special Methods for classes

# Lets start the lesson by remembering about the Basic Python Objects. For example:

lst = [1, 2, 3]

# Remember how we could call methods on a list?

lst.count(2)


def checkin(ex):
    return sum(i for i in ex)
    # for i in ex:
    #     i += i
    # return i


def mult(nums):
    return eval('*'.join(map(str, nums)))


print(mult([1, 2, 3]))
# 1


#! Objects

# In Python, everything is an object.

# ? use type() to check the type of object something is:

print(type(1))
print(type([]))
print(type(()))
print(type({}))

# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object.

# From classes we can construct instances.

# An instance is a specific object created from a particular class.

# For example, above we created the object lst which was an instance of a list object.

# Let see how we can use class:

# # Create a new object type called Sample


class Sample:
    pass


# # Instance of Sample
x = Sample()

print(type(x))

# <class '__main__.Sample'>

# Note how x is now the reference to our new instance of a Sample class.
# In other words, we instantiate the Sample class.

# For example, we can create a class called Dog.


class Dog(object):
    def __init__(self, breed, *args, **kwargs):
        self.breed = breed


sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print(sam.breed)
# 'Lab'

print(frank.breed)

# 'Huskie'


class Dogs:

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def bark(self):
        print('Woof my name is {} and I love Geoff'.format(self.name))


colby = Dogs('Lab', 'Colby', 8)
print(colby.bark())

print(colby.name)


# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects.
#  Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.

# You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

# Let's go through an example of creating a Circle class:

class Circle:
    pi = 3.14

# * Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

#     #! Method for resetting Radius == new_radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
        # self.area = new_radius * new_radius * Circle.pi

# Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

# Radius is:  1
# Area is:  3.14
# Circumference is:  6.28

# In the __init__ method above, in order to calculate the area attribute, we had to call Circle.pi.
# This is because the object does not yet have its own .pi attribute, so we call the Class Object Attribute pi instead.
# In the setRadius method, however, we'll be working with an existing Circle object that does have its own pi attribute. Here we can use either Circle.pi or self.pi.

# Now let's change the radius and see how that affects our Circle object:

c.setRadius(2)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

# Radius is:  2
# Area is:  12.56
# Circumference is:  12.56

# Great! Notice how we used self. notation to reference attributes of the class within the method calls. Review how the code above works and try creating your own method.
# Inheritance

# Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called DERIVED CLASSES, the classes that we derive from are called base classes.

# Benefits of inheritance are code reuse and reduction of complexity of a program.

# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# Let's see an example by incorporating our previous work on the Dog class:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

#! By using inheritance, you can reduce the amount of code you write:

# * So what can super() do for you in single inheritance?


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# ? PY3 SUPER() DEFAULT PARAM: super() == super(Square,self)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


print(Square(4).area())
rectangle = Rectangle(2, 4)

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())


# A more common practice is to use abstract classes and inheritance.

# An ABSTRACT CLASS is one that never expects to be instantiated.

#  For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:


class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
# Constructor of the class
#         self.name = name

# # Abstract method, defined by convention only
# raise NotImplementedError("Subclass must implement abstract method")
    def speak(self):
        print('Hello')

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Canine(Animal):
    def __init__(self, name):
        self.name = name
        # print("Cainine created")

    def whoAmI(self):
        print("Canine")

    def bark(self):
        print("Woof!")
#!overrides speak of Animal

    def speak(self):
        return self.name+' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


c = Canine('')

# Animal created
# Dog created

c.whoAmI()


c.eat()

# Eating

c.bark()

# Woof!

niko = Canine('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# Niko says Woof!
# Felix says Meow!

# Here we have a Dog class and a Cat class, and each has a .speak() method. When called, each object's .speak() method returns a result unique to the object.

# There a few different ways to demonstrate polymorphism. First, with a for loop:

for pet in [niko, felix]:
    print(pet.speak())

# Niko says Woof!
# Felix says Meow!

# Another is with functions:


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

# Niko says Woof!
# Felix says Meow!


#     opening different file types - different tools are needed to display Word, pdf and Excel files
#     adding different objects - the + operator performs arithmetic and concatenation

#! Special Methods

# Finally let's go over special methods. Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:

class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)

# #Special Methods
print(book)
# * can use special mehtod len
print(len(book))
del book

# A book is created
# Title: Python Rocks!, author: Jose Portilla, pages: 159
# 159
# A book is destroyed

# The __init__(), __str__(), __len__() and __del__() methods

# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.

# ! For more great resources on this topic, check out:

#

# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming

# http://www.tutorialspoint.com/python/python_classes_objects.htm

# https://docs.python.org/3/tutorial/classes.html
