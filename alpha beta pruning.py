class TreeNode:
    def __init__(self, value=None, children=None):
        self.value = value            # Used only for leaf nodes
        self.children = children or []  # List of child TreeNode objects

# Evaluation function: Returns the value of a leaf node
def evaluate(node):
    return node.value

# Game over function: True if it's a leaf node
def game_over(node):
    return len(node.children) == 0

# Generate child nodes
def get_possible_moves(node):
    return node.children

# Create new game state: For tree traversal, return the child node directly
def make_move(state, move, player):
    return move

# Alpha-Beta Pruning implementation
def alpha_beta_pruning(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over(node):
        return evaluate(node)

    if maximizingPlayer:
        max_eval = float('-inf')
        for child in get_possible_moves(node):
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for child in get_possible_moves(node):
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
# Constructing the tree like your example
root = TreeNode()
root.left = TreeNode(3)
root.right = TreeNode()
root.right.left = TreeNode()
root.right.right = TreeNode()
root.right.left.left = TreeNode(-3)
root.right.right.right = TreeNode(4)

# Convert to a list-based child format
root.children = [root.left, root.right]
root.right.children = [root.right.left, root.right.right]
root.right.left.children = [root.right.left.left]
root.right.right.children = [root.right.right.right]

# Run the Alpha-Beta pruning algorithm
best_value = alpha_beta_pruning(root, depth=4, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
print("Best value:", best_value)


