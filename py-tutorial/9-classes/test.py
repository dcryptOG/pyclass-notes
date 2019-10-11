# 9. Classes
#! 9. Classes

# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

# Python’s class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3.
#
# Python classes provide all the standard features of
#
# * Object Oriented Programming:

# One of the popular approach to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

# The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

# An OBJECT has 2 characteristics:

#     attributes
#     behavior

# Objects can contain arbitrary amounts and kinds of data.

# Inheritance ==	A process of using details from a new class without modifying existing class.

# Encapsulation ==	Hiding the private details of a class from other objects.

# Polymorphism  ==	A concept of using common operation in different ways for different data input.

# the class inheritance mechanism allows multiple base classes,
# a derived class can override any methods of its base class or classes
# a method can call the method of a base class with the same name.

# ? EX

# Parrot is an object,

#     name, age, color are attributes
#     singing, dancing are behavior

# ==============================================
#
# NOTE  As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

# In C++ terminology, normally class members (including the data members) are public (except see below Private Variables), and all member functions are virtual. As in Modula-3, there are no shorthands for referencing the object’s members from its methods: the method function is declared with an explicit first argument representing the object, which is provided implicitly by the call. As in Smalltalk, classes themselves are objects. This provides semantics for importing and renaming. Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user. Also, like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class instances.

# (Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms. I would use Modula-3 terms, since its object-oriented semantics are closer to those of Python than C++, but I expect that few readers have heard of it.)

#! 9.1. A Word About Names and Objects

# * ALIASING (alias) == describes a situation in which a data with the same memory can be accessed through different symbolic names in the program

# Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as ALIASING in other languages.
#
# This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples).
#
# However, aliasing has a possibly surprising effect on the semantics of Python code involving MUTABLE OBJ such as:
#       lists
#       dictionaries
#       sets
#
# ALIASES behave like POINTERS in some respects.

# NOTE POINTERS (C, C++) == variables that hold the MEMORY ADDRESS of another variable. Pointers allow for effieciency

# NOTE EX

#  passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change — this eliminates the need for two different argument passing mechanisms as in Pascal.

# * Name (also called IDENTIFIER) == is simply a NAME used to access OBJECTS.
#
# Everything in Python is an object.

# NOTE EX

# The assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with
#
# *id() == can get the ADDRESS (in RAM) of some OBJECT.
#
#  Let's check it.

# Note: You may get different value of id

# a = 2
# # Output: id(2)= 10919424
# print('id(2) =', id(2))

# # Output: id(a) = 10919424
# print('id(a) =', id(a))

# # Here, both refer to the same object.

# # ==========================#==========================

# # NOTE EX
# #
# # Let's make things a little more interesting.
# # You may get DIFFERENT VALUE of ID

# # Initially, an object 2 is created and the name a is associated with it
# a = 2
# # Output: id(a) = 10919424
# print('id(a) =', id(a))

# # NEW object 3 is created and now a associates with this object.
# a = a+1
# # Output: id(a) = 10919456
# print('id(a) =', id(a))

# # Note that id(a) and id(3) have same values.
# # Output: id(3) = 10919456
# print('id(3) =', id(3))

# b = 2
# # Output: id(2)= 10919424
# print('id(2) =', id(2))
# NEW name b gets associated with the previous object 2.


# This is efficient as Python doesn't have to create a new duplicate object.
# This DYNAMIC nature of name binding makes Python powerful; a name could refer to any type of object.

#     >>> a = 5
#     >>> a = 'Hello World!'
#     >>> a = [1,2,3]

# All these are valid and a will refer to three different types of object at different instances.

# Functions are objects too, so a name can refer to them as well.

# def printHello():
#     print("Hello")


# a = printHello()

# Output: Hello

# Our same name a can refer to a function and we can call the function through it, pretty neat.


#! 9.2. Python Scopes and Namespaces


# What is a Namespace in Python?

# * A NAMESPACE ==  collection of names as a MAPPING of EVERY NAME defined to corresponding OBJECTS.

#  Most namespaces are currently implemented as Python DICTIONARIES, but that’s normally not noticeable in any way (except for PERFORMANCE).

# NOTE EX of namespaces are:
# ?       1. the set of built-in names
# ?                   a. built-in FUNCTIONS such as abs())
# ?                  b. built-in EXCEPTIONS names
# ?       2. the GLOBAL NAMES names in a module
# ?        3. The LOCAL NAMES in a function invocation.


