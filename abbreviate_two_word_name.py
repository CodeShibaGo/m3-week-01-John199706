def abbrev_name(s):
  x=0
  for char in s:
    x+=1
    if char==" ":
        break

  return f"{s[0].upper()}.{s[x].upper()}"

result = abbrev_name("John Smith")
print(result)