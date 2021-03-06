# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/04-Milestone%20Project%20-%201

# ! Milestone Project 1

# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

#    ! 2 players should be able to play the game (both sitting at the same computer)
#     ? The board should be printed out every time a player makes a move
#     You should be able to accept input of the player position and then place a symbol on the board

#! pick x or o


# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.

# There are 4 Jupyter Notebooks related to this assignment:

#     This Assignment Notebook
#     A "Walkthrough Steps Workbook" Notebook
#     A "Complete Walkthrough Solution" Notebook
#     An "Advanced Solution" Notebook

# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, i's totally open book, so take your time, do a little research, and remember:
# HAVE FUN!


# # * dictionary of symbols to print board
# d = {'1': '*', '2': ' ', '3': "\n"}

# a = d['1'] + d['1'] + d['3'] + d['1']

# print(a)

# def tic_tac(board):
#     patterns = {'v': '|', 'h': '_', 's': ' ', 'n': '\n', 'X': 'X',
#                 'O': 'O', 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
#     moves = []


# for pattern in patterns:
#     print(patterns['s'*5, 'v', 'n', 's'*2, 1, 's'*2, 'v'])
#  ['s'*5, 'v', 'n', 's'*2, 1, 's'*2, 'v']
# print(patterns['v']+patterns['h'])

# patterns = {'v': '|', 'h': '_', 's': ' ', 'n': '\n', 'X': 'X',
#             'O': 'O', 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# board = {1:  [1, 'v', ], 2:  [2, 'v'], 3: [3], 'n': ['n'], 'line': ['h']*3}

# print(map(patterns, board.get('line')))
# keys = ['firstKey', 'secondKey', 'thirdKey']
# for key in keys:
#     myDictionary.get(key)

# [myDictionary.get(key) for key in keys]
# for x in board:
#     print(patterns['1'])

#! concat works too try this? print(patterns['v'] + patterns['h'])

# def games(moves):
#     patterns = {'v': '|', 'h': '_', 's': ' ', 'n': '\n', 'X': 'X',
#                 'O': 'O', 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
#     board = {'1':  ['s'*5, 'v', 'n', 's'*2, 1, 's'*2, 'v'], '2': [2], '3': [3], '4': [4],
#              '5': [5], '6': [6], '7': [7], '8': [8], '9': [9]}
#     for move in moves:
#         print(patterns[move])

#! top middle bottom
# def ttt(moves):
#     patterns = {1: ['        |      |\n__{num}{val}__|'.format(num=1, val='')], 2: ['__{num}{val}__|'.format(num="2", val="")], 3: '*   *', 4: '*****',
#                 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
#     board = {1: [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [
#         4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}
#     for move in board[moves]:
#         print(patterns[move][0])


# nums = [1, 2]
# result = map(ttt, nums)
# print(ttt(1))

#! so you want a board and a moves no patterns

legend = {1: ['        |         |\n__{num}{val}__|'.format(num="1", val="")],
          2:  ['__{num}{val}__|'.format(num="2", val="")], 3: ['__{num}{val}__'.format(num="3", val="")],
          4: ['\n        |         |\n__{num}{val}__|'.format(num="4", val="")],
          5: ['__{num}{val}__|'.format(num="5", val="")], 6:  ['__{num}{val}__'.format(num="6", val="")],
          7:  ['\n        |         |\n   {num}{val}   |'.format(num="7", val="")],
          8: ['   {num}{val}   |'.format(num="8", val="")], 9: ['   {num}{val}   '.format(num="9", val="")]}


def fuck(pos):
    for b in legend[pos]:
        return b


print(fuck(1), fuck(2), fuck(3), fuck(4), fuck(
    5), fuck(6), fuck(7), fuck(8), fuck(9))

keys = {1, 2, 3, 4, 5, 6, 7, 8, 9}
moves = dict.fromkeys(keys)
print(moves)

# num = 1
# val = 'x'
pos = {1, 4, 5, 6, 9}

move = dict.fromkeys(pos, 'x')

print(move)
moves.update(move)
print(moves)

# for i in moves.get(i):
print(moves[1])
#! dictionary of win conditons
#! use a map or filter to compare
# * make a set()

win = {'a', 'd', 'i'}
a = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}
# d = {}
wins = dict.fromkeys('a', a)
win.update(wins)
print(wins)

board = ['', '', '', '', '', '', '', '', '', '', '']

print(len(board[1]))


def win_check(board):
    if len(board) > 0:
        return (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8])


print(win_check(board))
# def win(moves):
#     '''function checks if win conditions 3x across, down or diag'''
#     if moves[1][0] == moves[2][0] == moves[3][0]:
#         return True
#     if moves[4][0] == moves[5][0] == moves[6][0]:
#         return True
# i = 1
# for i in moves:
#     if i == 1 or i == 4 or i == 7 and 0 < len(moves.get(i)):
#         if moves[i][0] == moves[i+1][0] == moves[i+2][0]:
#             return True
#         else:
#             break
#     if i == 1 or i == 2 or i == 3:
#         if moves.get(i) == moves.get(i+3) == moves.get(i+6) and 0 < len(moves.get(i)):
#             return True
#         else:
#             continue
#     if i == 3:
#         if moves.get(i) == moves.get(i+2) == moves.get(i+4) and 0 < len(moves.get(i)):
#             return True
#         else:
#             continue
#     if i == 1:
#         if moves.get(i) == moves.get(i+4) == moves.get(i+8) and 0 < len(moves.get(i)):
#             return True
#         else:
#             continue
#     else:
#         continue
#     i += 1
# else:
#     return False


# print(moves[1][0] == moves[2][0] == moves[3][0])

# if type(moves.get(1)) == int and moves.get(1) == moves.get(2) == moves.get(3) or moves.get(4) == moves.get(5) == moves.get(6) or moves.get(7) == moves.get(8) == moves.get(9) or moves.get(1) == moves.get(4) == moves.get(7) or moves.get(2) == moves.get(5) == moves.get(8) or moves.get(3) == moves.get(6) == moves.get(9) or moves.get(1) == moves.get(5) == moves.get(9) or moves.get(3) == moves.get(5) == moves.get(7):

# print(moves.get(i) == moves.get(i+1) == moves.get(i+2))
# def win(moves):
#     if type(moves.get(1)) == int and moves.get(1) == moves.get(2) == moves.get(3):
#         return True
#     else:
#         return False

# val = 'x'
# pos = {1, 5}

# move = dict.fromkeys(pos, 'x')

# print(move)
# moves.update(move)
# print(moves)

# for i in moves.get(i):
# print(moves[1])
# print(moves[1][0] == moves[2][0] == moves[3][0])

# print(bool(None))
# print(moves.get(i) == moves.get(i+1) == moves.get(i+2))

# print(win(moves))
#! win conditions
# moves = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
# def fuck(pos):
#     current = []
#     for b in board[pos]:
#         current.append(b)
#     return current


test = ['Python', 'Java', 'Ruby']
s = ''
print(s.join(test))
# *start backed of game forget printing?
# while True:
#     input('Play Tic Tac Toe?')
# *
