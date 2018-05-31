class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse(root):
    current_node = root
    stack = []
    i = 0

    while (not i):
        if current_node is not None:
            stack.append(current_node)
            current_node = current_node.left
        else:
            if (len(stack) > 0):
                current_node = stack.pop()
                print(current_node.value),
                current_node = current_node.right
            else:
                i = 1

""" Sample binary tree:
            6
          /   \
         5     8
       /  \
      2    3        """

root = Node(6)
root.left = Node(5)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(3)

traverse(root)