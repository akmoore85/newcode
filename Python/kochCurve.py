from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def koch(t, n):
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    bob.delay = .001

print koch(bob, 20000)