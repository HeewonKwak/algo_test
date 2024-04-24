# 스택/큐 / 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge_weight = 0
    now_bridge = deque()
    while q:
        if len(now_bridge) > 0:
            if now_bridge[0][1] == 1:
                truck, _ = now_bridge.popleft()
                bridge_weight -= truck
            for i in range(len(now_bridge)):
                now_bridge[i][1] -= 1
        if len(q) == 0:
            pass
        elif bridge_weight + q[0] <= weight:
            truck = q.popleft()
            now_bridge.append([truck, bridge_length])
            bridge_weight += truck
        answer += 1
            
    return answer + bridge_length