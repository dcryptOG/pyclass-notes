board = {1: ['__{num}{val}__|'.format(num="1", val="")], 2:  ['__{num}{val}__|'.format(num="2", val="")], 3: ['__{num}{val}__'.format(num="3", val="")],
         4: ['\n__{num}{val}__|'.format(num="4", val="")], 5: ['__{num}{val}__|'.format(num="5", val="")], 6:  ['__{num}{val}__'.format(num="6", val="")],
         7:  ['\n   {num}{val}   |'.format(num="7", val="")], 8: ['   {num}{val}   |'.format(num="8", val="")], 9: ['   {num}{val}   '.format(num="9", val="")]}
# print(board[1][0], board[1][1], board[1][2])


# def fuck(pos):
#     current = []
#     for b in board[pos]:
#         current.append(b)
#     return current

def fuck(pos):
    for b in board[pos]:
        print(b)
    return b


nums = [1, 2, 3, 5, 6, 7, 8, 9]
for num in nums:
    print(fuck(num))
print(fuck(1), fuck(2), fuck(3), fuck(4), fuck(
    5), fuck(6), fuck(7), fuck(8), fuck(9))
