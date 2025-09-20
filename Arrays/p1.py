from array import *

# Create an array 
arr = array('i', [1, 2, 3, 4, 5, 6])

# Create a new array from existing array
# newArr = array(arr.typecode, (a for a in arr))

#Assigning Square of a number
newArr = array(arr.typecode, (a**2 for a in arr))

for i in newArr:
  print(i)