print('-=' * 20)
print('triangle analyzer')
print('-=' * 20)

n1 = float(input('First segment: '))
n2 = float(input('Second segment: '))
n3 = float(input('Third segement: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2: 
    print('The above segments CAN FORM a triangle')
else:
    print('The above segments CANNOT FORM a triangle')
