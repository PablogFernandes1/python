n1 = str(input('enter a phrase: ')).upper() .strip()

print ('the letter A appears {} times in the sentence '.format(n1.count('A')))
print ('the first letter A appeared in position {}'.format(n1.find('A')+1))
print ('The last letter A appeared in position {}'.format(n1.rfind('A')+1))