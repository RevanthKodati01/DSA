from typing import List
from collections import deque

"""
Problem: Rotting Oranges (LeetCode 994)
Topic: Graphs / BFS
Approach: Multi-source BFS starting from all rotten oranges (value 2).
          Each minute, rot adjacent fresh oranges (value 1).
          Track minutes by BFS levels. If any fresh remain, return -1.
Time: O(m*n)
Space: O(m*n) for queue in worst case
Pitfall: Initialize queue with ALL rotten oranges first; minutes should count BFS layers, not each pop.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
