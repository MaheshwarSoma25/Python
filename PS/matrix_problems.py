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
  
# # Add two matrices
# m1 = [
#   [1, 2],
#   [4, 5]
# ]
# m2 = [
#   [1, 2],
#   [4, 5]
# ]

# for i in range(len(m1)):
#   for j in range((len(m1[i]))):
#     print(m1[i][j]+m2[i][j], end=" ")
#   print()

# # Multiply two matrices
# m1 = [
#   [1, 2],
#   [4, 5]
# ]
# m2 = [
#   [1, 2],
#   [4, 5]
# ]



# # Sum of diagonal elements
# list1 = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# sum = 0

# for i in range(len(list1)):
#   for j in range((len(list1[i]))):
#     if i==j:
#       sum += list1[i][j]
# print(sum)

# # Check if the given matrix is an identity matrix
# list1 = [
#   [1, 0, 0],
#   [0, 1, 0],
#   [0, 0, 1]
# ]
# is_identity = True

# for i in range(len(list1)):
#   for j in range((len(list1[i]))):
#     if (i==j and list1[i][j]!=1) or (i!=j and list1[i][j]!=0):
#       is_identity = False
#       break
#   if not is_identity:
#     break

# if is_identity:
#   print("Identity")
# else:
#   print("Non Identity")