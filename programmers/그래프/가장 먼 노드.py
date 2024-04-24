# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque, defaultdict

def solution(n, edge):
    nodes = defaultdict(list)
    for vertex in edge:
        nodes[vertex[0]].append(vertex[1])
        nodes[vertex[1]].append(vertex[0])
    # print(nodes)
    queue = deque()
    visted = [0 for _ in range(n + 1)]
    queue.append(1)
    while(len(queue)):
        now = queue.popleft()
        for i in nodes[now]:
            if visted[i] == 0 and i !=1:
                visted[i] = visted[now] + 1 
                queue.append(i)
    # print(visted)
    return visted.count(max(visted))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))