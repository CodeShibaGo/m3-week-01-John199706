import math
def is_square(n):
    if n  < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n
result = is_square(9)
print(result)



