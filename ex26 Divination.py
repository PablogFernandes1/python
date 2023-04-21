from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-' * 20)
print('Ill think of a number between 0 and 5. Try to guess...')
print('-=-' * 20)

player = int(input('what number did i think of? '))
print('THINKING...')
sleep(3)

if player == pc:
    print('Congratulations!! you managed to beat me!')
else:
    print('I WON IDIOT! I thought of number {} not {}'.format(pc, player))