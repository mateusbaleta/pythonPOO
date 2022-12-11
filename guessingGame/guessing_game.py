# Guessing game

import random
# import sys

# answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('\nMind reader!!\n:D\n\nDone.')
            return True
    else:
        print('Out of range bro, try again.\n')


if __name__ == '__main__':
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input('What number am I thinking from 1~10?\n'))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('We only accept numbers.\n')
            continue
