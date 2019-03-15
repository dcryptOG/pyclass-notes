
# Object Oriented Programming

# Object Oriented Programming (OOP) tends to be one of the major obstacles for beginners when they are first starting to learn Python.

# There are many, many tutorials and lessons covering OOP so feel free to Google search other lessons, and I have also put some links to other useful tutorials online at the bottom of this Notebook.

# For this lesson we will construct our knowledge of OOP in Python by building on the following topics:

#     Objects
#     Using the class keyword
#     Creating class attributes
#     Creating methods in a class
#     Learning about Inheritance
#     Learning about Polymorphism
#     Learning about Special Methods for classes

# Lets start the lesson by remembering about the Basic Python Objects. For example:
# In [1]:

# lst = [1,2,3]

# Remember how we could call methods on a list?
# In [2]:

# lst.count(2)

# Out[2]:

# 1

# What we will basically be doing in this lecture is exploring how we could create an Object type like a list. We've already learned about how to create functions. So let's explore Objects in general:
# Objects

# In Python, everything is an object. Remember from previous lectures we can use type() to check the type of object something is:
# In [3]:

# print(type(1))
# print(type([]))
# print(type(()))
# print(type({}))

# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# So we know all these things are objects, so how can we create our own Object types? That is where the class keyword comes in.
# class

# User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object lst which was an instance of a list object.

# Let see how we can use class:
# In [4]:

# # Create a new object type called Sample
# class Sample:
#     pass

# # Instance of Sample
# x = Sample()

# print(type(x))

# <class '__main__.Sample'>

# By convention we give classes a name that starts with a capital letter. Note how x is now the reference to our new instance of a Sample class. In other words, we instantiate the Sample class.

# Inside of the class we currently just have pass. But we can define class attributes and methods.

# An attribute is a characteristic of an object. A method is an operation we can perform with the object.

# For example, we can create a class called Dog. An attribute of a dog may be its breed or its name, while a method of a dog may be defined by a .bark() method which returns a sound.

# Let's get a better understanding of attributes through an example.
# Attributes

# The syntax for creating an attribute is:

# self.attribute = something

# There is a special method called:

# __init__()

# This method is used to initialize the attributes of an object. For example:
# In [5]:

# class Dog:
#     def __init__(self,breed):
#         self.breed = breed

# sam = Dog(breed='Lab')
# frank = Dog(breed='Huskie')

# Lets break down what we have above.The special method

# __init__()

# is called automatically right after the object has been created:

# def __init__(self, breed):

# Each attribute in a class definition begins with a reference to the instance object. It is by convention named self. The breed is the argument. The value is passed during the class instantiation.

#  self.breed = breed

# Now we have created two instances of the Dog class. With two breed types, we can then access these attributes like this:
# In [6]:

# sam.breed

# Out[6]:

# 'Lab'

# In [7]:

# frank.breed

# Out[7]:

# 'Huskie'

# Note how we don't have any parentheses after breed; this is because it is an attribute and doesn't take any arguments.

# In Python there are also class object attributes. These Class Object Attributes are the same for any instance of the class. For example, we could create the attribute species for the Dog class. Dogs, regardless of their breed, name, or other attributes, will always be mammals. We apply this logic in the following manner:
# In [8]:

# class Dog:

#     # Class Object Attribute
#     species = 'mammal'

#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

# In [9]:

# sam = Dog('Lab','Sam')

# In [10]:

# sam.name

# Out[10]:

# 'Sam'

# Note that the Class Object Attribute is defined outside of any methods in the class. Also by convention, we place them first before the init.
# In [11]:

# sam.species

# Out[11]:

# 'mammal'

# Methods

# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.

# You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

# Let's go through an example of creating a Circle class:
# In [12]:

# class Circle:
#     pi = 3.14

#     # Circle gets instantiated with a radius (default is 1)
#     def __init__(self, radius=1):
#         self.radius = radius
#         self.area = radius * radius * Circle.pi

