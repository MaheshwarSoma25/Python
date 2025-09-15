#1. What are variables and why are they called variables? Assign two numbers to variables `a` and `b`, and print their sum.
a = 10
b = 20
print(a + b)

#2. Write a Python program to subtract two numbers and print the result.
a = 15
b = 8
print(a - b)

#3. Multiply two variables and store the result in a third variable. Print all three.
num1 = 6
num2 = 7
product = num1 * num2
print(num1, num2, product)

#4. Divide 10 by 3 and print the result with and without decimals.
print(10/3) 
print(int(10/3))

#5. Use floor division `//` to divide 17 by 4. Print the output.
result = 17//4
print(result)

#6. Use the modulo operator `%` to check the remainder when 25 is divided by 6.
remainder = 25%6
print(remainder)

#7. Calculate and print the square of a number stored in a variable.
a = 9
print(a**2)

#8. Assign values to three variables `x`, `y`, `z` and compute the average.
a = 5
b = 10
c = 15
average = (a+b+c)/3
print(average)

#9. Take a number and find its cube using the `**` operator.
num = 4
print(num ** 3)

#10. Create two variables `length` and `width`. Calculate and print area of a rectangle.
length = 12
width = 5
area = length * width
print(area)

#11. Assign a variable `total_marks = 450` and `obtained_marks = 375`. Find percentage.
total_marks = 450
obtained_marks = 375
percentage = (obtained_marks / total_marks) * 100
print(percentage, "%")

#12. Write a Python statement that calculates `(a + b) * c` for some values of a, b, and c.
a = 2
b = 3
c = 4
result = (a + b)*c
print(result)

#13. Draw and show how reassignment changes variable reference to a memory block.
# Reassignment example
x = 5 
# x = 10  # x points to a new memory block
print(id(x))

