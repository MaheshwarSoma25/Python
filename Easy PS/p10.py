str1 = "Helloworld"
output = ""

for i in str1:
  if i in "aeiouAEIOU":
    for ch in i:
      if ch not in output:
        output = output + ch
print(output)