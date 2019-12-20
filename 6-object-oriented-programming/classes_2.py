
#! Object Oriented Programming

#? PROCEDURE ORIENTED PROGRAMMING , where the main emphasis is on functions

# Python is an object oriented programming language.

# In Python, everything is an object.

#? OBJECT ORIENTED PROGRAMMING stress on objects.

# The concept of OOP in Python focuses on creating reusable code. This concept is also known as

# ? DRY (Don't Repeat Yourself).

# ? CLASS

# A class is a blueprint mapping/alias for the object.

#! OBJECT AKA INSTANCE (of class)= is simply a collection of ATTRIBUTES (((DATA (variables) and METHODS (functions))) that act on those data. 

#? Class is a blueprint for the object.

#* INSTANTIATION = process of creating this object or INSTANCE of a class

# A class creates a NEW LOCAL NAMESPACE where all its ATTRIBUTES are defined. 

# ATTRIBUTES may be DATA or FUCNTIONS.


#! Constructors in Python

# CLASS FUNCTIONS that begins with double underscore (__) are called SPECIAL FUNCTIONS as they have special meaning.

#*__init__() function. 

# This special function gets called whenever a new object of that class is INSTANTIATED.

# This type of function is also called CONSTRUCTORS in Object Oriented Programming (OOP).
# 
#  We normally use it to initialize all the variables.

#!                          OOP KEYWORDS


# ?  CLASS KW to create USER-DEFINED OBJECTS (INSTANCE is a specific OBJECT of a CLASS)

#! CLASS USES CAMEL CASE SYNTAX

#==========================#==========================

# ?! SELF KW
# ? to create ATTRIBUTES and METHODS

#* An OBJECT has 2 characteristics/OPERATIONS:

# ? attributes/ATTRIBUTE REFERENCES
# ? behavior/INSTANTATION(METHODS and DATA REFERENCES)

#==========================#==========================

#!                        CREATE ATTRIBUTES

# ? def __init__(self, args):
# ?    self.attribute = attributes


#! User-Defined Object Types

# ? use type() to check the type of object something is:

print(type(1))
print(type([]))
print(type(()))
print(type({}))

# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# User defined objects are created using the class keyword.

# Above we created the object lst which was an instance of a list object.

# NOTE EX

# ? Create a new object type called Sample

class Sample:
    pass

# Instance of Sample

x = Sample()

print(type(x))

# <class '__main__.Sample'>

# Note how x is now the reference to our new instance of a Sample class.

# In other words, we INSTANTIATE the Sample class.

#! CLASS DEFINITION

#? WHEN A CLASS IS DEFINED... 
# ONLY the description for the object is defined, NO MEMORY or storage is ALLOCATED (), like def function must be executed to have an effect.

# NOTE When a CLASS DEFINITION is entered... 
# a NEW NAMESPACE is created, and used as the LOCAL SCOPE — thus, ALL ASSIGNMENTS to local variables go into this new namespace. Function definitions BIND the NEW function NAME here.

#? ORIGINAL LOCAL SCOPE == scope in effect just BEFORE the CLASS DEFINITION was entered) is reinstated, and the CLASS OBJECT is bound here to the CLASS NAME given in the CLASS DEFINITION HEADER.


#! Class Objects

# As soon as we define a class, a new CLASS OBJECT is CREATED with the SAME NAME. 

#? When a CLASS DEFINITION is left normally (via the end), a CLASS OBJECT is created. This is basically a WRAPPER around the contents of the NAMESPACE created by the class definition. 

# ? CLASS OBJECTS support 2 kinds of OPERATIONS:

# ?            1. ATTRIBUTE REFERENCES
# ?           2. INSTANTIATION


#!                     ATTRIBUTE REFERENCES

# All ATTRIBUTE REFERENCES use the STANDARD SYNTAX syntax use

#*                          OBJ.AttributeNAME.

#* ATTRIBUTES may be DATA or METHOD. 

# ? 2 kinds of valid ATTRIBUTRE NAMES or INSTANCE ATTRIBUTES

#    ?                DATA ATTRIBUTES
#   ?                 METHODS

#!                          CLASS INSTANTIATION

# Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class.

#!INSTANCES / Instance Objects

print('\n\t\t\tINSTNACES OF OBJECTS\n')

# * INSTANCE == is a specific object created from a particular class.

