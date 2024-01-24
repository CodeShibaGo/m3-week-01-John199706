def century(year):
    if year%100==0:
        x=int(year/100)
    else:
        x=int(year/100)+1
    return x

