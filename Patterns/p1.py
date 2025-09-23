n = 7
imid = n//2
jmid = (n-1)//2

# * * * * * * * 
# *     *     * 
# *     *     * 
# * * * * * * * 
# *     *     * 
# *     *     * 
# * * * * * * * 

for i in range(n):
  for j in range(n):
    if i==0 or j==0 or j==n-1 or j==jmid or i==n-1 or i==imid:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()