# Tower of Hanoi
def tower_of_hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    tower_of_hanoi(n - 1, start, 6 - start - end)
    print(start, end)
    tower_of_hanoi(n - 1, 6 - start - end, end)


n = int(input())
print(2**n - 1)
tower_of_hanoi(n, 1, 3)


# Fibonacci
def fibonacci_recursive_call(n):
    if n <= 1:
        return n
    return fibonacci_recursive_call(n - 2) + fibonacci_recursive_call(n - 1)


print(fibonacci_recursive_call(10))
