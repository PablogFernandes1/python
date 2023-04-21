n1 = int(input('What is the current speed of the car? '))

if n1 > 80:
    print('FINED! You have exceeded the permitted limit which is 80km/h')
    fined = (n1-80) * 7
    print('You must pay a fine of R${:.2f}'.format(fined))
print('Have a good day! drive safely!')