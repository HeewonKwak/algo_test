# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict
def solution(clothes):
    answer = 1
    c = defaultdict(list)
    for a, b in clothes:
        c[b].append(a)
    for a in c:
        answer *= (len(c[a]) + 1)
    return answer - 1