from typing import List

"""
Problem: Word Search (LeetCode 79)
Topic: Backtracking / DFS Grid
Approach: Try starting from every cell. DFS 4 directions to match the word.
          Mark visited cells temporarily (in-place) to avoid reuse in the same path.
Time: O(m*n*4^L) worst-case where L = len(word)
Space: O(L) recursion depth
Pitfall: Must unmark visited (restore board cell) after DFS, or future paths break.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[i]:
                return False

            # mark visited
            tmp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # unmark
            board[r][c] = tmp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False

