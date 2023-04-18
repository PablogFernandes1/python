import random

n1 = str(input('first name: '))
n2 = str(input('second name: '))
n3 = str(input('third name: '))
n4 = str(input('fourth name: '))
list = [n1, n2, n3, n4]
chosen = random.choice(list)

print('The chosen student was: {}'.format(chosen))