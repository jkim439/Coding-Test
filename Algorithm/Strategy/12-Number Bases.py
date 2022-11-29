def convert(n, base):
    if n == 0:
        return "0"
    numbers = "0123456789ABCDEF"
    result = ""
    while n > 0:
        n, mod = divmod(n, base)
        result += numbers[mod]
    return result[::-1]


print(convert(10, 7))
