str1 = input("Enter any character: ")
vowels = "aeiouAEIOU"
mid = len(str1)//2

if len(str1)%2 == 0:
  for i in range(0, mid):
    count1 = 0
    if str1[i] in vowels:
      count1 += 1
  for j in range(mid, len(str1)):
    count2 = 0
    if str1[j] in vowels:
      count2 += 1
  print(True) if count1 == count2 else print(False)

else:
  print(False)
    

