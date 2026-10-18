# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf") 
        def dfs(node):
            if node is None:
                return 0
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            sum_through_node = node.val + left_gain + right_gain
            self.best = max(sum_through_node, self.best)

            return node.val + max(left_gain, right_gain)
        dfs(root)
        return self.best