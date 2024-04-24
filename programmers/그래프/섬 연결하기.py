# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def get_parent(parent, x):
    if parent[x] != x:
        return get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a < b: parent[b] = a
    else: parent[a] = b

def find_parent(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a!=b: return 1
    else: return 0

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n+1)]
    costs.sort(key=lambda x: (x[2]))
    for edge in costs:
        if find_parent(parent, edge[0], edge[1]):
            union_parent(parent, edge[0], edge[1])
            answer += edge[2]
    return answer