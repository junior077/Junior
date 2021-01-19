import random
import time
import itertools
randlist = list()
tot = 0
print(19*'-=', 'LUCKY LOTTO', 19*'-=')
print()
print(20*'-=', 'Rules', 20*'-=')
print('''
      You have a sequence of 6 numbers per ticket.
      Firstly you need to input how many tickets you
      would like to play with.
      Then just sit and wait for the computer analyze
      and gives you some good news... or not ! :D ''')
print()
guess = int(input('How many tickets would you like? '))
while tot < guess:
    while True:
        games = random.sample(range(1, 60), 6)
        randlist.append(games)
        tot += 1
        if tot == guess:
            break
        randlist.sort()
print()
print('You have randomized picket the following combinations! :')
print(f'{randlist}')
print()
print('Waiting for the computer...')
time.sleep(1)
cpu = random.sample(range(1, 60), 6)
print(f'The computer selection is...{cpu} !')
print()
print('Analyzing...')
time.sleep(1)
if cpu in randlist:
    print('You have WON!! ')
else:
    print('You have lost... :( ')