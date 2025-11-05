str1 = "Polymorphism"
count = 0
v_count = 0
c_count = 0

for i in str1:

    if i in "aeiouAEIOU":
        v_count += 1
    elif i not in "aeiouAEIOU":
        c_count += 1

    count += 1

print(f"In '{str1}' word total letters are {count}.")
print(f"Vowels are {v_count}.")
print(f"Consonants are {c_count}.")
