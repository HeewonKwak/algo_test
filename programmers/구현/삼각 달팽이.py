# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    tri = [[0 for _ in range(i + 1)] for i in range(n)]
    step = [i for i in range(n, 0, -1)]
    step[0] = n - 1
    ss = 0
    x, y = 0, 0
    for i in range(1, n * (n + 1) // 2 + 1):
        tri[x][y] = i
        if i == n * (n + 1) // 2:
            break
        if ss % 3 == 0:
            x += 1
        elif ss % 3 == 1:
            y += 1
        else:
            x -= 1
            y -= 1
        step[ss] -= 1
        if step[ss] == 0:
            ss += 1 
    for i in tri:
        answer += i
    return answer
