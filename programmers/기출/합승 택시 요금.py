# 2021 KAKAO BLIND RECRUITMENT / 합승 택시 요금
# https://school.programmers.co.kr/learn/courses/30/lessons/72413
import heapq
from collections import defaultdict
def solution(n, s, a, b, fares):
    answer = float('INF')
    graph = defaultdict(list)
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])
    for node in graph.keys():
        answer = min(answer, dijkstra(graph, s)[node] + dijkstra(graph, node)[a] + dijkstra(graph, node)[b])
    return answer

def dijkstra(graph, start):
    distance = {node: float('INF') for node in graph}
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        
        if cur_dist > distance[cur_node]:
            continue
        for new_node, new_dist in graph[cur_node]:
            dist = new_dist + cur_dist
            if dist < distance[new_node]:
                distance[new_node] = dist
                heapq.heappush(queue, [dist, new_node])
    return distance

            
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))