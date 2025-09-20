list1 = [1,2,3,4,5,6,7]
low, high = 0, len(list1)-1
search = 5

while low <= high:
  mid = (low+high)//2

  if list1[mid] == search:
    print(mid)
    break
  elif list1[mid] > search:
    high = mid - 1
  else:
    low = mid + 1

