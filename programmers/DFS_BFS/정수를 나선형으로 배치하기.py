# 코딩 기초 트레이닝 / 정수를 나선형으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181832
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    answer = dfs(answer, 0, 0, 2, 0)
    return answer

def dfs(array, x, y, value, direction):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        xx = x + dx[(i+direction)%4]
        yy = y + dy[(i+direction)%4]
        if xx >= len(array) or xx < 0 or yy >= len(array) or yy < 0:
            continue
        elif array[xx][yy] != 0:
            continue
        array[xx][yy] = value
        return dfs(array, xx, yy, value + 1, (i+direction)%4)
    return array