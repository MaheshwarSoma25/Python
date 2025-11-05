# Remove duplicates

# str1 = "Bunny"
# new_str = ""

# for i in str1:
#     if i not in new_str:
#         new_str += i
# print(new_str)

# Reverse a string

# str1 = "Python"
# new_str = ""

# for i in str1:
#     new_str = i + new_str
# print(new_str) 

# Find the most frequent character in a string

# str1 = "maheshwar"
# freq = {}

# # Count frequency
# for i in str1:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# # find max frequency
# max_count = 0
# for j in freq:
#     if freq[j] > max_count:
#         max_count = freq[j]
# # find max characters
# max_char = ""
# for j in freq:
#     if freq[j] == max_count:
#         max_char += j

# print(f"Max character(s) is {max_char}, count is {max_count}")


# Print duplicates and its counts
str1 = "Bookkeeper"
new_str = ""
count_str = ""

for i in str1:
    if i not in new_str:
        new_str += i

for i in new_str:
    count = 0
    for j in str1:
        if i == j:
            count += 1
    if count > 1:
        count_str += i + str(count)
print(count_str)