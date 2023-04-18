n1 = str(input('enter your full name: ')).strip()

print('Your name in capital letters is: {}'.format(n1.upper()))
print('Your lowercase name is: {}'.format(n1.lower()))
print('your name has all {} letters'.format(len(n1) - n1.count(' ')))
         
    