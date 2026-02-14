"""
Problem: Climbing Stairs (LeetCode 70)
Topic: Dynamic Programming (1D)
Approach: dp[i] = dp[i-1] + dp[i-2]. Use two variables to keep O(1) space.
Time: O(n)
Space: O(1)
Pitfall: Base cases: n <= 2 should return n.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # dp[1], dp[2]
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
