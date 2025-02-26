#Joey #2/26/2025

import math
a = int(input("please enter length: "))
#for getting the length of the shape
cube = a**3
#using the length to find the volume of the cube
pi = 3.1416
#this is pi
r = int(input("please enter the radius: "))
h = int(input("please enter the height: "))
#for getting radius & height of the cone of cylinder.

sphere = 4/3*pi*r**2
#getting the sphere volume
cone = 1/3*pi*r**2*h
#getting the cones volume
cylinder = pi*r**2*h
#getting the volume of the cylinder
print("heres the cubes volume: "+str(cube))
#printing the cubes volume
print("heres the spheres volume: "+str(sphere))
#printing the spheres volume
print("heres the cones volume: "+str(cone))
#printing the cones volume
print("heres the cylinders volume: "+str(cylinder))
#printing the cylinders volume

print("finished")



