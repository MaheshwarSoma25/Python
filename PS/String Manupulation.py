# check the the second string is subset of first string or not, 
# if it is substring find the starting index of second string in first string
s1 = "helloworld"
s2 = "world"

found = False
for i in range(len(s1) - len(s2) + 1):
    match = True
    for j in range(len(s2)):
        if s1[i + j] != s2[j]: 
            match = False
            break
    if match:
        print("Substring found at index", i)
        found = True
        break

            

# find the largest word in given string without using split method
text = "the largest word"
freq = {}
current_word = ""

for ch in text:
    if ch != ' ':
        current_word += ch
    else:
        freq[current_word] = len(current_word)
        current_word = ""

if current_word:
    freq[current_word] = len(current_word)

max_len = 0
max_word = ""

for word in freq:
    if freq[word] > max_len:
        max_len = freq[word]
        max_word = word

print("Largest word is:", max_word)

