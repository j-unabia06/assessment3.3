class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):

        self.root = Node("U")

        self.root.left = Node("N")
        self.root.right = Node("A1")

        self.root.left.left = Node("B")
        self.root.left.right = Node("I")

        self.root.right.left = Node("A2")



    def bfs(self):
        if self.root is None:
            return

        queue = [self.root]

        print("BFS Traversal:")
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print()



    def dfs(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.dfs(node.left)
        self.dfs(node.right)



tree = BinaryTree()

tree.bfs()

print("DFS Traversal:")
tree.dfs(tree.root)
print()
