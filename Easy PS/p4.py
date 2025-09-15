#Middle character(s) of a string
s = "Python"
mid = len(s)//2
if len(s) % 2 == 0:
  print(s[mid-1:mid+1])
else:
  print(s[mid])



def middle_char(s):
    length = 0
    for _ in s:
        length += 1               # Calculate length manually

    mid = length // 2             # Middle index
    result = ''

    if length % 2 == 0:           # Even length
        i = 0
        for ch in s:
            if i == mid-1 or i == mid:
                result += ch
            i += 1
    else:                         # Odd length
        i = 0
        for ch in s:
            if i == mid:
                result += ch
            i += 1
    return result

print(middle_char("Wonder"))  # nd
print(middle_char("World"))   # r
print(middle_char("6969"))    # 96
