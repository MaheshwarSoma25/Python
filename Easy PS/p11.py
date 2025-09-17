str2 = "madam"
output = ""
for ch in str2:
  if ch not in output:
    output = output + ch
print(output)