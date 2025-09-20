str1 = input("Enter the string: ")
mid = len(str1)//2

if len(str1)%2==0:
  count1 = 0
  for i in range(0, mid): 
    if str1[i] in "aeiouAEIOU":
      count1 += 1

  count2 = 0
  for i in range(mid, len(str1)):
    if str1[i] in "aeiouAEIOU":
      count2 += 1
  
  print(count1==count2)
else:
  print("Enter the string with even length.")