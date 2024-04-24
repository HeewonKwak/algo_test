# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import Counter, deque
from itertools import combinations

def solution(weights):
    answer = 0
    weight_cnt = Counter(weights)
    case = deque(weight_cnt.keys())
    for w1, cnt in weight_cnt.items():
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2
        if not case:
            break
        case.popleft()
        for w2 in case:
            if partner(w1, w2):
                answer += cnt * weight_cnt[w2]
    return answer

def partner(weight1, weight2):
    ratio = [[1,1],[2,3],[1,2],[3,2],[3,4],[2,1],[4,3]]
    for a, b in ratio:
        if weight1 * a == weight2 * b:
            return True
    return False