#     # Method for resetting Radius
#     def setRadius(self, new_radius):
#         self.radius = new_radius
#         self.area = new_radius * new_radius * self.pi

#     # Method for getting Circumference
#     def getCircumference(self):
#         return self.radius * self.pi * 2


# c = Circle()

# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())

# Radius is:  1
# Area is:  3.14
# Circumference is:  6.28

# In the __init__ method above, in order to calculate the area attribute, we had to call Circle.pi. This is because the object does not yet have its own .pi attribute, so we call the Class Object Attribute pi instead.
# In the setRadius method, however, we'll be working with an existing Circle object that does have its own pi attribute. Here we can use either Circle.pi or self.pi.

# Now let's change the radius and see how that affects our Circle object:
# In [13]:

# c.setRadius(2)

# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())

# Radius is:  2
# Area is:  12.56
# Circumference is:  12.56

# Great! Notice how we used self. notation to reference attributes of the class within the method calls. Review how the code above works and try creating your own method.
# Inheritance

# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# Let's see an example by incorporating our previous work on the Dog class:
# In [14]:

# class Animal:
#     def __init__(self):
#         print("Animal created")

#     def whoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")

#     def whoAmI(self):
#         print("Dog")

#     def bark(self):
#         print("Woof!")

# In [15]:

# d = Dog()

# Animal created
# Dog created

# In [16]:

# d.whoAmI()

# Dog

# In [17]:

# d.eat()

# Eating

# In [18]:

# d.bark()

# Woof!

# In this example, we have two classes: Animal and Dog. The Animal is the base class, the Dog is the derived class.

# The derived class inherits the functionality of the base class.

#     It is shown by the eat() method.

# The derived class modifies existing behavior of the base class.

#     shown by the whoAmI() method.

# Finally, the derived class extends the functionality of the base class, by defining a new bark() method.
# Polymorphism

# We've learned that while functions can take in different arguments, methods belong to the objects they act on. In Python, polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in. The best way to explain this is by example:
# In [19]:

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name+' says Woof!'

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name+' says Meow!'

# niko = Dog('Niko')
# felix = Cat('Felix')

# print(niko.speak())
# print(felix.speak())

# Niko says Woof!
# Felix says Meow!

# Here we have a Dog class and a Cat class, and each has a .speak() method. When called, each object's .speak() method returns a result unique to the object.

# There a few different ways to demonstrate polymorphism. First, with a for loop:
# In [20]:

# for pet in [niko,felix]:
#     print(pet.speak())

# Niko says Woof!
# Felix says Meow!

# Another is with functions:
# In [21]:

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(niko)
# pet_speak(felix)

# Niko says Woof!
# Felix says Meow!

# In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

# A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:
# In [22]:

# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name

#     def speak(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")


# class Dog(Animal):

#     def speak(self):
#         return self.name+' says Woof!'

# class Cat(Animal):

#     def speak(self):
#         return self.name+' says Meow!'

# fido = Dog('Fido')
# isis = Cat('Isis')

# print(fido.speak())
# print(isis.speak())

# Fido says Woof!
# Isis says Meow!

# Real life examples of polymorphism include:

#     opening different file types - different tools are needed to display Word, pdf and Excel files
#     adding different objects - the + operator performs arithmetic and concatenation

# Special Methods

# Finally let's go over special methods. Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:
# In [23]:

# class Book:
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         print("A book is destroyed")

# In [24]:

# book = Book("Python Rocks!", "Jose Portilla", 159)

# #Special Methods
# print(book)
# print(len(book))
# del book

# A book is created
# Title: Python Rocks!, author: Jose Portilla, pages: 159
# 159
# A book is destroyed

# The __init__(), __str__(), __len__() and __del__() methods

# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.

# Great! After this lecture you should have a basic understanding of how to create your own objects with class in Python. You will be utilizing this heavily in your next milestone project!

# ! For more great resources on this topic, check out:

# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming

# http://www.tutorialspoint.com/python/python_classes_objects.htm

# https://docs.python.org/3/tutorial/classes.html
