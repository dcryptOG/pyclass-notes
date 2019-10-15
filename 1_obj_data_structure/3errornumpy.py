# PYTHON ONLY ACCURATE FOR 53 BITS,
x = 0.1 + 0.2
print(x)
# answer is 0.30000000000000004
#! PYTHON FAILS AFTER 17 DECIMALS

print('\nx = str(round(x, 2))\n ROUND DECIMAL')
x = str(round(x, 2))
print(x)
print(type(x))

print('\n')
print('"%0.2f" % num')
a = 0.1 + 0.2
print("%.2f" % a)

print("\nprint('{:0.2f}'.format(a))")
print('{:0.2f}'.format(a))

# : introduces the format spec
# * 0 enables sign-aware zero-padding for numeric types TOO MANY HAS WHITE SPACE
# .2 sets the precision to 2
# f displays the number as a fixed-point number
