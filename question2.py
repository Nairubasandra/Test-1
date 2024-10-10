import math

#using a function create a program that calculates the volume of a cylinder
radius=int(input('enter the radius of the cylinder:'))
height=int(input('enter the height of the cylinder:'))
pie = math.pi
volume=pie * radius**2 * height
print(volume)