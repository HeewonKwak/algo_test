# https://school.programmers.co.kr/learn/courses/30/lessons/159993#
from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    x, y = 0, 0
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                x, y = i, j
            elif maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
    distance = [[float('INF') for _ in range(len(maps[0]))] for _ in range(len(maps))]
    distance[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < len(maps) and 0 <= yy < len(maps[0]) and maps[xx][yy] != 'X':
                if distance[x][y] + 1 < distance[xx][yy]:
                    distance[xx][yy] = distance[x][y] + 1
                    q.append([xx, yy])
    
    if distance[sx][sy] == float('INF') or distance[ex][ey] == float('INF'):
        return -1
    answer += distance[sx][sy] + distance[ex][ey]
    return answer