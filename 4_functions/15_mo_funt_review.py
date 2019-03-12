# Just for fun:
#! PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# todo FINISH THIS ONE TOO
# print_big('a')

# out:   *
#       * *
#      *****
#      *   *
#      *   *

# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

# def print_big(letter):
#     pass

# print_big('a')


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****',
                5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [
        4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
