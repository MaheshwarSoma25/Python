#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# * * * * * * *

# n = 7

# for i in range(n):

#   for sp in range(n-i-1):
#     print(" ", end="")

#   for j in range(n):
#     if i == n-1 or j == 0 or i == j:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# * * * * * * * 
#  * * * * * * * 
#   * * * * * * *
#    * * * * * * *
#     * * * * * * *
#      * * * * * * *
#       * * * * * * *
# for i in range(n):

#   for sp in range(i):
#     print(" ", end="")

#   for j in range(n):
#       print("*", end=" ")
#   print()

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *
# for i in range(n):

#   for sp in range(n-i-1):
#     print(" ", end="")

#   for j in range(n):
#     if i >= j:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()


# *           * 
# * *       * * 
# * * *   * * *
# * * * * * * *
# * * *   * * *
# * *       * *
# *           *
# for i in range(n):

#   for j in range(n):
#     if ((i >= j) and (i+j <= n-1)) or ((i <= j) and (i+j >= n-1)):
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()


# * * * * * * * 
#   * * * * *   
#     * * *
#       *
#     * * *
#   * * * * *
# * * * * * * *
# for i in range(n):

#   for j in range(n):
#     if (i <= j and i+j <= n-1) or (i >= j and i+j >= n-1):
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()


#     1 
#    2 2 
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
# n = 5
# count = 0
# for i in range(n):
#   for sp in range(n-i-1):
#     print(" ", end="")
#   count += 1
#   for j in range(n):
    
#     if i>=j:
#       print(count, end=" ")
      
#   print()

# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# for i in range(n):
#   count = 1
#   for j in range(n):
#     if i>=j:
#       print(count, end=" ")
#       count += 1
#   print()


# 1 
# 0 1 
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# for i in range(n):

#   for j in range(n):
#     if i>=j:
#       if (i+j)%2==0:
#         print(1, end=" ")
#       else:
#         print(0, end=" ")
#   print()


#         1 
#       2 1 2 
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
# n = 5

# for i in range(n):
#   is_one = False

#   start = i+1
#   for sp in range(2*(n-i-1)):
#      print(" ", end="")

#   for j in range(2 * i + 1):
#       print(start, end=" ")

#       if start==1:
#         is_one = True
      
#       if is_one == False:
#         start -= 1
#       else:
#          start += 1

#   print()

n = 5
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print("*", end=" ")
  print()

for i in range(n):
  for j in range(n):
    if i>=j:
      print("*", end=" ")
  print()

  