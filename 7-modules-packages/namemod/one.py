# one.py
#!all code at indentation level 0 are going to be called

# ? built in var called __name__

# * know runnign python directly through name

print('TOP ONE.PY')


def func():
    print('func() in ONE.py')


if __name__ == '__main__':
    print('ONE.py is run directly\n__name__ is main')
else:
    print('one.py has been imported')
