def row_sum_odd_numbers(n):
    first_num = n * (n-1) + 1
    result = 0
    index = 0
    while index < n:
        result += first_num + (index * 2)
        index += 1
    return result


print(row_sum_odd_numbers(3))
