#Sum of the digits
# num = 12345
# new_num = 0
# while num>0:
#   new_num = new_num + num%10
#   num = num//10
# print(new_num)

#Reverse the number
# num = 12345
# new_num = 0

# while num>0:
#   new_num = new_num*10 + num%10
#   num = num//10
# print(new_num)

#Reverse a string
# str1 = "Python"
# new_str = ""

# for i in str1:
#   new_str = i + new_str
# print(new_str)

#Factorial
# num = 5

# for i in range(1, num):
#   num = num * i
# print(num)

#Print middle character(s) in the given string or number
#String
# str1 = "Python"
# length = len(str1)
# div = length//2
# if length%2==0:
#   print(str1[div-1],str1[div])
# else:
#   print(str1[div])
  
# #Number
# num = 123456
# new_num = str(num)

# length = len(new_num)
# div = length//2
# if length%2==0:
#   print(new_num[div-1],new_num[div])
# else:
#   print(new_num[div])



# num = 75547
# new_num = str(num)

# first_num = new_num[0]
# last_num = new_num[-1]

# middle_num = new_num[1:-1]

# edge_sum = int(first_num) + int(last_num)

# middle_sum = 0
# for i in middle_num:
#   middle_sum = middle_sum + int(i)

# if edge_sum==middle_sum:
#   print("Equal")
# else:
#   print("Not Equal")



# num = 7554
# new_num = str(num)

# first_num = new_num[0]
# last_num = new_num[-1]

# if first_num==last_num:
#   print(True)
# else:
#   print(False)



# num = 75847
# new_num = str(num)

# first_num = new_num[0]
# last_num = new_num[-1]

# middle_num = new_num[1:-1]

# ans = True
# for i in middle_num:
#     if not (i < first_num and i < last_num):
#         ans = False
#         break
# print(ans)


#Reverse the vowels 
# str1 = "Helloworld"
# new_str = ""

# for i in str1:
#   if i in "aeiouAEIOU":
#     for j in i:
#       new_str = i + new_str
# print(new_str)



# str1 = "JackSparrow"
# output = ""

# for i in str1:
#   if i in "aeiouAEIOU":
#     for ch in i:
#       if ch not in output:
#         output = output + ch
# print(output)


# str2 = "Hello"
# output = ""
# for ch in str2:
#   if ch not in output:
#     output = output + i
# print(output)


# str1 = "madam"
# output = ""
# output2 = ""
# for ch in str1:
#   if str1.count(ch)==1:
#     output = output + ch
# print(output)


# str1 = "JohnWick"
# result = ""

# for i in str1:
#   if i.isupper():
#     result = result + i.lower()
#   elif i.islower():
#     result = result + i.upper()
#   else:
#     result = result + i
# print(result)

str1 = "NumberOne"
result = ""

for i in str1:
  if i.isupper():
    result = i + result
  elif i.islower():
    result = result + i
print(result)
    
    









