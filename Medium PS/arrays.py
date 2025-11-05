# list1 = list(map(int, input("Enter numbers: ").split(",")))

# count = 0
# for num in list1:
#     num_str = str(num)
#     if num_str[0] == num_str[-1]:
#         count += 1
# print(count)

# -----------------------------------------------------

# list1 = list(map(int, input("Enter numbers: ").split(",")))

# for i in range(len(list1)):
#     new_num = list1[i]+1
#     if new_num > 1:
#       for j in range(2, int(new_num*0.5)+1):
#         if new_num%j == 0:
#           break
#         else:
#           print(list1[i], end=" ")
#           break

# -----------------------------------------------------

# list1 = list(map(int, input("Enter numbers: ").split(",")))
# second_input = int(input("Enter the number: "))

# result = 1
# for i in range(2, second_input+1):
#     result = result * i

# if result in list1:
#     print(list1.index(result))
# else:
#     print("Not found")

# -----------------------------------------------------

# num = int(input("Enter the number: "))
# new_num = ""
# duplicates = ""

# for i in str(num):
#     if i not in new_num:
#         new_num += i
#     elif i not in duplicates:
#         duplicates += i

# sum = 0
# for d in duplicates:
#     sum = sum + int(d)
# print(sum)

# -----------------------------------------------------

list1 = list(map(int, input("Enter numbers: ").split(",")))
freq = {}
duplicates = []

for i in list1:
    if i in freq:
        freq[i] += 1

        if freq[i] == 2:
            duplicates.append(i)

        if len(duplicates) == 2:
            break
    else:
        freq[i] = 1
      
if len(duplicates) < 2:
    print("No Duplicates")
else:
    second_duplicate = duplicates[1]
    count = 0
    for j in list1:
        if j == second_duplicate:
            count += 1
print(f"Second duplicate number is {second_duplicate} and it is occurred {count} times")