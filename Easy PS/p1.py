#Sum of Digits of a Number
def sum_of_digits(num):
  total = 0
  while num>0:
    total = total + num%10
    num = num//10
  return total

print(sum_of_digits(1234))
