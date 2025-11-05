# Recursion

# count = 0
# def example():
#   global count
#   if count>=5:
#     return
#   count += 1
#   print(count)
#   example()
# example()

# def sample_func(n):
#   if n<=0:
#     return
  
#   print(n)
#   sample_func(n-1)
#   print(n)
# sample_func(10)


# Factorial of a number

# def fact(n):
#   if n == 1:
#     return 1
  
#   return n * fact(n-1)
# print(fact(10))

# Sum of digits

# def sum_of_digits(num1):
#   if num1<10:
#     return num1

#   return num1 % 10 + sum_of_digits(num1 // 10)
# print(sum_of_digits(1234))

# Reverse a string

# def reverse_string(str1):
#   if len(str1) <= 1:
#     return(str1)

#   return str1[-1] + reverse_string(str1[ : len(str1)-1])
# print(reverse_string("Good Morning"))

# Multplication without using * operator

# def mul(num1, num2):
#   if num2 == 1:
#     return num1
#   if num2 == 0:
#     return 0

#   return num1 + mul(num1, num2-1)
# print((mul(5, 3)))

# Power without using ** operator

# def mul(num1, num2):
#   if num2 == 1:
#     return num1
#   if num2 == 0:
#     return 0

#   return num1 * mul(num1, num2-1)
# print((mul(5, 3)))
# print(5**3)

# Reverse a List

# def reverse_list(list1):
#   if len(list1) <= 0:
#     return list1
#   return [list1[-1]] + reverse_list(list1[ :-1])

# print(reverse_list([1,2,3,4,5,6,7,8,9]))

# def reverse_list(list1):
#   if len(list1) == 0:
#     return
#   print(list1[-1])
#   reverse_list(list1[ :-1])

# print(reverse_list([1,2,3,4,5,6,7,8,9]))


# Fibonacci

# def fibo(n):
#   if n == 0 or n == 1:
#     return n
#   return fibo(n-1) + fibo(n-2)

# print(fibo(4))

# Palindrome

# def palindrome(str1):
#   if len(str1) <= 1:
#     return True
#   return str1[0] == str1[-1] and palindrome(str1[1 : -1])
# print(palindrome("MALAYALAM"))


# max element in list

# list1 = [1, 5, 8, 6, 7, 2]

# def max_element(list1):
#   if len(list1) == 0:
#     return "Invalid"
#   if len(list1) == 1:
#     return list1[0]

#   first_element = list1[0]
#   rem_elements= max_element(list1[1: ])
#   return first_element if first_element > rem_elements else rem_elements

# print(max_element(list1))


# Binary Search

list1 = [1, 2, 3, 4, 5]

def binary_search(list1, search_elem, low, high):
  if low > high:
    return -1
  
  mid = (low + high)//2
  if list1[mid] == search_elem:
    return mid
  elif list1[mid] > search_elem:
    return binary_search(list1, search_elem, low, mid-1)
  else:
    return binary_search(list1, search_elem, mid+1, high)

print(binary_search(list1, 4, 0, len(list1)-1))