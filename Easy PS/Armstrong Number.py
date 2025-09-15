num = int(input("Enter any number: "))
org_num = num
sum = 0

while num>0:
    reminder = num%10
    sum += reminder**3
    num = num//10

print(sum)
if sum==org_num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")