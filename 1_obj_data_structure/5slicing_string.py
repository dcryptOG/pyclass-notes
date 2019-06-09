mystring = 'Hello World'
print(mystring[0], mystring[9], mystring[-1], mystring[-2])


print('\nSLICE SYNTAX [START:STOP:STEP]')
abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc)
#! SLICE SYNTAX
# * [start:stop:step]

# todo              REVERSE TRICK
print('REVERSE trick abc[::-1]')
print(abc[::-1])
print('\n')
print('INPUT: abc[2:], abc[:3], abc[5:8]')
print('OUTPUT', abc[2:], '\n', abc[:3], abc[5:8])
print(':stop -- up to BUT NOT including thus abc[:3] does not include d\n')
#! Indexing starts at 0

print('abc[::], abc[::2], abc[::3]')
print(abc[::], abc[::2], abc[::3])
test = 'tinker'
print('whatdafuk'[1:4])
print('\ntinker'[1:4], test[1:4])
# step size can be negative as well, reverses string
