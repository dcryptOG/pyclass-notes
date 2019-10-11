# DICTIONARIES
# #!UNORDERED mappings for storing objectes
#! MUTABLE
#! key-value pair access objects

# DICTIONARY SYNTAX (JSON)
# {''KEY1':VALUE1','KEY2':''VALUE2}
##
print('DICTIONARIES\n')
#! CONSTRUCTING A DICTIONARY

print('1 CONSTRUCTING A DICTIONARY\n')
print("\nSYNTAX DICTIONARY  = {'key1':'value1','key2':'value2'}\n")
my_dict = {'key1': 123, 'key2': [12, 23, 33],
           'key3': ['item0', 'item1', 'item2']
           }
print(
    "my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}")

print('SYNTAX dict[key][value]')

#!Ex create dict with IMMUTABLE VALUE
print('\n CREATE DICT w/ IMMUTABLE KEYS')
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)

# * EX create dict with mutable keys & DICT COMPREHENSION
print('\n create dict w/ MUTABLE KEYS using DICT COMPREHENSION')
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

vowels = {key: list(value) for key in keys}
# you can also use
# vowles = { key : value[:] for key in keys }
print(vowels)

# * updating the value
value.append(2)
print(vowels)
# TODO append doesn't update all values

# ACCESSING OBJECT IN DICTIONARY
print('\n2 ACCESSING OBJ FROM DICTIONARY\n')

print("my_dict['key3'][0].upper()")
print(my_dict['key3'][0].upper())
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print("\nd = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}")
print("d['k2'][-1]")
print(d['k2'][-1])
d = {'key1': {'nestkey': {'subnestkey': 'value'}}}
print("\nKEEP CALL KEY d = ['key']['nestkey']['subnestkey']")
print(d['key1']['nestkey']['subnestkey'])

# NESTING DICTIONARIES
print('\n3 NESTING DICTIONARIES\n')

print('\n4 BASIC DICTIONARY METHODS\n')

#! DICTIONARIES MUTABLE SO ITEMS CAN BE ADDED

print('\nDICTIONARY MUTABLE SO ITEMS ADDED')
print('\nADD KEY VALUE PAIRS')
d = {'k1': 100, 'k2': 200}
print(d)
print('\nADD ITEM TO DICTIONARY')
print('d[k3]=300')
d['k3'] = 300
print(d)
# REASSIGN NEW VALUE TO d
d['k1'] = 'NEW VALUE'
print("d['k1']='NEW VALUE'")
print(d)
# SEE ALL KEYS

#! BASIC DICTIONARY METHODS

print('DICTIONARY METHODS\nd.keys()')
print(d.keys())
d.values()
d.items()
print('d.values()')
print(d.values())
print('d.items()')
print(d.items())
# output for items tuples
