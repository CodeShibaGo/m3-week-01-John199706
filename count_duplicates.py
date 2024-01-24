def count_duplicates(text):
    x=0
    text=text.lower()
    num=set(text)
    for i in num:
        if text.count(i)>1:
            x+=1
    return x
