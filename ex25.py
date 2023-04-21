n1 = str(input('enter your full name: ')).strip()
n2 = n1.split()

print('Nice to meet you!')
print('Your first name is: {}'.format(n2[0]))
print('Your last name is: {}'.format(n2[len(n2)]-1))