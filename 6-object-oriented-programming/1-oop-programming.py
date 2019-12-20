
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

# From classes we can construct INSTANCES.

#! INSTANCE (def__init__) = is a SPECIFIC OBJECT created from a particular CLASS

# *special method NOT function

#! METHODS = functions defined IN the BODY of a CLASS used to perform operations with ATTRIBUTES of our OBJECTS (self kw).

#  Methods are a key to dividing responsibilities in programming, especially in large applications.

# You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

#! SELF = keyword represents INSTANCE of OBJ to create ATTRIBUTES and METHODS

# ?self kw used signify that this is method not a function


#!OOP SYNTAX

# * def __init__(self,param1,param2):
# *    self.param1 = self.param1

# todo CREATE METHODS
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

# ==========================#==========================

print('\nEX CLASS OBJECT ATTRIBUTE')


class Dogs(object):

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


class Circle():
    # * pi is Class Obj Attribute
    #! CLASS OBJECT ATTRIBUTE
    pi = 3.14

# * Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi
# Because pi is Class Object Attribute
# ? self.area = radius * radius * Circle.pi
#! CLASS OBJ ATTRIBUTE alt Syntax
#! self.attribute = Class.Class_Obj_Attribute
# radius is Attribute declared as Parameter VS. Area defined as Attribute
#     #! Method for resetting Radius == new_radius

    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
        # self.area = new_radius * new_radius * Circle.pi

# Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()
c_two = Circle(30)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('\nChange default value to 30\nRadius of C_two: ', c_two.radius)
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

#! INHERITANCE============

# INHERITACE is a way to form new classes DERIVED CLASSES  using previously defined classes BASE CLASSES.

#! DERIVED CLASS = new class formed from previously defined class BASE CLASS (ancestor)

# Benefits of inheritance
# 1. reuse code
# 2. reduce of complexity of a program.

# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

#!EX 1 BASE CLASS

print('\n INHERITANCE EX')

# In this example, we have two classes:
# 1. Animalz is the base class,
# #2. Dogz is the derived class.

# The derived class inherits the functionality of the base class.


class Animalz():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dogz(Animalz):
    def __init__(self):
        Animalz.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


d = Dogz()
# *output
# Animal created
# Dog created

#     shown by the whoAmI() method.

d.whoAmI()
# *output
# Dog

# ? Derived class MODIFIES existing METHODS/BEHAVIOR of the Base class.

# It is shown by the eat() method.
d.eat()
# *output
# Eating
# ? Derived class INHERITS the FUNCTIONALITY of the Base class.

d.bark()
# *output
# Woof!

# ? Derived class EXTENDS the FUNCTIONALITY of the Base class, by defining a NEW METHOD bark()

#!POLYMORPHISM================

print('\nPOLYMORPHISM\n')
#! POLYMORPHISM = Way in which DIFFERENT object CLASSES can share the SAME METHOD NAME,
# #and those methods belong to the object they act on
# Here we have a Dog class and a Cat class, and each has a .speak() method.


class Canine():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'


class Feline():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


niko = Canine('Niko')
print(niko.speak())

# *OUTPUT Niko says Woof!

felix = Feline('Felix')
print(felix.speak())

# *OUTPUT Felix says Meow!


# When called, each object's .speak() method returns a result unique to the object.

# ! EX2 Polymorphism
# polymorphism with a for loop:

print('\nEX polymorphism w/ for loop')

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# *Output Canine Feline class from ex 1

#!EX 3 Polymorphis with functions:

print('\nEX polymorphism w/ functions')


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

# * In both cases:
# 1.  Able to pass in DIFFERENT OBJECT types,
# 2.  AND Obtained OBJECT-SPECIFIC RESULTS from the SAME mechanism.

#!ABSTRACT CLASS and INHERITANCE
print('\nEX ABSTRACT CLASS INHERITANCE')

# A more common practice is to use ABSTRACT CLASSES and inheritance.

#! ABSTRACT CLASS is one that never expects to be instantiated ONLY act as BASE CLASS.

#  For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:


class Animals():
    # * Constructor of the class
    def __init__(self, name):
        self.name = name

  # Abstract method, defined by convention only
# ?raise error

    def speak(self):
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

# *CODE RAISES ERROR
# my_animal = Animals('Fred')
# print(my_animal.speak())

#! Real life examples of polymorphism include:

# ? 1. opening DIFFERENT FILE TYPES - different tools are needed to display Word, pdf and Excel files
# *2. ADDING DIFFERENT OBJECTS - the + operator performs ARITHMETIC and CONCATENATION


#! Special Methods
print('\nEX Special Methods----------\n')
# Finally let's go over special methods.
#! Classes in Python can implement BUILT-FUNCTIONS with SPECIAL METHOD NAMES.
# These methods are NOT called directly but by Python specific language syntax.

# ?  For example let's create a Book class:


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
# *output: A book is created

print(book)
# *output: Title: Python Rocks!, author: Jose Portilla, pages: 159

print(len(book))
# *output: 159

del book
# *output: A book is destroyed

# ? These SPECIAL METHODS are defined by their use of UNDERSCORES.

#! The __init__(), __str__(), __len__() and __del__() methods

# They allow us to use Python specific functions on objects created through our class.

# ! For more great resources on this topic, check out:


# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming

# http://www.tutorialspoint.com/python/python_classes_objects.htm

# https://docs.python.org/3/tutorial/classes.html

# ??????=============

print('\nSUPER()INHERITANE EX')


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
print(rectangle.area())

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
