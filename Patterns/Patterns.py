num = int(input("Enter the number: "))

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55




# for i in range(1, num+1):
#     for j in range(num-i+1):
#         print("*", end=" ")
#     print()

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# n = ord('A')
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(chr(n), end=" ")
#         n+=1
#     print()

# 11 12 13 14 15 16 17 18 19
# 21 22 23 24 25 26 27 28 29
# 31 32 33 34 35 36 37 38 39
# 41 42 43 44 45 46 47 48 49
# 51 52 53 54 55 56 57 58 59
for i in range(1, num+1):
    for j in range((num-1)+i, num+i):    
        print("*", end=" ")
    print()