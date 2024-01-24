def distinct(seq):
    ex = []
    for i in seq:
        if i not in ex:
            ex.append(i)
    return ex


result = distinct("AaBbCde")
print(result)