# 깊이/너비 우선 탐색(DFS/BFS) / 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    maps[-1][-1] = -1
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = True
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx == len(maps) and yy == len(maps[0]):
                return maps[x][y] + 1
            if xx >= 0 and xx < len(maps) and yy >= 0 and yy < len(maps[0]) and visited[xx][yy] == False and maps[xx][yy] != 0:
                visited[xx][yy] = True
                maps[xx][yy] = maps[x][y] + 1
                q.append([xx, yy])
    return maps[-1][-1]