from typing import Optional

"""
Problem: Validate Binary Search Tree (LeetCode 98)
Topic: Trees / DFS
Approach: DFS with bounds. Each node must satisfy (low < node.val < high).
          Left subtree has upper bound = node.val, right subtree has lower bound = node.val.
Time: O(n)
Space: O(h) recursion stack
Pitfall: Use STRICT inequalities (< and >). Duplicates are not allowed in a valid BST in LeetCode 98.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
