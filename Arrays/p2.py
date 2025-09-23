from array import *

# # Searching an int in array
# intInp = int(input("Enter any char: "))
# arr = array('i', [5, 8, 9, 2, 6])

# for i in range(0, len(arr)):
#   if intInp == arr[i]:
#     print(i)

# Searching a string in array
strInp = str(input("Enter any char: "))
fruits = ('u', ["apple", "banana", "cherry"])

for i in range(0, len(fruits)):
  if strInp in fruits[i]:
    print(i)