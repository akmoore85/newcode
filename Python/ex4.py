'Divisors'
endList = []
startNumber = input('Give me a number: ')
def divides(startNumber):
    x = range(0, startNumber)
    print ("this is what we're dividing with" + str(x))
    for startNumber in x:
        print('these are all the numbers that lead up to x: ' + x)
        if startNumber // x == 0:
            endList.append(x)
print(endList)
