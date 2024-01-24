def find_smallest_int(arr):
        arr.sort()
        return arr[0]

result = find_smallest_int([10, 20, 30, 40, 50])
print(result)
