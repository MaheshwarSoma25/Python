#Print middle character(s) in the given string or number
#String
str1 = "Python"
length = len(str1)
div = length//2
if length%2==0:
  print(str1[div-1],str1[div])
else:
  print(str1[div])
  
# #Number
num = 123456
new_num = str(num)

length = len(new_num)
div = length//2
if length%2==0:
  print(new_num[div-1],new_num[div])
else:
  print(new_num[div])