# When stariting PYTHON INTERPRETER a NAMESPACE containing ALL the BUILT-IN names is created and exists as long we don't exit. Therefore, BUILT-IN FUNCTIONS like id(), print() etc. are ALWAYS AVAILABLE.

# ==========================#==========================

# NOTE The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces;

# DIFFERENT NAMESPACES can co-exist at a given time but are completely ISOLATED. Each module creates its own global namespace. Hence, the SAME NAME that may exist in DIFFERENT MODULES DONT COLLIDE. Users of the modules must prefix it with the module name.

# Modules can have various functions and classes.

#  A local namespace is created when a function is called, which has all the names defined in it.

# ==========================#==========================

# In a sense the set of attributes of an object also form a namespace.

# NOTE EX,
#
# in the expression z.real, real is an attribute of the object z. Strictly speaking, references to names in modules are attribute references: in the expression modname.funcname, modname is a module object and funcname is an attribute of it. In this case there happens to be a straightforward mapping between the module’s attributes and the global names defined in the module: they share the same namespace! 1

# Attributes may be read-only or writable. In the latter case, assignment to attributes is possible.
#
# Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement.
#
# NOTE EX
#
# del modname.the_answer will remove the attribute the_answer from the object named by modname.

# ==========================#==========================
#!SCOPE

# Namespaces are created at different moments and have different lifetimes.
#
# * SCOPE == is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

# SCOPES are DETERMINED STATICALLY, and are USED DYNAMICALLY.
#
# At any time during execution, there are at least 3 NESTED SCOPES (local, global, built-ins) whose namespaces are directly accessible:

#! LEGB

# Local(L): Defined inside function/class

# Enclosed(E): Defined inside enclosing functions(Nested function concept)

# Global(G): Defined at the uppermost level

# Built-in(B): Reserved names in Python builtin modules

# ? SEACH PRIORITY LEGB

#       1. LOCAL the innermost scope SEARCHED FIRST, contains the local names\

#       2. ENCLOSING functions, which are searched starting with the nearest                  enclosing scope, contains NON-LOCAL, but also NON-GLOBAL names

#       3. GLOBAL contains the CURRENT MOD GLOBAL NAMES

#       4. BUILT-IN the outermost scope (searched LAST) is the namespace containing            built-in names

# ==========================#==========================

# * CREATION OF NAMESPACE vs aforementioned using namspace

# ?                            BUILT-IN CREATION

# The BUILTIN NAMESPACE containing the built-in names is CREATED when the Python INTERPRETER STARTS up, and is NEVER DELETED.

# (The BUILT-IN NAMES actually also live in a MODULE; this is called builtins.)

# ?                            GLOBAL NAMPEACE CREATION

# The GLOBAL NAMESPACE for a MODULE is created when the MODULE DEFINITION is READ in; normally, module namespaces also last until the INTERPRETER QUITS.
#
# The statements executed by the TOP-LEVEL INVOCATION of the interpreter, either READ from a SCRIPT FILE or INTERACTIVELY, are considered part of a module called __main__, so they have their own global namespace.


# ?                           LOCAL NAMESPACE CREATION

# The LOCAL NAMESPACE for a function is CREATED when the FUNCTION is CALLED, and DELETED when the function RETURNS or RASIES an EXCEPTION that is NOT handled WITHIN the function.
#
# RECURSIVE INVOCATIONS each have their own local namespace.

# ==========================#==========================

# ?                                                     ASSIGNMENTS LEGB

# If a name is declared global, then all references and assignments go directly to the middle scope containing the module’s global names.
#
# To REBIND variables found outside of the innermost scope, the NONLOCAL statement can be used; IF NOT DECLARED nonlocal, those variables are READ-ONLY (an ATTEMPT to write to such a variable will simply CREATE a NEW LOCAL VARIABLE in the innermost scope, leaving the identically named outer variable unchanged).

# LOCAL SCOPE is a relative term
# Inside functions references the local names of the (textually) current function.
# Outside functions, the local scope references the same namespace as the global scope: the module’s namespace.
#
# Class definitions place yet another namespace in the local scope.

# It is important to realize that scopes are determined TEXTUALLY: the GLOBAL SCOPE of a FUNCTION DEFINED in a MODULE is that MODULE'S NAMESPACE, no matter from where or by what alias the function is called.

