def find_capitals(word):
    for char in word:
        if char.isupper() == False:
            word = word.replace(char,"")


    return word

result = find_capitals("The Quick Brown Fox")
print(result)