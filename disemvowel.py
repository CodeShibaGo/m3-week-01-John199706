def disemvowel(s):
    for letter in "aeiouAEIOU":
        s=s.replace(letter,"")
    return s
result=disemvowel("hello")
print(result)
