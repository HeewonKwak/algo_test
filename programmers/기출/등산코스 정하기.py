# 2022 KAKAO TECH INTERNSHIP / 등산코스 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = []
    nodes = defaultdict(dict)
    summits.sort()
    summit_s = set(summits)
    for path in paths:
        nodes[path[0]][path[1]] = path[2]
        nodes[path[1]][path[0]] = path[2]
    return dijkstra(nodes, gates, summits, summit_s)

def dijkstra(graph, gates, summits, summit_s):
    distances = {node: float('inf') for node in graph}
    queue = []
    for gate in gates:
        heapq.heappush(queue, [0, gate])
        distances[gate] = 0

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance or current_destination in summit_s:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = max(current_distance, new_distance)
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
        
    ans = [0, float('inf')]
    for summit in summits:
        if distances[summit] < ans[1]:
            ans[0] = summit
            ans[1] = distances[summit]

    return ans