# Now what can we do with instance objects?

#? The ONLY OPERATIONS understood by INSTANCE OBJECTS are ATTRIBUTE REFERENCES

#? CREATING INSTANCE Object in Python

#Class obj used to create new object instances (instantiation) of that class. 
# 
# The procedure to create an object is similar to a function call.

class MyClass:
	"This is a docstring. I have  a brief description about the class. I have special attributes that begin with double underscores (__). EX. __doc__ "
	a = 10

	def func(self):
		print('Hello')
 
#! This will create a new INSTANCE OBJECT or INSTANCE OF A CLASS ob. 
ob = MyClass()

print(MyClass.a)
print(MyClass.__doc__)

print('\n\t\tFUNCTION OBJECT\nclass.method\n',MyClass.func,'\ntype(MyClass.func)\n',type(MyClass.func))

#todo                            MyClass.func is a FUNCTION OBJECT (ATTRIBUTE of CLASS)
# Any FUNCTION OBJECT that is a CLASS ATTRIBUTE defines a method for objects of that class.

print('\n\t\t\tABSTRACT OBJECT = METHOD OBJECT bound to FUNCTION OBJECT\nob.func() === MyClass.func(ob)\n',ob.func, '\n')
#todo                           OB.FUNC is a METHOD OBJECT.
# Method of an object are corresponding functions of that class. 

#!ob.func() === MyClass.func(ob).

#todo review
# You may have noticed the self parameter in function definition inside the class but, we called the method simply as
# 
#  ob.func() 
# This is because, whenever an object calls its method, 

#* the INSTANCE OBJECT itself is passed as the FIRST ARG. 

#? OUTPUT

# 10
# This is a docstring. I have  a brief description about the class. I have special attributes that begin with double underscores (__). EX. __doc__ 

#? <function 0x7feaa932eae8="" at="" myclass.func="">

#?<bound method MyClass.func of <__main__.MyClass object at 0x0000011B147DF550>>'

#==========================#==========================

#!ABCTACT OBJECT. FUNCTION AND METHOD OBJECT EXPLAINED

#!ob.func() === MyClass.func(ob).

# In general, calling a method with a list of n arguments is equivalent to  calling the corresponding function with an ARG LIST that is created by INSERTING the METHOD'S OBJ BEFORE the 1ST ARG argument.

#NOTE For these reasons, 
#? the 1st ARG of the function in class must be the OBJ itself. This is conventionally called SELF. 

# It can be named otherwise but we highly recommend to follow the convention.

# When REFERENCING a NON-DATA ATTRIBUTE of an INSTANCE , the INSTANCE CLASS is SEARCHED. 

#?If the name denotes Class attribute that is a FUNCTION OBJ,

#  a METHOD OBJ is created by PACKING (pointers to) the INSTANCE OBJ and the function object just found together in an ABSTRACT OBJ: this is the METHOD OBJECT

# When the METHOD OBJ is called with an ARG LIST, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.


#? Now you must be familiar with 
# CLASS OBJECT, 
# INSTANCE OBJECT, 
# FUNCTION OBJECT, 
# METHOD OBJECT and their differences.

#==========================#==========================

#!                         CREATE METHODS

# ? def method(self)

# Methods are functions defined inside the body of a class. 

# Methods are used to perform operations with the attributes of our objects.

# You can basically think of methods as FUNCTIONS ACTING on an Object that take the OBJECT ITESELF into account through its self ARG.

#Methods are essential to dividing responsibilities in programming, especially in large application

#==========================#==========================

#! Example 2 : Creating Methods in Python

class Parrot:

#?CLASS OBJ ATTRIBUTE or CLASS VAR
    species = "bird"
    #Shared by all instances, 
    #! USE IMMUTABLE DATA TYPE
    #* __class__.classObjAttribute

#? INSTANCE ATTRIBUTES
    def __init__(self, name, age):
        #NOTE INSTANCE VARIABLE
        self.name = name
        self.age = age
    
#? INSTANCE METHODS
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


#? INSTANCE OBJECT(S) - INSTANTIATE Class

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# blu and woo are INSTANCE OBJECTS or REFERENCES (VALUES) to our new objects.

