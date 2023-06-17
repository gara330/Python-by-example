import math

def circle_radius():
    radius = float(input("Enter the radius: "))
    area = (math.pi * radius) ** 2
    print(round (area, 2))
    pass

circle_radius()
