list1 = [8, 78, 6, 9, 4, 2, 10]

for i in range(len(list1)):
    for j in range(len(list1) - 1 - i):
        if list1[j] < list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(f"2nd largest element in {list1} is {list1[1]}")