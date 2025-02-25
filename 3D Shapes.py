import math
A = int(input("please enter length: "))

cube = A**3

pi = 3.1416

r = int(input("please enter the radius: "))
h = int(input("please enter the height: "))


sphere = 4/3*pi*r**2

cone = 1/3*pi*r**2*h

cylinder = pi*r**2*h

print("heres the cubes volume: "+str(cube))

print("heres the spheres volume: "+str(sphere))

print("heres the cones volume: "+str(cone))

print("heres the cylinders volume: "+str(cylinder))






