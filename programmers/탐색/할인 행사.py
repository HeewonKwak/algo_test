# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter
def solution(want, number, discount):
    answer = 0
    w = {}
    for i, j in zip(want, number):
        w[i] = j
    for i in range(len(discount) -9):
        ww = Counter(discount[i:i+10])
        if w == ww:
            answer += 1
    return answer