# IF NO GLOBAL STATEMENT is in effect – ASSIGNMENTS to names ALWAYS go into the INNERMOST SCOPE.
#
# Assignments do not copy data — they just bind names to objects.
#
# Deletions: the statement del x REMOVES the BINDING of x from the namespace referenced by the local scope.
#
# ALL operations that introduce NEW NAMES use the local scope: in particular, import statements and function definitions BIND the module or function name in the LOCAL-SCOPE.

# The GLOBAL STATEMENT can be used to indicate that particular variables live in the global scope and should be rebound there
#
# NONLOCAL STATEMENT indicates that particular variables live in an ENCLOSING SCOPE and should be rebound there.

# ==========================#==========================

# ?                                                       SEACHING VARS

# *COMPILE TIME == Is the instance where the code you entered is converted to EXECUTABLE

# *RUN TIME ==  is the instance where the EXECUTABLE is running

#  SEARCH for names is done DYNAMICALLY, at RUN TIME —

#  The language definition is EVOLVING towards STATIC NAME resolution, at “COMPILE” TIME! (In fact, LOCAL VARIABLES variables are already determined statically.)


#! 9.2.1. Scopes and Namespaces Example

# ?EX
#  demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)

# The output of the example code is:

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# NOTE how the local assignment (which is default) didn’t change scope_test’s binding of spam. The nonlocal assignment changed scope_test’s binding of spam, and the global assignment changed the module-level binding.

# You can also see that there was no previous binding for spam before the global assignment.

#! 9.3. A First Look at Classes

# Classes introduce a little bit of new syntax, three new object types, and some new semantics.

#! 9.3.1. Class Definition Syntax

# The simplest form of class definition looks like this:


# class FirstClassName:
#     pass
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an if statement, or inside a function.)

# In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed.
#  The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.

# When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

# When a class definition is left normally (via the end), a class object is created. This is basically a wrapper around the contents of the namespace created by the class definition; we’ll learn more about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (ClassName in the example).

#! 9.3.2. Class Objects

# Class objects support 2 kinds of OPERATIONS:
# ?                  1. attribute references
# ?                  2. instantiation.


# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# * Attribute references
# Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created. So, if the class definition looked like this:

# then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment. __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

# * Class instantiation

# Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):


# x = MyClass()

# creates a new instance of the class and assigns this object to the local variable x.

# The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__(), like this:


# def __init__(self):
#     self.data = []

# When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance. So in this example, a new, initialized instance can be obtained by:


# x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,
# >>>

# >>> class Complex:
# ...     def __init__(self, realpart, imagpart):
# ...         self.r = realpart
# ...         self.i = imagpart
# ...
# >>> x = Complex(3.0, -4.5)
# >>> x.r, x.i
# (3.0, -4.5)

#! 9.3.3. Instance Objects

# Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names, data attributes and methods.

# data attributes
# data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. For example, if x is the instance of MyClass created above, the following piece of code will print the value 16, without leaving a trace:

# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# attribute reference
# The other kind of instance attribute reference is a method.
# A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.)

# Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.

#! 9.3.4. Method Objects

# Usually, a method is called right after it is bound:

# x.f()

# In the MyClass example, this will return the string 'hello world'. However, it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

# xf = x.f
# while True:
#     print(xf())

# will continue to print hello world until the end of time.

# What exactly happens when a method is called? You may have noticed that x.f() was called without an argument above, even though the function definition for f() specified an argument. What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any — even if the argument isn’t actually used…

# Actually, you may have guessed the answer: the special thing about methods is that the instance object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.

# If you still don’t understand how methods work, a look at the implementation can perhaps clarify matters. When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

#! 9.3.5. Class and Instance Variables

# Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

# class Dog:

#     kind = 'canine'         # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.kind                  # shared by all dogs
# 'canine'
# >>> e.kind                  # shared by all dogs
# 'canine'
# >>> d.name                  # unique to d
# 'Fido'
# >>> e.name                  # unique to e
# 'Buddy'

# As discussed in A Word About Names and Objects, shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries. For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

# class Dog:

#     tricks = []             # mistaken use of a class variable

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.add_trick('roll over')
# >>> e.add_trick('play dead')
# >>> d.tricks                # unexpectedly shared by all dogs
# ['roll over', 'play dead']

