def check_fermat(a, b, c, n):
    a = int(raw_input("this is a: "))
    b = int(raw_input("this is b: "))
    c = int(raw_input("this is c: "))
    n = int(raw_input("this is n: "))
    if (a**n) + (b**n) == (c**n):
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."



print check_fermat(3,6,9,2)