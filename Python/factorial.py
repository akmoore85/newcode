import math

def fact(num):
    for i in range(num, 1, -1):
        product = []
        if i == num:
            i-=1
        elif i == 1:
            pass
        else:
            i-=1 
print fact(4)