#whole numbers
# n = 0
# while n <= 10:
#     print(n)
#     n += 1

#math table
# num = int(input("Enter a number: "))
# i = 0
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i+=1

#W rite a program to check if a given number is positive, negative, or zero. 
# num = int(input("Enter a number: "))
# if num == 0:
#   print("Zero")
# elif num > 0:
#   print("Positive")
# else:
#   print("Negative")

#Determine if a number is odd or even. 
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

#Check if a person is eligible to vote (age >= 18).

# age = int(input("Enter the age:"))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

#Write a program to find the greatest of two numbers. 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")

#Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail." 
# marks = int(input("Enter tghe marks: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

#Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
# day = int(input("Enter a number 1-7: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid")

#Implement a simple calculator to perform addition, subtraction, multiplication, and division. 
# num1 = float(input("Enter the first number: "))
# symbol = str(input("Enter any symbol (+, -, *, /): "))
# num2 = float(input("Enter the second number: "))
# if symbol == "+":
#   print(num1+num2)
# elif symbol == "-":
#   print(num1-num2)
# elif symbol == "*":
#   print(num1*num2)
# elif symbol == "/":
#   print(num1/num2)

#Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.). 
# day = int(input("Enter a number 1-12: "))
# if day == 1:
#     print("Jan")
# elif day == 2:
#     print("Feb")
# elif day == 3:
#     print("Mar")
# elif day == 4:
#     print("Apr")
# elif day == 5:
#     print("May")
# elif day == 6:
#     print("June")
# elif day == 7:
#     print("July")
# elif day == 8:
#     print("Aug")
# elif day == 9:
#     print("Sept")
# elif day == 10:
#     print("Oct")
# elif day == 11:
#     print("Nov")
# elif day == 12:
#     print("Dec")
# else:
#     print("Invalid")

#Write a program to find the greatest of three numbers. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter second number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num1} and {num2}")