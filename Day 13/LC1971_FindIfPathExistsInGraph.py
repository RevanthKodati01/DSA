from typing import List

"""
Problem: Find if Path Exists in Graph (LeetCode 1971)
Topic: Union Find (Disjoint Set Union)
Approach: Union all edges. Then check if find(source) == find(destination).
Time: O((n + e) α(n))
Space: O(n)
Pitfall: Graph is 0-indexed here; DSU size should be n.
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
