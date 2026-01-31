from typing import List

"""
Problem: Maximum Subarray
Topic: Arrays + DP (Kadane’s Algorithm)
Approach: Track best subarray ending at i, and global best.
Time: O(n)
Space: O(1)
Pitfall: Must handle all-negative arrays (initialize with nums[0]).
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0

        for x in nums:
            cur = max(x, cur + x)
            best = max(best, cur)

        return best
