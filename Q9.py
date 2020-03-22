import random

x = random.randint(1,9)
guess = eval(input('Enter a number to guess in range (1-9): '))


if guess<x:
    print('Too low')
elif guess==x:
    print('Exacly right')
else:
    print('Too high')
