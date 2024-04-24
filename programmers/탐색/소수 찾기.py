# 완전탐색 / 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
def solution(numbers):
    answer = 0
    num = set()
    for j in range(len(numbers)):
        for i in permutations(numbers, j+1):
            num.add(int(''.join(i)))
    for i in num:
        if prime(i):
            answer += 1
    return answer

def prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(pow(number,0.5))+1):
        if number % i == 0:
            return False
    return True