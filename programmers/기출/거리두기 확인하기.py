# 2021 카카오 채용연계형 인턴십 / 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from itertools import combinations
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

def check(place):
    palyers = []
    partitions = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                palyers.append([i, j])
            elif place[i][j] == 'X':
                partitions.append([i, j])
    if palyers == []:
        return 1
    for p1, p2 in combinations(palyers, 2):
        if p1[0] == p2[0] and abs(p1[1] - p2[1]) == 1:
            return 0
        elif p1[1] == p2[1] and abs(p1[0] - p2[0]) == 1:
            return 0
        elif abs(p1[1] - p2[1]) == 1 and abs(p1[0] - p2[0]) == 1:
            if place[p1[0]][p2[1]] == 'O' or place[p2[0]][p1[1]] == 'O':
                return 0
        elif p1[0] == p2[0] and abs(p1[1] - p2[1]) == 2 and place[p1[0]][(p1[1] + p2[1])//2] == 'O':
            return 0
        elif p1[1] == p2[1] and abs(p1[0] - p2[0]) == 2 and place[(p1[0] + p2[0])//2][p1[1]] == 'O':
            return 0
    return 1
        