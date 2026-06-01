import math

volume = float(input("Enter the volume: "))
rad = float(input("Enter the redius: "))

height = volume/(math.pi*rad*rad)
height = float(height)

print (height)
