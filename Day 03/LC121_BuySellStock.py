from typing import List

"""
Problem: Best Time to Buy and Sell Stock (LeetCode 121)
Topic: Sliding Window / Arrays
Approach: Track minimum price so far; update best profit each day.
Time: O(n)
Space: O(1)
Pitfall: Always update min_price before computing profit for future days.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0

        for p in prices:
            min_price = min(min_price, p)
            best = max(best, p - min_price)

        return best
