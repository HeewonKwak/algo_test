# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(now, visited, nodes):
    visited[now] = True
    for i in range(len(nodes[now])):
        if visited[i] == False and nodes[now][i] == 1:
            dfs(i, visited, nodes)
            
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, computers)
            answer += 1
    return answer