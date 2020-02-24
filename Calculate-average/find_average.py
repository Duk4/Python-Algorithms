def find_average(arr):
    if len(arr) < 1:
        return 0
    return sum(arr)/len(arr)


print(find_average([3, 6, 9]))
