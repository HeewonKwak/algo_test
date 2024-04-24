# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n for _ in range(n)]
    for i in range(s%n):
        answer[-(i+1)] +=1
    return answer

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    if n == 1:
        return [s]
    return [s//n]*(n-s%n) , [s//n + 1] * (s%n)