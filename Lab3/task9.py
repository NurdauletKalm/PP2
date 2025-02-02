import math
def vsr(radius):
    volume = (4 / 3) * math.pi * radius
    return volume
radius = int(input())
print(vsr(radius))