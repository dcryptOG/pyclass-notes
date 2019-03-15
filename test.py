board = {1: ['_', 1, '_', '|'], 2: [
    '_2_|'], 3: ['_3_'], 4: ['\n_4_|'], 5: [
    '_5_|'], 6: ['_6_'], 7: ['\n 7 | '], 8: [' 8 |'],
    9: [' 9 ']}
print(board[1][0], board[1][1], board[1][2])


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
