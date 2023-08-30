import sys
from random import randint

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

answer = randint(min_num, max_num)

is_game_over = False

while not is_game_over:
    guess = int(input("Guess a number: "))

    if guess == answer:
        print(f'You are correct. The correct number is {answer}.')
        print('Game over')
        is_game_over = True
    elif guess < answer:
        print('Too low, guess a higher number')
    else:
        print('Too high, guess a lower number')