#todo access the CLASS ATTRIBUTES
print("\nBlu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# Then, we ACCESS  the CLASS ATTRIBUTE using __class __.species. 
 
# CLASS ATTRIBUTES are SAME for ALL INSTANCES of a CLASS. 

#todo access the INSTANCE ATTRIBUTES
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

#Instance attributes are different for every instance of a class.

#? obj.attr

#todo CALL our INSTANCE METHODS
print(blu.dance())
print(blu.sing("'Happy\n"))

#NOTE When we run the program, the output will be:

# Blu is a bird
# Woo is also a bird
# Blu is 10 years old
# Woo is 15 years old
# Blu sings 'Happy'
# Blu is now dancing


# In the above program, we

# 1. create a class with name Parrot. 
# 2. we define attributes (attributes are a characteristic of an object).
# 3. Then, we create instances of the Parrot class. 
# define two methods i.e sing() and dance(). These are called instance method because they are called on an instance object i.e blu.

#==========================#==========================

class Dogs:

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name, age, bestfriend):
        self.breed = breed
        self.name = name
        self.age = age
        self.bestfriend = bestfriend

    def bark(self):
        print('Woof my name is {} and I love Geoff'.format(self.name))
    
    def breakfast(self):
        print('{} it is your best friend {} and it is breakfast time!\nGive me kisses while I eat because I love you'.format(self.bestfriend, self.name))

colby = Dogs('Lab', 'Colby', 8, 'Geoff')
print(colby.bark())
print(colby.name)
print(colby.breakfast())
print('\n')

# ==========================#==========================

# In Python, the concept of OOP follows some basic principles:

# *INHERITANCE == 
# A process of using details from a new class WITHOUT MODIFYING EXISTING CLASS.

# * ENCAPSULATION == 
# Hiding the private details of a class from other objects.

# * POLYMORPHISM == 
# A concept of using common operation in DIFFERENT ways for DIFFERENT data input.

# ==========================#==========================

#!                           Python Inheritance

# ==========================#==========================

#* What is Inheritance?

#? It refers to defining a NEW CLASS called CHILD/DERIVED CLASS taking all functionality from an EXISTING CLASS and adding functionality with LITTLE or NO MODIFICATION to the ORIGINAL class known as PARENT/BASE CLASS. 

# BENEFITS of inheritance
#                      code reuse
#                      simplify a program.

#* The DERIVED classes (descendants) OVERRIDE or extend the functionality of BASE classes (ancestors).


#? Python Inheritance Syntax

#! class BaseClass:
#!   Body of base class
#! class DerivedClass(BaseClass):
#!   Body of derived class

# Derived class inherits features from the base class, adding new features to it. # This results into re-usability of code.

#==========================#==========================


# The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

# class DerivedClassName(modname.BaseClassName):

# Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: 
# if a requested attribute is not found in the class, the search proceeds to look in the base class.
#  This rule is applied recursively if the base class itself is derived from some other class.

# There’s nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. 
# Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

#NOTE EX

# To demonstrate the use of inheritance, let us take an example.

#! Inheritance

# Example 3: Use of Inheritance in Python

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

print('\t\t\tINHERITANCE')
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# When we run this program, the output will be:

# Bird is ready
# Penguin is ready
# Penguin
# Swim faster
# Run faster

# In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). 
# The child class inherits the functions of parent class. We can see this from swim() method. 
# Again, the child class modified the behavior of parent class.
#  We can see this from whoisThis() method. 
# Furthermore, we extend the functions of parent class, by creating a new run() method.

# Use super() function before __init__() method. This is because we want to pull the content of __init__() method from the parent class into the child class.

#! super().__init__() = bird.__init__(self)

#==========================#==========================

# If an attribute is not found in the class, search continues to the base class. This repeats recursively, if the base class is itself derived from other classes.

#* Method Overriding in Python

# In the above example, notice that __init__() method was defined in both classes, PENGUIN as well BIRD. 
# When this happens, the method in the derived class overrides that in the base class. 
# This is to say, __init__() in PENGUIN gets preference over the same in BIRD.

# Generally when overriding a base method, we tend to extend the definition rather than simply replace it. 
# The same is being done by calling the method in base class from the one in derived class (calling BIRD.__init__() from __init__() in PENGUIN).

#? A better option would be to use the built-in function super().
#! super().__init__(3) = Polygon.__init__(self,3)

# ?Two built-in functions isinstance() and issubclass() are used to check inheritances. 
# 
# *Function isinstance() returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.

