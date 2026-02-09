from typing import List, Optional
from collections import deque

"""
Problem: Binary Tree Level Order Traversal (LeetCode 102)
Topic: Trees / BFS
Approach: BFS using a queue. Process nodes level by level using the queue size.
Time: O(n)
Space: O(n) for queue in worst case
Pitfall: Capture level size first, then pop exactly that many nodes to form one level.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res
