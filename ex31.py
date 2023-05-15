n1 = int(input('First value: '))
n2 = int(input('Second value: '))
n3 = int(input('Third value: '))
smaller = n1 

if n2 < n1 and n2 < n3:
    smaller = n2
if n3 < n1 and n3 < n2:
    smaller = n3 
    
print ('The smallest value entered was: {}'.format(smaller))
