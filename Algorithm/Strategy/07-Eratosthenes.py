def eratosthenes(n):
    a = [1] * (n + 1)

    for i in range(2, int(n**0.5)):
        if a[i]:
            for j in range(i + i, n + 1, i):
                a[j] = 0

    return [k for k in range(2, n + 1) if a[k]]


print(eratosthenes(211))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(211))
