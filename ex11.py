n1 = float(input('what is the salary of the employee? R$'))
incrise = n1 + (n1 * 15 / 100)

print('The employee who earned R${}, with a 15% increase, started to receive R${:.2f}'.format(n1, incrise))