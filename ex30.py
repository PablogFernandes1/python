n1 = int(input('What year do you want to analyze? '))

if n1 % 4 == 0:
    print('The year {} is a leap year'.format(n1))
else:
    print('The year {} is not a leep year'.format(n1))