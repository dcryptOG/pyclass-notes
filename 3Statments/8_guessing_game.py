
# Guessing Game Challenge

# Let's use while loops to create a guessing game.

# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#     If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#     On a player's first turn, if their guess is
#         within 10 of the number, return "WARM!"
#         further than 10 away from the number, return "COLD!"
#     On all subsequent turns, if a guess is
#         closer to the number than the previous guess return "WARMER!"
#         farther from the number than the previous guess, return "\nCOLDER!"
#     When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
# from random import randint
# comp_guess = randint(1, 100)
# print(comp_guess)

# correct = 0
# incorrect = 0
# player_guess = int(input('guess a number between 1 to 100: '))
# guesses = []

# make player guess list for \nwarmer \ncolder
# while player_guess != comp_guess:
#     player_guess = int(input('guess a number between 1 to 100: '))
#     diff = abs(player_guess - comp_guess)
#     guesses.append(player_guess)
#     x = int(len(guesses))
#     if player_guess > 100 or player_guess < 1:
#         print('OUT OF BOUNDS\ncorrect: {}\nincorrect: {}'.format(correct, incorrect))
#         incorrect += 1
#         if (abs(comp_guess - guesses[x-1]) < abs(comp_guess - guesses[x-2])):
#             print('\nwarmer')
#         else:
#             print('\ncolder')
#     if 0 < player_guess < 100 and 0 < diff <= 10:
#         print('WARM!\ncorrect: {}\nincorrect: {}'.format(correct, incorrect))
#         incorrect += 1
#         if (abs(comp_guess - guesses[x-1]) < abs(comp_guess - guesses[x-2])):
#             print('\nwarmer')
#         else:
#             print('\ncolder')
#     if 0 < player_guess < 100 and diff > 10:
#         print('COLD!\ncorrect: {}\nincorrect: {}'.format(correct, incorrect))
#         incorrect += 1
#         if (abs(comp_guess - guesses[x-1]) < abs(comp_guess - guesses[x-2])):
#             print('\nwarmer')
#         else:
#             print('\ncolder')
#     else:
#         print('{} correct answers!\n{} incorrect answers!'.format(correct, incorrect))
#         correct += 1
# print(player_guess)

##################################################################################
import random

num = random.randint(1, 100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = [0]


while True:

    # we can copy the code from above to take an input
    guess = int(
        input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number
    if guess == num:
        print(
            f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
