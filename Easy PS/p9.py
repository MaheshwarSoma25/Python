#Reverse the vowels 
str1 = "Helloworld"
new_str = ""

for i in str1:
  if i in "aeiouAEIOU":
    for j in i:
      new_str = i + new_str
print(new_str)