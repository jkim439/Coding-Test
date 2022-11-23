# Greatest Common Divisor
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(gcd(12, 18))


# Least Common Multiple
def lcm(a, b):
    return a * b / gcd(a, b)


print(lcm(10, 12))
