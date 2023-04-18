import math
n1 = float(input('enter the angle you want: '))
seno = math.sin(math.radians(n1))
print('the angle of {} has the sine of {:.2f}'.format(n1, seno))
cosseno = math.cos(math.radians(n1))
print('the angle of {} has the cosine of {:.2f}'.format(n1, cosseno))
tangente = math.tan(math.radians(n1))
print('the angle of {} has the tangent of {:.2f}'.format(n1, tangente))