# two.py
import one

print('TOP TWO.PY')

one.func()
#! SAME AS SAYING RUN THE SCRIPT
if __name__ == '__main__':
    print('two.py is run directly\n__name__ is main')
    # ? FUNCTIONS()
else:
    print('two.py has been imported')
