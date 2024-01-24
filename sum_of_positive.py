def positive_sum(arr):
    x=0
    for char in arr:
        if char >= 0:
            x=x+char
    return x