#* Similarly, issubclass() is used to check for class inheritance.


#!Method Overriding

# Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it.

# An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name.
#  There is a simple way to call the base class method directly: just call
#  BaseClassName.methodname(self, arguments).
#  This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)


#==========================#==========================

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


print('\nINHERITANCE EX 2')
print(Square(4).area())
rectangle = Rectangle(2, 4)

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())
print('issublcass(parentClass, derivedclass)\n',issubclass(Square, Rectangle),'\nisinstance(intanceObject, instanceClass)',isinstance(rectangle, Rectangle))

#* Python has two built-in functions that work with inheritance:

#?     Use isinstance(obj, int) to check an instance’s type: 
# isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

#?     Use issubclass(bool, int) to check class inheritance: issubclass(bool, int) 
# is True since bool is a subclass of int.
# is False since float is not a subclass of int.



#==========================#==========================

                            #!FAITH AND DILLIGENCE



#==========================#==========================

#! Encapsulation

print('\n\t\t\t\tENCAPSULATION')

#* ENCAPSULATION =  Restrict access to methods and vars of a class to PREVENT DATA from DIRECT MODIFICATION.

#!private attribute = an attribute can only be CHANGEDby SETTER FUNCTION reference and CANNOT be CHANGED referenced from inside an object

# ! SYNTAX PRIVATE ATTRIBUTE using underscore as prefix i.e single “ _ “ or double “ __“.

#==========================#==========================

#? Example 4: Data Encapsulation in Python

class Computer:

    def __init__(self):
   #NOTE __maxprice
   #! self.__privateATTRIBUTE
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

#!SETTER FUNCTION
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# When we run this program, the output will be:

# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000

#NOTE In the above program, we defined a class Computer. 
# We use __init__() method to store the maximum selling price of computer. 
# can’t change __maxprice because Python treats the __maxprice as PRIVATE ATTRIBUTES. 
# 
# ? To change the price use  a SETTER FUNCTION  i.e setMaxPrice() which takes price as parameter.

#==========================#==========================

#! Polymorphism

#* Polymorphism is an ability (in OOP) to use COMMON INTERFACE for multiple form (data types).

#? POLYMORPHISM is way in which DIFFERENT object CLASSES can share the SAME METHOD NAME,

print('\n\t\t\tPOLYMORPHISH')

# Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). However we could use same method to color any shape. This concept is called Polymorphism.

#NOTE Example 5: 

# ?Using Polymorphism in Python

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

#!COMMON INTERFACE
def flying_test(bird):
    bird.fly()

# instantiate objects
blu = Parrot()
peggy = Penguin()
print('\n')

#! PASSING OBJ in COMMON INTERRACE
flying_test(blu)
flying_test(peggy)
print('\n')

# When we run above program, the output will be:

# Parrot can fly
# Penguin can't fly

# In the above program, we defined two classes Parrot and Penguin. 

# Each of them have common method fly() method. However, their functions are different.

#  To allow polymorphism, we created common interface i.e flying_test() function that can take any object. Then, we passed the objects blu and peggy in the flying_test() function, it ran effectively.

# Key Points to Remember:

#     The programming gets easy and efficient.
#     The class is sharable, so codes can be reused.
#     The productivity of programmars increases
#     Data is safe and secure with data abstraction.

#==========================#==========================

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


#==========================#==========================

#! ABSTRACT CLASS is one that never expects to be instantiated.

print('\n\t\t\tABSTRACT CLASS')

# A more common practice is to use ABSTRACT CLASSES and inheritance.

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

#IRL APPLICATIONS
#?     opening different file types - different tools are needed to display Word, pdf and Excel files

#?     adding different objects - the + operator performs arithmetic and concatenation

#==========================#==========================
#! Python Multiple Inheritance

# learn about multilevel inheritance and the method resolution order.

#* Multiple Inheritance = DERIVED CLASS created from MULTIPLE BASE CLASSES.

print('\n\t\t\tMULTIPLE INHERITANCE')

# EX SYNTAX for multiple inheritance is similar to single inheritance.


#     class Base1:
#         pass
#     class Base2:
#         pass
#     class MultiDerived(Base1, Base2):
#         pass

# Here, MultiDerived is derived from classes Base1 and Base2.

# Multiple Inheritance in Python

# The class MultiDerived inherits from both Base1 and Base2.

