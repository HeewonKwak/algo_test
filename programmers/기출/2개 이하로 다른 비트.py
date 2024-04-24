# 월간 코드 챌린지 시즌2 / 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885
from collections import defaultdict
def solution(numbers):
    answer = []
    bit = defaultdict(int)
    for number in numbers:
        a = 0
        for num in bin(number)[::-1]:
            if num == '0' or num == 'b':
                break
            a += 1
        if a == 0:
            answer.append(number + 1)
        else:
            answer.append(number + pow(2,a-1))
    return answer