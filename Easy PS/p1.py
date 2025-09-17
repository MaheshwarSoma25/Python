#Sum of the digits
num = 12345
new_num = 0
while num>0:
  new_num = new_num + num%10
  num = num//10
print(new_num)