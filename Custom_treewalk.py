class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def walk_tree(node, depth=0):
    print("  " * depth + node.value)
    for child in node.children:
        walk_tree(child, depth + 1)

# Create tree
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
grand1 = TreeNode("Grandchild 1")
grand2 = TreeNode("Grandchild 2")
grand3 = TreeNode("Grandchild 3")

child1.add_child(grand1)
child1.add_child(grand2)
child2.add_child(grand3)
root.add_child(child1)
root.add_child(child2)
# Walk tree
walk_tree(root)
