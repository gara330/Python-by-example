import math


def cilinder_volume():
    radius = float(input("Enter de radius of the cilinder: "))
    depth = float(input("Enter the depth of the cilinder: "))
    area = (math.pi * radius) ** 2
    volume = area * depth
    print(round(volume, 3))
    pass


cilinder_volume()
