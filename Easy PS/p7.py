#Vowels in reverse order
def vowels_reverse(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for ch in s:
        for v in vowels:
            if ch == v:
                result = ch + result  # Prepend to reverse the order
    return result

print(vowels_reverse("Helloworld"))   # ooe
print(vowels_reverse("JackspArrow"))  # oAa
