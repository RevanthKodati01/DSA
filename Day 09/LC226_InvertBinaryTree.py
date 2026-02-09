from typing import Optional

"""
Problem: Invert Binary Tree (LeetCode 226)
Topic: Trees / DFS
Approach: DFS recursion. For each node, swap left and right subtrees, then recurse.
Time: O(n)
Space: O(h) recursion stack (h = tree height)
Pitfall: Base case must handle None nodes.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
