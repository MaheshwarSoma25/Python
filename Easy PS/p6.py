num = 75547
new_num = str(num)

first_num = new_num[0]
last_num = new_num[-1]

middle_num = new_num[1:-1]

edge_sum = int(first_num) + int(last_num)

middle_sum = 0
for i in middle_num:
  middle_sum = middle_sum + int(i)

if edge_sum==middle_sum:
  print("Equal")
else:
  print("Not Equal")