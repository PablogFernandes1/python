n1 = int(input('how many days rented? '))
n2= float(input('how many km driven? '))
price = (n1 * 60) + (n2 * 0.15) 

print('the total payable is R${:.2f}'.format(price))

