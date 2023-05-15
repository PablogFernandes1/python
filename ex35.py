n1 = int(input('Enter a whole number: '))
print('''Choose one of the bases for the conversion
[1] Convert to BINARY
[2] Convert to OCTAL 
[3] Convert to HEXADECIMAL''')

option = int(input('Your option: '))

if option == 1:
    print('{} converted to binary is equal to {}'.format(n1, bin(n1)))
elif option == 2:
    print('{} converted to octal is equal to  {}'.format(n1, oct(n1)))
elif option == 3:
    print('{} converted to hexadecimal is equal to {}'.format(n1, hex(n1)))
else:
    print('Invalid option, try again')