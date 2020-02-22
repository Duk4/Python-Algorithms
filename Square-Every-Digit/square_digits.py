def square_digits(num):
    string = str(num)
    result = ''
    for number in string:
        square = int(number)**2
        result += str(square)
    return int(result)


print(square_digits(9119))
