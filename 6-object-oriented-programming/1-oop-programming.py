
#! Object Oriented Programming

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

# *OOP create your own:
#!  Objects w/
# *METHODS and ATTRIBUTES

# ? OOP allows to reate code thatis repeatable and organized

#! Objects

# In Python, everything is an object.

print(type(1))
print(type([]))
print(type(()))
print(type({}))

# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# Let see how we can use class:

# # Create a new object type called Sample


class Sample:
    pass


# # Instance of Sample
x = Sample()

print(type(x))

# * <class '__main__.Sample'>

# Note how x is now the reference to our new instance of a Sample class.
# In other words, we instantiate the Sample class.

#!OOP KEYWORDS

# todo SYNTAX
#! class NameOfClass():

#! CLASS = kw used to create USER-DEFINED OBJECT types

# From classes we can construct instances.

# An instance is a specific object created from a particular class.

#! INSTANCE def__init__ = is a SPECIFIC OBJECT created from a CLASS

# *special method NOT function

#! METHODS = functions defined IN the BODY of a CLASS.
# ? METHODS used to perform operations with the ATTRIBUTES of our OBJECTS.

#  Methods are a key to dividing responsibilities in programming, especially in large applications.

# You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

#! SELF = keyword represents INSTANCE of OBJ to create ATTRIBUTES and METHODS


# ?self kw used signify that this is method not a function


#!OOP SYNTAX

# * def __init__(self,param1,param2):
# *    self.param1 = self.param1

# todo create methods
# ? def __init__(self,args):
#! ATTRIBUTES
#      self.attribute = self.attribute_name

#!EX DOGS

print('\nDog example\n')


class Dog(object):
    def __init__(self, breed, *args, **kwargs):
        self.breed = breed


sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print(sam.breed)
# 'Lab'

print(frank.breed)

# 'Huskie'

print('\nEX CLASS OBJECT ATTRIBUTE')


class Dogs:

    #! CLASS OBJECT ATTRIBUTE
    # * Doesn't use SELF kw
    # ? same for ANY INSTANCE of a CLASS

    species = 'mammal'
    # species is Class Object Attribute

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def bark(self):
        print('Woof my name is {} and I love Geoff'.format(self.name))

    def begging(self, number):
        print('Woof! I am {} and I love you. I want {} treats'.format(
            self.name, number))
# * use SELF.NAME to referenece Instance of Class Object


colby = Dogs('Lab', 'Colby', 8)
print(colby.bark())

print(colby.name)
print(type(colby), '\n')

# can also pasin new information

print(colby.begging(10))


#!EX Circle class:

print('\nEX CIRCLE')


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

print('\nINHERITACE')

#! Inheritance

# Inheritance is a way to form NEW classes or DERIVED CLASSES using previously defined classes BASE CLASSES.

# The newly formed classes are called DERIVED CLASSES, the classes that we derive from are called BASE CLASSES.

# Benefits of inheritance are code reuse and reduction of complexity of a program.

# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# Let's see an example by incorporating our previous work on the Dog class:


class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


d = Dog()

# Animal created
# Dog created

d.whoAmI()

# Dog

d.eat()

# Eating

d.bark()

# Woof!

# In this example, we have two classes: Animal and Dog. The Animal is the base class, the Dog is the derived class.

# The derived class inherits the functionality of the base class.

#     It is shown by the eat() method.

# The derived class modifies existing behavior of the base class.

#     shown by the whoAmI() method.

# Finally, the derived class extends the functionality of the base class, by defining a new bark() method.


#!POLYMORPHIS

print('\nPOLYMORPHISM\n')
# , polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in.


class Canine:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'


class Feline:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


niko = Canine('Niko')
felix = Feline('Felix')

print(niko.speak())
print(felix.speak())


# Niko says Woof!
# Felix says Meow!

# Here we have a Dog class and a Cat class, and each has a .speak() method. When called, each object's .speak() method returns a result unique to the object.

# There a few different ways to demonstrate polymorphism. First, with a for loop:

for pet in [niko, felix]:
    print(pet.speak())


# Another is with functions:

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

# In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

#!ABSTRACT CLASS and INHERITANCE
# A more common practice is to use abstract classes and inheritance.

# An ABSTRACT CLASS is one that never expects to be instantiated.

#  For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:

print('\nEX ABSTRACT CLASS INHERITANCE')


class Animals:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Doggy(Animals):

    def speak(self):
        return self.name+' says Woof!'


class Kitty(Animals):

    def speak(self):
        return self.name+' says Meow!'


fido = Doggy('Fido')
isis = Kitty('Isis')

print(fido.speak())
print(isis.speak())


#! Real life examples of polymorphism include:

#     opening different file types - different tools are needed to display Word, pdf and Excel files
#     adding different objects - the + operator performs arithmetic and concatenation


#! Special Methods
print('\nEX Special Methods\n')
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

# ??????=============

print('\nADDITIONAL EX')


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


print('\nEX CAR')


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


def checkin(ex):
    return sum(i for i in ex)
    # for i in ex:
    #     i += i
    # return i


def mult(nums):
    return eval('*'.join(map(str, nums)))


print(mult([1, 2, 3]))
# 1
