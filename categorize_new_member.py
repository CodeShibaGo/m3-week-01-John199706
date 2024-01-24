def categorize_new_member(data):
     x=0
     y=[]
     for char in range(len(data)):
          if data[char][x] > 55 and data[char][x+1] > 7 :
               y.append("Senior")
          elif data[char][x] > 55 and data[char][x+1] > 7 :
               y.append("Senior")
          else:
               y.append("Open")
     return y
result = categorize_new_member([(45, 10.0), (40, 6.0)])
print(result)








