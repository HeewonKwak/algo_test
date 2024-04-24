# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 2진수를 구현하는 함수 보다 bin()이 더 빠르다...
from collections import Counter
import itertools 
def solution(n):
    answer = n
    one = Counter(bin(n))['1']
    while(1):
        answer += 1
        if Counter(bin(answer))['1'] == one:
            return answer

def two(num):
    n2 = ""
    while(1):
        num, a = num//2, num%2
        n2 += str(a)
        if num == 0:
            break
    return n2[::-1]