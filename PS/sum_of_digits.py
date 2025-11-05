# Method - 1
# num = 5451
# new_num = str(num)
# sum = 0

# for i in range(len(new_num)):
#     sum = sum + int(new_num[i])
# print(sum)

# Method - 2
num = 5451
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print(sum)