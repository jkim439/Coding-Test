# 선입 선출 스케줄링
def solution(n, cores):
    if n < len(cores):
        return n

    else:
        n -= len(cores)
        left = 1
        right = max(cores) * n

        while left < right:
            mid = (left + right) // 2
            completed = 0

            for core in cores:
                completed += mid // core

            if completed < n:
                left = mid + 1
            else:
                right = mid

        for core in cores:
            n -= (right - 1) // core

        for i in range(len(cores)):
            if right % cores[i] == 0:
                n -= 1
                if n == 0:
                    return i + 1
