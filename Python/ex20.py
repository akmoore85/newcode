# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is
# inside the list and returns (then prints) an appropriate boolean.

def isIncluded(search, element):

    element = [i for i in search if element == i]
    if len(element) > 0:
        return True
    return False

mylist = [1,2,3,4,5]
included = isIncluded(mylist, 2)

print(included)
