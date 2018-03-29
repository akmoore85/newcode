"""this removes a value from a list"""
def removeFromList(list_array, item):
    # Removes all instances of 'item' from 'list_array'
  for index i n list_array:
      if index == item:
          del list_array[index]
  return list_array

test_list_1 = [1,2,3,4,5]
#test_list_2 = [1,2,1,1,3]

result_1 = removeFromList(test_list_1,3)
#result_2 = removeFromList(test_list_2,1)

print ( result_1)
#print ( result_2)
print ( [1,2,3])
