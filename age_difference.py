def age_difference(ages):
    x=0
    y=1000
    for char in ages:
        if char > x:
            x = char
        elif char == x:
            x= char
        else:
            x=x
    for char1 in ages:
        if  char1>y:
            y=y
        elif char1 == y:
            y = char1
        else:
            y=char1
    return (y,x)

result = age_difference([18, 25, 50, 35, 40])
print(result[1]-result[0])