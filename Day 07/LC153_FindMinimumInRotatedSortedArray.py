from typing import List

"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode 153)
Topic: Binary Search
Approach: Use binary search by comparing mid with right.
          If nums[mid] > nums[r], min is in right half; else min is in left half (including mid).
Time: O(log n)
Space: O(1)
Pitfall: This assumes no duplicates. Use while l < r and return nums[l] at end.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
