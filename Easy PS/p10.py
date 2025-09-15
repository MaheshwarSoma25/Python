#Toggle case
str1 = "PyThOn"
new_str = ""
for char in str1:
    if char.islower():
        new_str += char.upper()
    else:
        new_str += char.lower()
print(new_str)  # pYtHoN
