given = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = []

# for i in range(0, len(given)):
#     if i % 2 != 0:
#         evens.append(given[i])
evens = [even for even in given if even % 2 == 0]
print(evens)
