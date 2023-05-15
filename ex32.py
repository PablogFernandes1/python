n1 = float(input('what is the salary of the employee? R$'))

if n1 <= 1250:
    new = n1 + (n1 * 15 / 100)
else: 
    new = n1 + (n1 * 10 / 100)
    
print ('whoever won R${:.2f} will win R${:.2f}'.format(n1, new))