# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter
def solution(k, tangerine):
    answer = 0
    cc = Counter(tangerine)
    cc = sorted(cc.items(), key=lambda x: x[1], reverse=True)
    for _, c in cc:
        k -= c
        answer += 1
        if k <= 0:
            break
    return answer