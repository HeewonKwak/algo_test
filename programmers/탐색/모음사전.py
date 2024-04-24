# 완전탐색 / 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):
    answer = 0
    alp = ['A', 'E', 'I', 'O', 'U']
    case = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += alp.index(word[i]) * case[i]
    answer += len(word)
    return answer