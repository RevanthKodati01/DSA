"""
Problem: Unique Paths (LeetCode 62)
Topic: Dynamic Programming (2D)
Approach: dp[r][c] = number of ways to reach cell (r,c).
          dp[r][c] = dp[r-1][c] + dp[r][c-1].
          Optimize to 1D dp over columns.
Time: O(m*n)
Space: O(n)
Pitfall: Initialize dp with 1s for first row (only one way moving right).
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[-1]
