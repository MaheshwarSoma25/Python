#Remove duplicate characters
str1 = "programming"
new_str = ""
for char in str1:
    if char not in new_str:
        new_str += char
print(new_str)  # progamin
