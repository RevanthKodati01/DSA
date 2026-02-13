from typing import List

"""
Problem: Redundant Connection (LeetCode 684)
Topic: Union Find (Disjoint Set Union)
Approach: Use DSU. For each edge (u, v), if find(u) == find(v), adding it forms a cycle -> redundant edge.
          Otherwise union(u, v).
Time: O(n α(n))
Space: O(n)
Pitfall: Nodes are 1-indexed. DSU size should be n+1.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
