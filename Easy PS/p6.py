#Check middle digits < first and last
def check_middle(num):
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

    return mid_sum < (first + last)
print(check_middle(1234))  # True (2+3 < 1+4)

#Check middle digits < first and last (while loop version)
def middle_less(n):
    n_str = str(n)
    first = int(n_str[0])
    last = int(n_str[-1])
    i = 1
    while i < len(n_str) - 1:
        if int(n_str[i]) >= first or int(n_str[i]) >= last:
            return False           # If any middle digit ≥ first or last, return False
        i += 1
    return True                    # All middle digits are smaller

print(middle_less(1672))   # False
print(middle_less(84719))  # True
