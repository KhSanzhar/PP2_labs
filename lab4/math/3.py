from math import tan, pi
n = int(input('Input number of sides: '))
s = float(input('Input the length of a side: '))
ap = (n * s**2 * (1/tan(pi/n))) / 4
print('The area of the polygon is:', ap)