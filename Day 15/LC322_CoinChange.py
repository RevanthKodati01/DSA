from typing import List

"""
Problem: Coin Change (LeetCode 322)
Topic: Dynamic Programming (1D)
Approach: dp[a] = min coins to make amount a.
          Initialize dp[0]=0, others = inf. For each amount, try each coin.
Time: O(amount * number_of_coins)
Space: O(amount)
Pitfall: Use a large sentinel (amount+1) or inf; return -1 if dp[amount] not reachable.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != INF else -1
