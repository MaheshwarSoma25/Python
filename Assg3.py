#1. Given the total seconds, compute and print equivalent hours, minutes, and seconds using arithmetic operations.
n = int(input("Enter the number: "))
hr = n//3600
min = (n%3600)//60
sec = n%60
print(f"{hr}hr {min}min {sec}sec")

#2. Assign the price and quantity of two products. Calculate the total cost including 18% tax. Print a detailed bill.
p1, q1 = 5000, 2
p2, q2 = 200, 7

subtotal = (p1*q1) + (p2*q2)
tax = subtotal*0.18

total = subtotal+tax

#Detailed Bill
print(f"Product 1: Price: {p1}Rs x Quantity: {q1} = Rs.{p1*q1}")
print(f"Product 2: Price: {p2}Rs x Quantity: {q2} = Rs.{p2*q2}")
print(f"Tax: {tax}")
print(f"Total Bill: Rs.{total}")

#3. Compute the perimeter and area of a circle given a radius. Use the value of π from the math module.
import math
r = int(input("Enter the radius of the circle: "))
peri = 2*math.pi*r
area = math.pi*r**2

print(f"Perimeter of the circle is {peri}")
print(f"Area of the circle is {area}")

#4. Given a temperature in Celsius, convert it to Fahrenheit using the formula and print both values. (F = C × 9/5 + 32)
c = int(input("Enter the Celsius: "))
f = c*9/5+32
print(f"Celsius: {c}")
print(f"Fahrenheit: {f}")

#5. What is a compiled language? What is an interpreted language? Explain pros and cons of each. How hybrid languages bring in advantages of both.
#   Compiler language executes all the code at once. Pros:- Faster execution. Cons: Harder to debug.
#   Interpreter executes the code line by line. Pros:- Easier to debug. Cons of interpreter: Slower execution than Compiler.

#6. Draw the diagram of how a Python program is executed.
