from typing import List

"""
Problem: N-Queens (LeetCode 51)
Topic: Backtracking
Approach: Place one queen per row.
          Track used columns and diagonals:
          - cols[c] for columns
          - diag1[r-c] (use r-c offset by + (n-1)) for main diagonals
          - diag2[r+c] for anti-diagonals
          Backtrack row by row to build valid boards.
Time: Exponential (backtracking)
Space: O(n) for tracking sets + recursion (excluding output)
Pitfall: Diagonal indexing:
         diag1 = r - c + (n - 1), diag2 = r + c.
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # r - c + (n-1)
        diag2 = [False] * (2 * n - 1)  # r + c
        board = [["."] * n for _ in range(n)]

        def dfs(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                d1 = r - c + (n - 1)
                d2 = r + c
                if cols[c] or diag1[d1] or diag2[d2]:
                    continue

                # place queen
                cols[c] = diag1[d1] = diag2[d2] = True
                board[r][c] = "Q"

                dfs(r + 1)

                # backtrack
                board[r][c] = "."
                cols[c] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return res
