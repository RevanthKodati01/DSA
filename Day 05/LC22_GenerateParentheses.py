from typing import List

"""
Problem: Generate Parentheses (LeetCode 22)
Topic: Stack / Backtracking
Approach: Backtracking with counts:
          - We can add '(' if open_count < n
          - We can add ')' if close_count < open_count
          Build valid strings of length 2n.
Time: O(4^n / sqrt(n)) (Catalan number growth)
Space: O(n) recursion depth + output
Pitfall: Never allow close_count to exceed open_count (would make invalid prefix).
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: str, open_count: int, close_count: int) -> None:
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_count < n:
                backtrack(cur + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
