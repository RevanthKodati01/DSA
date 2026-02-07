from typing import List

"""
Problem: Binary Search (LeetCode 704)
Topic: Binary Search
Approach: Standard binary search on sorted array. Keep l..r inclusive, mid, shrink based on comparison.
Time: O(log n)
Space: O(1)
Pitfall: Use while l <= r for inclusive boundaries; update l = mid+1 or r = mid-1 to avoid infinite loop.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
