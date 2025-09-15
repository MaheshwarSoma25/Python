#Reverse a Number
num = 1234
new_num = 0

while num > 0:
  dig = num % 10
  new_num = new_num*10 + dig
  num = num // 10
print(new_num)