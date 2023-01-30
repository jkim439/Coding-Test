# Greatest Common Divisor
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# Least Common Multiple
def lcm(a, b):
    return a * b / gcd(a, b)


print(gcd(12, 18))
print(lcm(10, 12))
