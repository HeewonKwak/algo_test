# 2019 KAKAO BLIND RECRUITMENT / 그래프 / 길 찾기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/42892
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item, x, y):
        self.item = item
        self.left = None
        self.right = None
        self.x = x
        self.y = y
        self.min_x = -float('INF')
        self.max_x = float('INF')

class BinaryTree():
    def __init__(self):
        self.root = None
        self.preorder_list = []
        self.postorder_list = []

    # 전위 순회
    def preorder(self, n):
        if n != None:
            self.preorder_list.append(n.item)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 후위 순회
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.postorder_list.append(n.item)

def solution(nodeinfo):
    answer = []
    nodes = []
    level = defaultdict(list)
    for i, [x, y] in enumerate(nodeinfo):
        nodes.append(Node(i + 1, x, y))
        level[y].append(i+1)
    node_sort = sorted(nodes, key = lambda x: -x.y)
    high = sorted(level.keys(), reverse=True)
    tree = BinaryTree()
    tree.root = node_sort[0]
    idx = 0
    while idx < len(high) - 1:
        for i in level[high[idx]]:
            for j in level[high[idx+1]]:
                if nodes[i-1].left == None and nodes[i-1].x > nodes[j-1].x and nodes[i-1].min_x < nodes[j-1].x < nodes[i-1].max_x:
                    nodes[i-1].left = nodes[j-1]
                    nodes[j-1].max_x = nodes[i-1].x
                    nodes[j-1].min_x = nodes[i-1].min_x
                elif nodes[i-1].right == None and nodes[i-1].x < nodes[j-1].x and nodes[i-1].min_x < nodes[j-1].x < nodes[i-1].max_x:
                    nodes[i-1].right = nodes[j-1]
                    nodes[j-1].min_x = nodes[i-1].x
                    nodes[j-1].max_x = nodes[i-1].max_x
        idx += 1
    tree.preorder(tree.root)
    tree.postorder(tree.root)
    answer.append(tree.preorder_list)
    answer.append(tree.postorder_list)
        
    return answer

# chatGPT 풀이
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item, x, y):
        self.item = item
        self.left = None
        self.right = None
        self.x = x
        self.y = y

# tree 생성
def construct_tree(nodes):
    root = nodes[0]
    for i in range(1, len(nodes)):
        current = root
        while True:
            if nodes[i].x < current.x:
                if current.left is None:
                    current.left = nodes[i]
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = nodes[i]
                    break
                current = current.right
    return root

def preorder_traversal(node, result):
    if node:
        result.append(node.item)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.item)

def solution(nodeinfo):
    answer = []
    nodes = [Node(i + 1, x, y) for i, [x, y] in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x.y, x.x))  # 노드를 y 기준으로 내림차순, x 기준으로 오름차순 정렬

    tree_root = construct_tree(nodes)
    for i in nodes:
        print(i.item, i.left, i.right)
    preorder_result = []
    postorder_result = []

    preorder_traversal(tree_root, preorder_result)
    postorder_traversal(tree_root, postorder_result)

    answer.append(preorder_result)
    answer.append(postorder_result)

    return answer