#==========================#==========================

#! Multilevel Inheritance in Python

#* Multilevel inheritance =DERIVED CLASS inherits form a DERIVED CLASS. (be of any depth in Python.)

#features of the base class and the derived class is inherited into the new derived class.

print('\n\t\t\tMULTI-LEVEL INHERITANCE')

#  EX SYNTAX multilevel inheritance, 

#?     class Base:
#         pass
#?     class Derived1(Base):
#         pass
#?     class Derived2(Derived1):
#         pass

# Here, Derived1 is derived from Base, and Derived2 is derived from Derived1.

#==========================#==========================

#! Method Resolution Order in Python

# Every class in Python is derived from the class object. It is the most base type in Python.

# So technically, all other class, either built-in or user-defines, are derived classes and all objects are instances of object class.

print('\n\t\t\tMETHOD RESOLUTION ORDER')

# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))

# In the multiple inheritance scenario, any specified attribute is searched first in the current class. 
# If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.

# So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. 
# 
#* Method Resolution Order (MRO) linearization of MultiDerived class  = Set of rules used to find  SEARCH ORDER

# MRO must prevent local precedence ordering and also provide MONOTONICITY(subclass first priority). It ensures that a class always appears before its parents and in case of multiple parents, the order is same as tuple of base classes.

#! MONOTONIC (meaning that a class can be subclassed without affecting the precedence order of its parents). 

#? MRO of a class can be viewed as the
#  __mro__ attribute 
# or mro() method. 
# The former returns a tuple while latter returns a list.

#     >>> MultiDerived.__mro__
#     (<class '__main__.MultiDerived'>,
#      <class '__main__.Base1'>,
#      <class '__main__.Base2'>,
#      <class 'object'>)
#     >>> MultiDerived.mro()
#     [<class '__main__.MultiDerived'>,
#      <class '__main__.Base1'>,
#      <class '__main__.Base2'>,
#      <class 'object'>]

# Here is a little more complex multiple inheritance example and its visualization along with the MRO.

# Multiple Inheritance Visualization

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print('\nclass.mro()\n',M.mro(),'\ndepth first\n left to right second\nLAST IS PARENT')

# Refer to this, for further discussion on MRO and to know the actual algorithm how it is calculated.

#==========================#==========================

#? MOST PURPOSES, in the SIMPLEST CASE, you can think of the SEARCH(recursively) for ATTRIBUTES inherited from a parent class as 

#* DEPTH-FIRST, 
#* left-to-right, 
#* not searching twice in the same class where there is an overlap in the hierarchy. 

# Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

#==========================#==========================

#! MRO CHANGES DYNAMICALLY to support cooperative calls to super(). 
# This approach is known in some other MULTIPLE-inheritance languages as CALL-NEXT-METHOD 
# More powerful than the super call found in SINGLE-inheritance languages.

#! DYNAMIC ORDERING is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). 

#multiple inheritance provides more than one path to an object
#DYANMIC ALGO keeps base classes from multiple references
#monotocity

#==========================#==========================

#! Special Methods

print('\n\t\t\t\tSPECIAL METHODS')

# Finally let's go over special methods.
#  Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:

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

#==========================#==========================
#!ADCANCED OOP

#! Deleting Attributes and Objects

# Any attribute of an object can be deleted anytime, using the del statement. Try the following on the Python shell to see the output.

#     >>> c1 = ComplexNumber(2,3)
#     >>> del c1.imag
#     >>> c1.getData()
#     Traceback (most recent call last):
#     ...
#     AttributeError: 'ComplexNumber' object has no attribute 'imag'
#     >>> del ComplexNumber.getData
#     >>> c1.getData()
#     Traceback (most recent call last):
#     ...
#     AttributeError: 'ComplexNumber' object has no attribute 'getData'

# We can even delete the object itself, using the del statement.

#     >>> c1 = ComplexNumber(1,3)
#     >>> del c1
#     >>> c1
#     Traceback (most recent call last):
#     ...
#     NameError: name 'c1' is not defined

# Actually, it is more complicated than that. When we do c1 = ComplexNumber(1,3), a new instance object is created in memory and the name c1 binds with it.

# On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace. The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.

# This automatic destruction of unreferenced objects in Python is also called garbage collection.

# ==========================#==========================

#! Python Operator Overloading'

