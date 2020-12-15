

def reverse(num):

    result = 0
    m = 1
    if num < 0:
        m = -1
        num = m * num
    while num != 0:
        result = result * 10 + num % 10
        num = int(num / 10)
    result *= m
    if result > pow(2, 31) - 1 or result < -pow(2, 31):
        return 0

    return result

print(reverse(-123456))