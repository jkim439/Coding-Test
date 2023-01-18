# 스티커 모으기(2)
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp = [[sticker[0], sticker[0]], [0, sticker[1]]]

    for i in range(2, len(sticker) - 1):
        dp[0].append(max(dp[0][i - 2] + sticker[i], dp[0][i - 1]))

    for i in range(2, len(sticker)):
        dp[1].append(max(dp[1][i - 2] + sticker[i], dp[1][i - 1]))

    return max(dp[0][-1], dp[1][-1])