# ==========================#==========================

# You can change the meaning of an operator in Python depending upon the operands used. This practice is known as operating overloading.
# What is operator overloading in Python?

# Python operators work for built-in classes. But same operator behaves differently with different types. For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings.

# This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

# So what happens when we use them with objects of a user-defined class? Let us consider the following class, which tries to simulate a point in 2-D coordinate system.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
# Now, run the code and try to add two points in Python shell.

#     >>> p1 = Point(2,3)
#     >>> p2 = Point(-1,2)
#     >>> p1 + p2
#     Traceback (most recent call last):
#     ...
#     TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

# Whoa! That's a lot of complains. TypeError was raised since Python didn't know how to add two Point objects together.

# However, the good news is that we can teach this to Python through operator overloading. But first, let's get a notion about special functions.

#! Special Functions in Python

# Class functions that begins with double underscore __ are called special functions in Python. This is because, well, they are not ordinary. The __init__() function we defined above, is one of them. It gets called every time we create a new object of that class. There are a ton of special functions in Python.

# Using special functions, we can make our class compatible with built-in functions.

#     >>> p1 = Point(2,3)
#     >>> print(p1)
#     <__main__.Point object at 0x00000000031F8CC0>

# That did not print well. But if we define __str__() method in our class, we can control how it gets printed. So, let's add this to our class.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

# Now let's try the print() function again.

#     >>> p1 = Point(2,3)
#     >>> print(p1)
#     (2,3)

# That's better. Turns out, that this same method is invoked when we use the built-in function str() or format().

#     >>> str(p1)
#     '(2,3)'
#     >>> format(p1)
#     '(2,3)'

# So, when you do str(p1) or format(p1), Python is internally doing p1.__str__(). Hence the name, special functions.

# Ok, now back to operator overloading.

# ? Overloading the + Operator in Python

# To overload the + sign, we will need to implement __add__() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is sensible to return a Point object of the coordinate sum.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
# Now let's try that addition again.

#     >>> p1 = Point(2,3)
#     >>> p2 = Point(-1,2)
#     >>> print(p1 + p2)
#     (1,5)

# What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in turn is Point.__add__(p1,p2). Similarly, we can overload other operators as well. The special function that we need to implement is tabulated below.
# Operator Overloading Special Functions in Python Operator 	Expression 	Internally
# Addition 	p1 + p2 	p1.__add__(p2)
# Subtraction 	p1 - p2 	p1.__sub__(p2)
# Multiplication 	p1 * p2 	p1.__mul__(p2)
# Power 	p1 ** p2 	p1.__pow__(p2)
# Division 	p1 / p2 	p1.__truediv__(p2)
# Floor Division 	p1 // p2 	p1.__floordiv__(p2)
# Remainder (modulo) 	p1 % p2 	p1.__mod__(p2)
# Bitwise Left Shift 	p1 << p2 	p1.__lshift__(p2)
# Bitwise Right Shift 	p1 >> p2 	p1.__rshift__(p2)
# Bitwise AND 	p1 & p2 	p1.__and__(p2)
# Bitwise OR 	p1 | p2 	p1.__or__(p2)
# Bitwise XOR 	p1 ^ p2 	p1.__xor__(p2)
# Bitwise NOT 	~p1 	p1.__invert__()
# Overloading Comparison Operators in Python

# Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.

# Suppose, we wanted to implement the less than symbol < symbol in our Point class.

# Let us compare the magnitude of these points from the origin and return the result for this purpose. It can be implemented as follows.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

# Try these sample runs in Python shell.

#     >>> Point(1,1) < Point(-2,-3)
#     True
#     >>> Point(1,1) < Point(0.5,-0.2)
#     False
#     >>> Point(1,1) < Point(1,1)
#     False

# Similarly, the special functions that we need to implement, to overload other comparison operators are tabulated below.
# Comparision Operator Overloading in Python Operator 	Expression 	Internally
# Less than 	p1 < p2 	p1.__lt__(p2)
# Less than or equal to 	p1 <= p2 	p1.__le__(p2)

# Equal to
# 	p1 == p2 	p1.__eq__(p2)
# Not equal to 	p1 != p2 	p1.__ne__(p2)
# Greater than 	p1 > p2 	p1.__gt__(p2)
# Greater than or equal to 	p1 >= p2 	p1.__ge__(p2)
