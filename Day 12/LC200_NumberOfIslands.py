from typing import List

"""
Problem: Number of Islands (LeetCode 200)
Topic: Graphs / DFS
Approach: Iterate all cells. When you find '1', start DFS to mark the entire island as visited (flip to '0').
          Count how many times DFS is started.
Time: O(m*n)
Space: O(m*n) worst-case recursion (or O(m*n) visited) depending on grid shape
Pitfall: Mark visited immediately (set to '0') to avoid infinite recursion / double counting.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
