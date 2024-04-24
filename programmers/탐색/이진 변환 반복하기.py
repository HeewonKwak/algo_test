# https://school.programmers.co.kr/learn/courses/30/lessons/70129
from collections import Counter
def solution(s):
    answer = []
    zero = 0
    cnt = 0
    while(1):
        cc = Counter(s)
        if s == "1":
            break
        zero += cc['0']
        s = two(cc['1'])
        cnt += 1
    return [cnt, zero]

def two(n):
    num = ""
    while(1):
        n, a = n // 2, n % 2
        num += str(a)
        if n == 0:
            break
    return num[::-1]