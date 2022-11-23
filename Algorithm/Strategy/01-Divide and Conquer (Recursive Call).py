# Tower of Hanoi
def tower_of_hanoi(start, end, n, path):
    if n == 1:
        path.append([start, end])
    else:
        empty = 6 - start - end
        tower_of_hanoi(start, empty, n - 1, path)
        path.append([start, end])
        tower_of_hanoi(empty, end, n - 1, path)
    return path


print(tower_of_hanoi(1, 3, 3, []))


# Fibonacci
def fibonacci_recursive_call(n):
    if n <= 1:
        return n
    return fibonacci_recursive_call(n - 2) + fibonacci_recursive_call(n - 1)


print(fibonacci_recursive_call(10))
