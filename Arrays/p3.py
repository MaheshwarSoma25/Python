from array import *

arr = array("i", [])

n = int(input("Enter the range: "))

for i in range(n):
  val = int(input("Enter the value: "))
  arr.append(val)

print(arr)

intInp = int(input("Search the value: "))

for i in range(0, len(arr)):
  if intInp == arr[i]:
    print(i)

print(arr.index(intInp))