# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# puddles의 x,y 값이 반대다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def solution(m, n, puddles):
    graph = [[0 for _ in range(n+1)] for _ in range(m+1)]
    graph[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j < n and [i, j+1] not in puddles:
                graph[i][j+1] += graph[i][j]
            if i < m and [i+1, j] not in puddles:
                graph[i+1][j] += graph[i][j]
    print(graph)
    return graph[-1][-1] % 1000000007

# 복습

def solution(m, n, puddles):
    graph = [[0 for _ in range(m+1)]for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j != m and [j+1, i] not in puddles:
                graph[i][j+1] += graph[i][j]
            if i != n and [j, i+1] not in puddles:
                graph[i+1][j] += graph[i][j]
    return graph[n][m] % 1000000007

def p(g):
    for i in g:
        print(i)
    print('---------------')