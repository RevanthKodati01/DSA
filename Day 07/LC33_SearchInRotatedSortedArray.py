from typing import List

"""
Problem: Search in Rotated Sorted Array (LeetCode 33)
Topic: Binary Search
Approach: Modified binary search.
          At each step, one side (left..mid or mid..right) is sorted.
          Decide which side is sorted, then check if target lies in that side; shrink accordingly.
Time: O(log n)
Space: O(1)
Pitfall: Be careful with range checks using <= and < to avoid missing boundaries.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Left half sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
