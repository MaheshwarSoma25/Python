#Vowels without repetition
def vowels_unique(s):
    vowels = 'aeiouAEIOU'
    result = ''
    seen = ''
    for ch in s:
        for v in vowels:
            if ch == v:
                lower_ch = ch.lower()
                already_seen = False
                for x in seen:          # Check if vowel already seen
                    if x == lower_ch:
                        already_seen = True
                        break
                if not already_seen:
                    result += ch
                    seen += lower_ch
    return result

print(vowels_unique("Helloworld"))    # eo
print(vowels_unique("Jacksparrow"))  # ao
