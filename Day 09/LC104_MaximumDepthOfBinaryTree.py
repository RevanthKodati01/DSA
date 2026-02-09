from typing import Optional

"""
Problem: Maximum Depth of Binary Tree (LeetCode 104)
Topic: Trees / DFS
Approach: Depth of a node = 1 + max(depth(left), depth(right)).
Time: O(n)
Space: O(h) recursion stack
Pitfall: Return 0 for None to make depth math correct.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
