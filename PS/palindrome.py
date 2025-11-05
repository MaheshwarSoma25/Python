# Method - 1
str1 = "madam"
is_palindrome = True

for i in range(len(str1)//2):
    if str1[i] != str1[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")

# Method - 2
if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

