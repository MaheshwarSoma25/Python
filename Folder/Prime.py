lower = 1
upper = 100


for num in range(lower, upper + 1):
    if num > 1:  # primes are greater than 1
        for i in range(2, int(num**0.5) + 1):  # check divisibility up to sqrt(num)
            if num % i == 0:
                break
        else:
            print(num)

