from typing import List

"""
Problem: Range Sum Query - Immutable (LeetCode 303)
Topic: Prefix Sum
Approach: Build prefix array where prefix[i+1] = sum(nums[0:i]).
          Then sumRange(l, r) = prefix[r+1] - prefix[l].
Time: O(n) preprocessing, O(1) per query
Space: O(n)
Pitfall: Use prefix length n+1 to make sumRange math clean and avoid off-by-one errors.
"""

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        running = 0
        for x in nums:
            running += x
            self.prefix.append(running)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
