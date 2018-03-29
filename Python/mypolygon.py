from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
ray = Turtle()
print bob

def square(t, length):
    for i in range (4):
        fd(t, length)
        lt(t)

def polygon(t, length, side):
     angle = 360/side
     for i in range (int(0), int(side)):
         fd(t, length)
         lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)
    bob.delay = 0.001

print circle(bob, 30)
print polygon(ray, 80, 6)
print square(bob, 250)
wait_for_user()