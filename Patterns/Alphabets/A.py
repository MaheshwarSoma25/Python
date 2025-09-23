n = int(input("Enter the number: "))
mid = n//2

# A
for i in range(n):
  for j in range(n):
    if i==0 or j==0 or j==n-1 or i==mid:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()