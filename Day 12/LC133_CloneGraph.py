from typing import Optional

"""
Problem: Clone Graph (LeetCode 133)
Topic: Graphs / DFS
Approach: Use DFS with a hashmap (old_node -> new_node) to avoid cloning a node multiple times.
          For each node, clone it once, then recursively clone its neighbors.
Time: O(V + E)
Space: O(V) for hashmap + recursion stack
Pitfall: Always check if node already cloned before exploring neighbors to prevent infinite cycles.
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        clones = {}

        def dfs(cur: "Node") -> "Node":
            if cur in clones:
                return clones[cur]

            copy = Node(cur.val)
            clones[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
