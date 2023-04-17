width = float(input('wall width: '))
height = float(input('Wall height: '))

area =  width * height
ink = area / 2

print('its wall has the dimension of {}x{} and its area is {}m²'.format(width, height, area))
print('to paint this wall you will need {}l of paint'.format(ink))