# https://school.programmers.co.kr/learn/courses/30/lessons/86971#
from collections import defaultdict
import copy
def solution(n, wires):
    answer = n - 2
    node = defaultdict(int)
    connect = defaultdict(list)
    for i, j in wires:
        connect[i].append(j)
        connect[j].append(i)
        node[i] += 1
        node[j] += 1
    for i, j in wires:
        if node[i] > 1 and node[j] > 1:
            # print(i, j, connect)
            connect_copy = copy.deepcopy(connect)
            connect_copy[i].remove(j)
            connect_copy[j].remove(i)
            visited = [False for _ in range(n+1)]
            dfs(connect_copy, visited, 1)
            # print(answer, connect_copy, visited)
            answer = min(answer, abs(n-visited.count(True) - visited.count(True)))
    return answer

def dfs(nodes, visited, now):
    visited[now] = True
    for node in nodes[now]:
        if not visited[node]:
            dfs(nodes, visited, node)