# Method - 1 
a = 1
b = 5

a = a + b
b = a - b
a = a - b

print(f"a = {a}, b = {b}")

# Method - 2
x = 9
y = 7

x, y = y, x
print(f"x = {x}, y = {y}")