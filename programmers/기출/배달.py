# Summer/Winter Coding(~2018) / 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from collections import defaultdict, deque
def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
    q = deque()
    q.append(1)
    distance = [float('INF') for _ in range(N+1)]
    distance[1] = 0
    while q:
        node = q.popleft()
        for i, j in graph[node]:
            now_distance = distance[i]
            if distance[i] > distance[node] + j:
                distance[i] = distance[node] + j
                q.append(i)
    # print(distance)
    for dist in distance:
        if dist <= K:
            # print(dist)
            answer += 1
    return answer