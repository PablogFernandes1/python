n1 = float(input('Value of house: R$'))
n2 = float(input('buyers salary: R$'))
n3 = int(input('how many years of financing?: '))
installment = n1 / (n3 * 12)

print('To pay off a R${:.2f} house in {} years'.format(n1, n3))
print('The installment will be R${:.2f}'.format(installment))
