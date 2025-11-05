# Method - 1

# num = int(input("Enter number: "))
# count = 0

# for i in range(1, num + 1):
#   if num % i == 0:
#     count += 1
# if count == 2:
#   print("Prime")
# else:
#   print("Not a prime")

# ---------------------------------------
# Method - 2

# if num<=1:
#     print("Not prime")
# else:
#     isPrime = True
#     for i in range(2, num):
#         if num % i == 0:
#             isPrime = False
#             print("Not prime")

#     if isPrime == True:
#         print("Prime")


num = 6
if num <= 1:
    print("Not Prime")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            print("Not Prime")
            break
    if prime:
        print("Prime")
