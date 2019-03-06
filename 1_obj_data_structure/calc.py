print('Interest Claculator:')
# float num with decimal int num w/o
# input method of funtion
amount = float(input('Principal amount ?'))
ir = float(input('Rate of Ineterest ?'))
yrs = int(input('Duration (no. of year ?'))
# eq 1^interest*yrs
total = (amount * pow(1 + (ir/100), yrs))
print(total)
interest = total - amount
print('\nInterest - %0.2f' % interest)
