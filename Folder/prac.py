# list1 = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# for i in range(len(list1)):
#   for j in range((len(list1[i]))):
#     if i==j:
#       print(list1[i][j], end=" ")
#     else:
#       print(" ", end=" ")
#   print()
  
n = 7



for i in range(n):
  for j in range(n):
    if i==0 or i+j==n-1 or i==j or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()