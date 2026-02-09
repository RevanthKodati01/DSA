from typing import Optional

"""
Problem: Diameter of Binary Tree (LeetCode 543)
Topic: Trees / DFS
Approach: Compute height of each node. Diameter at a node is height(left) + height(right).
          Track the maximum diameter seen during DFS.
Time: O(n)
Space: O(h) recursion stack
Pitfall: Diameter is counted in EDGES, not nodes. Use left_height + right_height (where heights are in nodes)
         but return heights consistently; common approach returns height in nodes and diameter in edges.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            # diameter through this node (in edges)
            best = max(best, lh + rh)

            # return height (in nodes count from this node downward)
            return 1 + max(lh, rh)

        height(root)
        return best
