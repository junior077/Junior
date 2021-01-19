import random
import time
player_choice = [0,1,2]
moves = ['SCISSSOR', 'PAPER', 'ROCK']
cpu_choice = random.randint(0, 2)
cpu_moves = moves[cpu_choice]
count_win = 0
count_loss = 0
count_draw = 0
print(20*'-=')
print(8*'-=', 'WELCOME', 8*'-=')
print(20*'-=')
print('''For:
        SCISSOR = [ 0 ]
        PAPER   = [ 1 ]
        ROCK    = [ 2 ]
''')
print(20*'-=')
while True:
    player = (int(input('Your turn...: ')))
    if player in player_choice:
        print(f'Your choice is... {moves[player]} !!!')
    else:
        player = (int(input('Wrong choice! Your turn...: ')))
        print(f'Your choice is... {moves[player]} !!!')

    print()
    print(f'The CPU choice is...')
    time.sleep(2)
    print(20 * '-=')
    print(f'{cpu_moves} !')
    print(20 * '-=')
    print()

    if player == 0: # SCISSOR
        if cpu_choice == 0:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a DRAW!!')
            count_draw += 1
        elif cpu_choice == 1:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a WIN!!')
            count_win += 1
        elif cpu_choice == 2:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a LOSS!!')
            count_loss += 1
    if player == 1: # PAPER
        if cpu_choice == 0:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a LOSS!!')
            count_loss += 1
        elif cpu_choice == 1:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a DRAW!!')
            count_draw += 1
        elif cpu_choice == 2:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a WIN!!')
            count_win += 1
    if player == 2: #ROCK
        if cpu_choice == 0:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a WIN!!')
            count_win += 1
        elif cpu_choice == 1:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a LOSS!!')
            count_loss += 1
        elif cpu_choice == 2:
            print(f'You have chosen {moves[player]} and CPU {cpu_moves}, thats a DRAW!!')
            count_draw += 1
    print()
    tryagain = str(input('Wanna try it again? [ Y ] / [ N ] : ' )).strip().upper()
    print(20*'-=')
    if tryagain in 'N':
        break
print('THANKS')
print(f'''
      Total of Wins  : {count_win}
      Total of Loses : {count_loss}
      Total of Draws : {count_draw}''')
print()
print(20*'-=')