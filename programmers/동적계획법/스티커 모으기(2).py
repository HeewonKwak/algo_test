# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    dp1 = [0 for _ in sticker]
    dp2 = [0 for _ in sticker]
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    return max(max(dp1), max(dp2))

# 복습

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)
    dp1 = [0] * (len(sticker))
    dp2 = [0] * (len(sticker))
    arr1 = sticker[:-1]
    arr2 = sticker[1:]
    dp1[1], dp2[1] = arr1[0], arr2[0]
    dp1[2], dp2[2] = max(arr1[0:2]), max(arr2[0:2])
    for i in range(3, len(sticker)):
        dp1[i] = max(dp1[i-2] + arr1[i-1], dp1[i-1])
        dp2[i] = max(dp2[i-2] + arr2[i-1], dp2[i-1])
    return max(dp1[-1], dp2[-1])