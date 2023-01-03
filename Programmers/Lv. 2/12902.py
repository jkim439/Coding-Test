# 3 x n 타일링
def solution(n):
    dp = [0, 3, 11]
    idx = n // 2

    for i in range(3, idx + 1):
        dp.append(dp[i - 1] * 3 + sum(dp[1 : i - 1] * 2) + 2)

    return dp[idx] % 1000000007
