# TUPLES
#! IMMUTABLE lists
#! ORDERED
# lements inside Tuples cannot be reassigned

# TUPLE SYNTAX parenthesis (1,2,3)
print(' tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed')
t = (1, 2, 3)
print('\nt = (1,2,3)')
print('len(t)')
print(len(t))
t = ('one', 2, 'one')
print(t)
#! TUPLE METHODS
# *count and index
print("\nt.index('one')")
print(t.index('one'))
print("\nt.count('one') ---> COUNT TOTAL IN INDEX")
print(t.count('one'))
#! IMMUTABLE
print('\nIMMUTABLE')
print("\nt[0]= 'change'")
print('ERROR')
print("t.append('nope')")
print('ERROR')
