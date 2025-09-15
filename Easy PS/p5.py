#Check sum of middle digits vs first+last
def check_sum(num):
    num_str = str(num)
    length = 0
    for _ in num_str:
        length += 1               # Calculate length manually

    if length < 3:
        return False               # Not enough digits

    first = int(num_str[0])       # First digit
    last = int(num_str[-1])       # Last digit

    mid_sum = 0
    for i in range(1, length-1):
        mid_sum += int(num_str[i]) # Sum of middle digits

    return mid_sum == (first + last)
print(check_sum(1234))  # True (2+3 == 1+4)
print(check_sum(12345)) # False (2+3+4 != 1+5)


#Check sum of middle digits vs first+last (while loop version)
def check_sum(n):
    n_str = str(n)                 # Convert number to string
    first_last = int(n_str[0]) + int(n_str[-1])  # Sum of first and last digit
    middle_sum = 0
    i = 1
    while i < len(n_str) - 1:      # Sum of middle digits
        middle_sum += int(n_str[i])
        i += 1

    if first_last == middle_sum:
        return "equal"
    else:
        return "not equal"

print(check_sum(75547))  # equal
print(check_sum(765))    # not equal
