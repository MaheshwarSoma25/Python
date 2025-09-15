new_list = []
list1 = [1, 2, 3, 4, 5, 6]
#Reverssing the list

#Method-1
# for ind in range(len(list1)-1, -1, -1):
#   new_list.append(list1[ind])
# print(new_list)

#Method-2
# for ind in range(0, len(list1)):
#   new_list.insert(0, list1[ind])
# print(new_list)

#Method-3
low = 0
high = len(list1) - 1
while low < high:
  list1[low], list1[high] = list1[high], list1[low]
  low += 1
  high -= 1
print(list1)