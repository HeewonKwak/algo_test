def get_parent(parent, child):
    if parent[child] == child:
        return parent[child]
    return get_parent(parent, parent[child])

def union_parent(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a < b: parent[b] = a
    else: parent[a] = b

def find_parent(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a==b: return 1
    else: return 0

parent = [i for i in range(0, 11)]
union_parent(parent, 1, 2)
union_parent(parent, 2, 3)
union_parent(parent, 3, 4)
union_parent(parent, 4, 5)
union_parent(parent, 6, 7)
union_parent(parent, 7, 8)
union_parent(parent, 8, 9)
# print(find_parent(parent, 1, 5))
# print(get_parent(parent, 3))

# 부모 노드를 찾아주는 함수
def getparent(parent, node):
    if parent[node] != node:
        return get_parent(parent, parent[node])
    return parent[node]

def unnionfind(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = [i for i in range(0, 11)]
unnionfind(parent, 1, 2)
unnionfind(parent, 2, 3)
unnionfind(parent, 3, 4)
unnionfind(parent, 4, 5)
unnionfind(parent, 6, 7)
unnionfind(parent, 7, 8)
unnionfind(parent, 8, 9)
for i in range(1, 9):
    print(getparent(parent, i))