# Correct design of the class should use an instance variable instead:

# class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.add_trick('roll over')
# >>> e.add_trick('play dead')
# >>> d.tricks
# ['roll over']
# >>> e.tricks
# ['play dead']

#! 9.4. Random Remarks

# Data attributes override method attributes with the same name; to avoid accidental name conflicts, which may cause hard-to-find bugs in large programs, it is wise to use some kind of convention that minimizes the chance of conflicts. Possible conventions include capitalizing method names, prefixing data attribute names with a small unique string (perhaps just an underscore), or using verbs for methods and nouns for data attributes.

# Data attributes may be referenced by methods as well as by ordinary users (“clients”) of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding — it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extensions to Python written in C.)

# Clients should use data attributes with care — clients may mess up invariants maintained by the methods by stamping on their data attributes. Note that clients may add data attributes of their own to an instance object without affecting the validity of the methods, as long as name conflicts are avoided — again, a naming convention can save a lot of headaches here.

# There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this actually increases the readability of methods: there is no chance of confusing local variables and instance variables when glancing through a method.

# Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

# Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

# # Function defined outside the class
# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'

#     h = g

# Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C — h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

# Methods may call other methods by using method attributes of the self argument:

# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we’ll find some good reasons why a method would want to reference its own class.

# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.

#! 9.5. Inheritance

# Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

# class DerivedClassName(modname.BaseClassName):

# Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

# There’s nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

# Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively virtual.)

# An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

# Python has two built-in functions that work with inheritance:

#     Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

#     Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

#! 9.5.1. Multiple Inheritance

# Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

# In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

# Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For example, all classes inherit from object, so any case of multiple inheritance provides more than one path to reach object. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see https://www.python.org/download/releases/2.3/mro/.

#! 9.6. Private Variables

# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

# Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

# Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# The above example would work even if MappingSubclass were to introduce a __update identifier since it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the MappingSubclass class respectively.

# Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

# Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing __dict__ directly.
#! 9.7. Odds and Ends

# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. An empty class definition will do nicely:

# class Employee:
#     pass

# john = Employee()  # Create an empty employee record

# # Fill the fields of the record
# john.name = 'John Doe'
# john.dept = 'computer lab'
# john.salary = 1000

# A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods read() and readline() that get the data from a string buffer instead, and pass it as an argument.

# Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is the function object corresponding to the method.
#! 9.8. Iterators

# By now you have probably noticed that most container objects can be looped over using a for statement:

# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("myfile.txt"):
#     print(line, end='')

# This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the next() built-in function; this example shows how it all works:
# >>>

# >>> s = 'abc'
# >>> it = iter(s)
# >>> it
# <iterator object at 0x00A1DB50>
# >>> next(it)
# 'a'
# >>> next(it)
# 'b'
# >>> next(it)
# 'c'
# >>> next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(it)
# StopIteration

# Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an __iter__() method which returns an object with a __next__() method. If the class defines __next__(), then __iter__() can just return self:

# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# >>>

# >>> rev = Reverse('spam')
# >>> iter(rev)
# <__main__.Reverse object at 0x00A1DB50>
# >>> for char in rev:
# ...     print(char)
# ...
# m
# a
# p
# s

#! 9.9. Generators

# Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]

# >>>

# >>> for char in reverse('golf'):
# ...     print(char)
# ...
# f
# l
# o
# g

# Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the __iter__() and __next__() methods are created automatically.

# Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.

# In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. In combination, these features make it easy to create iterators with no more effort than writing a regular function.
#! 9.10. Generator Expressions

# Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

# Examples:
# >>>

# >>> sum(i*i for i in range(10))                 # sum of squares
# 285

# >>> xvec = [10, 20, 30]
# >>> yvec = [7, 5, 3]
# >>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
# 260

# >>> from math import pi, sin
# >>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

# >>> unique_words = set(word  for line in page  for word in line.split())

# >>> valedictorian = max((student.gpa, student.name) for student in graduates)

# >>> data = 'golf'
# >>> list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']

# Footnotes

# 1

#     Except for one thing. Module objects have a secret read-only attribute called __dict__ which returns the dictionary used to implement the module’s namespace; the name __dict__ is an attribute but not a global name. Obviously, using this violates the abstraction of namespace implementation, and should be restricted to things like post-mortem debuggers.
