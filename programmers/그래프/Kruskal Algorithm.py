def get_parent(parent, node):
    if parent[node] != node:
        return get_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, node1, node2):
    a = get_parent(parent, node1)
    b = get_parent(parent, node2)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())

parent = [i for i in range(v+1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input.split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if get_parent(parent, a) != get_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost)