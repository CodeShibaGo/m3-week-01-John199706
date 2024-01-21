def unique_in_order(iterable):
    x=" "
    num=[]
    for char in iterable:
        if char != x:
            x = char
            num.append(char)

        else:
            x = char


    return num

result = unique_in_order("AAAABBBCCDAABBB")
print(result)