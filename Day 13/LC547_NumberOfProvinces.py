from typing import List

"""
Problem: Number of Provinces (LeetCode 547)
Topic: Union Find (Disjoint Set Union)
Approach: Union i and j when isConnected[i][j] == 1. Count number of unique roots at end.
Time: O(n^2 α(n))
Space: O(n)
Pitfall: Only loop j > i to avoid double work, but either way works.
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

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

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        roots = set(find(i) for i in range(n))
        return len(roots)
