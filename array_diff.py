def array_diff(a, b):
    num = []
    for char in a:
        if char not in b:
            num.append(char)
    return num

result = array_diff([1,2,3,4],[2,3])
print(result)