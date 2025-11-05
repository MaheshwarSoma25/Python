num = int(input("Enter the number: "))

num1, num2 = 0, 1

for i in range(num):
    print(num1)
    new_num = num1 + num2
    num2 = num1
    num1 = new_num
