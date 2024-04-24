# 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import Counter
def solution(topping):
    answer = 0
    yb = Counter(topping)
    ob = set()
    for val in topping:
        ob.add(val)
        yb[val] -= 1
        if yb[val] == 0:
            yb.pop(val)
        if len(ob) == len(yb):
            answer += 1
    return answer