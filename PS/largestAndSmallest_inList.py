list1 = [2, 5, 1, 7, 3, 9]
max_num = list1[0]
min_num = list1[0]

for i in range(len(list1)):
    if list1[i] > list1[0]:
        max_num = list1[i]

    elif list1[i] < list1[0]:
        min_num = list1[i]

print(f"Max is {max_num} and Min is {min_num}")