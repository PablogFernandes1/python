n1 = float(input('What is the distance of your trip? '))
print('You are about to start a journey of {}km '.format(n1))

if n1 <= 200:
    price = n1 * 0.50
else: 
    price = n1 * 0.45
print('and the price of this ticket will be R${:.2f}'.format(price))