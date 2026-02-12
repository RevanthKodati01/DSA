from typing import List

"""
Problem: Pacific Atlantic Water Flow (LeetCode 417)
Topic: Graphs / DFS
Approach: Reverse thinking: instead of flowing from each cell to oceans, do DFS/BFS FROM the oceans inward.
          A cell can reach an ocean if there's a non-decreasing path from the ocean to the cell (reverse edges).
          Run DFS from:
          - Pacific border (top row + left col)
          - Atlantic border (bottom row + right col)
          Answer = intersection of reachable sets.
Time: O(m*n)
Space: O(m*n)
Pitfall: In reverse DFS, you can move from (r,c) to (nr,nc) only if heights[nr][nc] >= heights[r][c].
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int, visited: List[List[bool]]) -> None:
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        # Pacific: top row + left col
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)

        # Atlantic: bottom row + right col
        for c in range(n):
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, n - 1, atl)

        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res
