"""
Problem: Longest Common Subsequence (LeetCode 1143)
Topic: Dynamic Programming (2D)
Approach: dp[i][j] = LCS length for text1[:i] and text2[:j].
          If chars match: dp[i][j] = 1 + dp[i-1][j-1]
          Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
Time: O(m*n)
Space: O(m*n)
Pitfall: Use dp with extra row/col (size (m+1)x(n+1)) to avoid bounds checks.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
