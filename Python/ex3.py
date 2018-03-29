a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
higher = []
lower = []
for i in a:
  if i > 5:
      higher.append(i)
  else:
      lower.append(i)


print(higher, lower)
