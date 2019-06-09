# Lists ordered sequences holding a variety of object types
# 1 CREATING LISTS
# 2 INDEXING AND SLICING LISTS
# 3 LIST METHODS
# 4 NESTING LISTS
# 5 INTRO LIST COMPREHENSIONS

# 1 CREATING LISTS

# use [] and commas , to separate objects
# EX [1,2,3,4,5]
my_list = [1, 2, 3]
print(my_list)
my_list = ['STRING', 100, 23.20]
print(my_list)
print(len(my_list))

# Lists support INDEXING and SLICING
# Lists can be NESTED

# 2 INDEXING AND SLICING LISTS
print('2 SYNTAX SLICING INDEXING')
print('start:stop:step')
my_list = ['one', 'two', 'three', 4, 5]
print(my_list)
# grab everything @ index zero
print('slicing list')
print(my_list[0])
print('my_list[1:]')
print(my_list[1:])
print('my_list[:3]')
print(my_list[:3])
print('\nconcat')
my_list + ['new item']
print(my_list)

# permanent concat
print('permaconcat')
my_list = my_list + ['add new item permanently']
print(my_list)
print(my_list * 2)

# 3 LIST METHODS


print('\n.append()')
list1 = [1, 2, 3]
list1.append('append me!')
print(list1)

print('\n.pop()')
print('list1.pop(0)')
list1.pop(0)
print(list1)
print('defualt location -1')
print('second .pop()')
popped_item = list1.pop()
print('popped item')
print(popped_item)
print('')
print('\n.reverse()')

new_list = ['a', 'e', 'x', 'b', 'c']
list2 = ['3', '4', '1', '2']
# permanent
print(new_list)
new_list.reverse()
print(new_list)
# sort in alpha order
print('\n.sort()')
print(list2)
print('OR print(sorted(list2))')
print('list2.sort()/nprint(list2)')
list2.sort()
print(list2)

# 4 NESTING LISTS def. datastructures within data structures

print('\nNesting Lists')

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]

print(matrix)
print(matrix[0])
print(matrix[0][0])

# 5 INTRO LIST COMPREHENSIONS

first_col = [row[0] for row in matrix]
first_col
