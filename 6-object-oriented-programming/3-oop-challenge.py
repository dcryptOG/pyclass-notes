class Animal:
    def __init__(self, **kwargs):
        self.species = kwargs.get("species")
        self.age = kwargs.get("age")
        self.sound = kwargs.get("sound")

# >>> wolf.color
# AttributeError...

# No, it's not! But there weren't any errors when I created the instance. Why isn't the attribute available?

# Well, because I didn't create it. Remember, Python is very explicit. If I don't do something explicitly, Python doesn't do it at all. Since I didn't assign a color attribute to self, my instance doesn't have a color attribute.

# This is where setattr comes in. setattr lets me set attributes that I don't know about beforehand. I can, of course, go back and explicitly define a color attribute but what if the next user comes along and she wants a height or weight attribute? A year from now, Animal.__init__ might be hundreds of lines long with attribute declarations! And some of those attributes will only apply to a few animals!

# But...if I'm clever and use setattr, I can just happily accept any and all attributes that someone gives for a particular Animal instance without having to continually update __init__.


class Animals:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

# So, since I have a handy-dandy kwargs dict due to using **kwargs in the method parameters, I can loop through it's items method and pull out the two values from each iteration into attribute and value variables.

# The setattr function takes three arguments: the object to work on, the attribute name to define, and the value to give that attribute. Now, no matter what attribute values I give to my object (assuming they're valid attribute names), my class will happily apply them.


# a = Animals
# a.__init__(self.name=name)


def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
      Country="Wakanda", Age=25, Phone=9876543210)
