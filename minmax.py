class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Minimax function
def minimax(node, is_maximizing):
    # If node is a leaf, return its value
    if node.left is None and node.right is None:
        return node.val

    if is_maximizing:
        best = float('-inf')
        if node.left:
            best = max(best, minimax(node.left, False))
        if node.right:
            best = max(best, minimax(node.right, False))
        return best
    else:
        best = float('inf')
        if node.left:
            best = min(best, minimax(node.left, True))
        if node.right:
            best = min(best, minimax(node.right, True))
        return best

# Build the tree from your image
root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)

root.right.left = TreeNode(0)
root.right.right = TreeNode(0)

root.right.left.left = TreeNode(-3)
root.right.right.right = TreeNode(4)

# Print result
print("Minimax Value at Root:", minimax(root, True))
