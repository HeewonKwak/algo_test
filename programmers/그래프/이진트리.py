class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

n = [Node(10*i) for i in range(0,9)]

class BinaryTree():
    def __init__(self):
        self.root = None

    # 전위 순회
    def preorder(self, n):
        if n != None:
            print(n.item, '', end='')
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
            print(n.item, '', end='')

    # 중위 순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.item, '', end='')
            if n.right:
                self.inorder(n.right)

    # level 순회
    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
            print(t.item, '', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)
    

tree = BinaryTree()
print(n[1])
tree.root = n[1]
n[1].left = n[2]
n[1].right = n[3]
n[2].left = n[4]
n[2].right = n[5]
n[3].left = n[6]
n[3].right = n[7]
n[4].left = n[8]

tree.preorder(n[1])
print()
tree.postorder(n[1])
print()
tree.inorder(n[1])
print()
tree.levelorder(n[1])