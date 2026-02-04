from typing import List

"""
Problem: Find Pivot Index (LeetCode 724)
Topic: Prefix Sum
Approach: Total sum is known. Scan left to right with left_sum.
          At index i, right_sum = total - left_sum - nums[i].
          If left_sum == right_sum, i is the pivot.
Time: O(n)
Space: O(1)
Pitfall: Update left_sum AFTER checking pivot condition at i.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            right_sum = total - left_sum - x
            if left_sum == right_sum:
                return i
            left_sum += x

        return -1
