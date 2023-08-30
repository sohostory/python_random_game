import random
from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    # answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    answer = random.randint(1,10)

    while True:
        try:
            guess = int(input(f'guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break

        except ValueError:
            print('please enter a number')
            continue