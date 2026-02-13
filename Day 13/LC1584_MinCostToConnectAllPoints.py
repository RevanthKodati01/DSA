from typing import List
import heapq

"""
Problem: Min Cost to Connect All Points (LeetCode 1584)
Topic: Union Find (Kruskal MST)
Approach: Build all edges with Manhattan distance, sort edges, and run Kruskal using DSU.
          Add edge if it connects two different components until we have (n-1) edges.
Time: O(n^2 log n)
Space: O(n^2)
Pitfall: This builds all edges (O(n^2)). Works for constraints, but be mindful of memory/time.
         Alternative is Prim’s algorithm without storing all edges.
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

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

        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edges.append((w, i, j))

        edges.sort()
        cost = 0
        used = 0

        for w, u, v in edges:
            if union(u, v):
                cost += w
                used += 1
                if used == n - 1:
                    break

        return cost
