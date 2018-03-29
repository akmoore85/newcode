from distanceCalculator import distance
import math

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    return radius

print circle_area(2,4,6,8)