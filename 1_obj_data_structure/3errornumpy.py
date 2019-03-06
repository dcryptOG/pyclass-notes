# PYTHON ONLY ACCURATE FOR 53 BITS,
x = 0.1 + 0.2
print(x)
print('x = str(round(x, 2))\n ROUND DECIMAL')
x = str(round(x, 2))
print(x)
# answer is 0.30000000000000004
# PYTHON FAILS AFTER 17 DECIMALS
# LINK https://docs.python.org/2/tutorial/floatingpoint.html
# SEE str.round() method
