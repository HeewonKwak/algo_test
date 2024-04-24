# https://school.programmers.co.kr/learn/courses/30/lessons/12907
def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    for coin in sorted(money):
        for i in range(coin, n+1):
            dp[i] = (dp[i] + dp[i-coin]) % 1000000007
    return dp[n]

# 복습
def solution(n, money):
    dp = [0 for _ in range(n+1)]
    for m in sorted(money):
        dp[m] += 1
        j = 1
        while j+m < n+1:
            dp[j+m] = (dp[j+m] + dp[j])% 1000000007
            j+=1
    return dp[n] % 1000000007