print ('THE FINAL NOTE')

n1 = float(input('students first grade: '))
n2 = float(input('students second grade: '))
n3 = float(input('Students third grade: '))
n4 = float(input('Students fourth grade: '))

media = (n1 + n2 + n3 + n4) / 4

print ('The final average of your report card is: {}'.format(media))

if media >= 7:
    print("Approved")
else: 
    print("Not approved")
    
    