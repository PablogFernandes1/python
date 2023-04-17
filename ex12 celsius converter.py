print('celsius converter')

options = ["Fahrenheit","Kelvin"]

count = 1
for option in options:
    print(f"{count} - {option}")
    count += 1

option_typed = int(input('which option do you want? '))

if option_typed == 1: 
    g = float(input('enter its value in degrees: '))
    calculation = ((g * 9) / 5) + 32

    print('the value of {}ºC is {}ºF'.format(g, calculation))

if option_typed == 2:
    g = float(input('enter its value in degrees: '))
    calculation = g + 273.15

    print('the value of {}ºC is {}K'.format(g, calculation))