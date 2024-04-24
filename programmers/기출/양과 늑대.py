# 2022 KAKAO BLIND RECRUITMENT / 양과 늑대
# https://school.programmers.co.kr/learn/courses/30/lessons/92343#

# 풀이 참고
def solution(info, edges):
    answer = []
    
    visited = [False for _ in range(len(info))]
    visited[0] = True
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = False
                
    dfs(1, 0)
    return max(answer)

# fail idea
from collections import deque

class Node():
    def __init__(self, node):
        self.parent_node = node
        self.sheep = []
        self.wolf = []
        self.left = None
        self.right = None
        self.point = -17
        self.visited = False
    def edge(self, node):
        if self.left == None:
            self.left = node
        elif self.left > node:
            self.node = node
        else:
            self.right = node

def solution(info, edges):
    answer = 0
    cnt = 0
    nodes = [Node(i) for i in range(len(info))]
    for parent_node, child_node in edges:
        nodes[parent_node].edge(child_node)
    nodes[0].sheep = [0]
    nodes[0].point = 1
    dfs(nodes, 0, info)
    # for node in nodes:
    #     print(node.parent_node, node.sheep, node.wolf, node.point)
    sheep_node = deque([i for i in range(len(info)) if info[i] == 0])
    my_sheep = set()
    wolf_node = set()
    while sheep_node:
        node1 = sheep_node.popleft()
        cnt = len(my_sheep) - len(wolf_node)
        print(node1, answer, cnt, sheep_node, wolf_node, nodes[node1].point)
        if nodes[node1].point > 0:
            my_sheep.add(node1)
            for wolf in nodes[node1].wolf:
                wolf_node.add(wolf)
            for nn in sheep_node:
                nodes[nn].visited = False
            continue
        temp_wolf = wolf_node.copy()
        for wolf in nodes[node1].wolf:
            temp_wolf.add(wolf)
        if len(my_sheep) > len(temp_wolf):
            wolf_node = temp_wolf
            my_sheep.add(node1)
            for nn in sheep_node:
                nodes[nn].visited = False
        elif nodes[node1].visited == False:
            nodes[node1].visited = True
            sheep_node.append(node1)
        else:
            print(node1, nodes[node1].visited)
            break
    print(my_sheep, wolf_node)
    return len(my_sheep)

def dfs(nodes, start, info):
    if nodes[start].right != None:
        if info[nodes[start].right] == 0:
            nodes[nodes[start].right].sheep = nodes[start].sheep + [nodes[start].right]
            nodes[nodes[start].right].wolf = nodes[start].wolf
            nodes[nodes[start].right].point = nodes[start].point
        else:
            nodes[nodes[start].right].sheep = nodes[start].sheep
            nodes[nodes[start].right].wolf = nodes[start].wolf + [nodes[start].right]
            nodes[nodes[start].right].point = min(nodes[start].point, len(nodes[nodes[start].right].sheep) - len(nodes[nodes[start].right].wolf))
        dfs(nodes, nodes[start].right, info)
    if nodes[start].left != None:
        if info[nodes[start].left] == 0:
            nodes[nodes[start].left].sheep = nodes[start].sheep + [nodes[start].left]
            nodes[nodes[start].left].wolf = nodes[start].wolf
            nodes[nodes[start].left].point = nodes[start].point
        else:
            nodes[nodes[start].left].sheep = nodes[start].sheep
            nodes[nodes[start].left].wolf = nodes[start].wolf + [nodes[start].left]
            nodes[nodes[start].left].point = min(nodes[start].point, len(nodes[nodes[start].left].sheep) - len(nodes[nodes[start].left].wolf))
        dfs(nodes, nodes[start].left, info)
        
