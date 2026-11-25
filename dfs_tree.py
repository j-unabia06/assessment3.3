from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_level_order_tree(chars):
    if not chars:
        return None

    root = Node(chars[0])
    queue = deque([root])
    i = 1

    while i < len(chars):
        current = queue.popleft()

        if i < len(chars):
            current.left = Node(chars[i])
            queue.append(current.left)
            i += 1

        if i < len(chars):
            current.right = Node(chars[i])
            queue.append(current.right)
            i += 1

    return root


def preorder(node, out):
    if node is None:
        return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)


def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)


def main():
    name = "JEANELLEUNABIA"
    root = build_level_order_tree(list(name))

    pre_order, in_order, post_order = [], [], []
    preorder(root, pre_order)
    inorder(root, in_order)
    postorder(root, post_order)

    print("Preorder  (Root -> Left -> Right):", " -> ".join(pre_order))
    print("Inorder   (Left -> Root -> Right):", " -> ".join(in_order))
    print("Postorder (Left -> Right -> Root):", " -> ".join(post_order))


if __name__ == "__main__":
    main()