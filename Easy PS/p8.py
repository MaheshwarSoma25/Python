num = 75847
new_num = str(num)

first_num = new_num[0]
last_num = new_num[-1]

middle_num = new_num[1:-1]

ans = True
for i in middle_num:
    if not (i < first_num and i < last_num):
        ans = False
        break
print(ans)