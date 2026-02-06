from typing import List

"""
Problem: Next Greater Element I (LeetCode 496)
Topic: Monotonic Stack
Approach: Compute next greater for each number in nums2 using a monotonic decreasing stack.
          Pop smaller elements when a bigger element arrives; map popped -> current as next greater.
          Then answer queries for nums1 using the map.
Time: O(n + m)
Space: O(n)
Pitfall: nums1 is a subset of nums2. Use values as keys (nums2 has distinct values in this problem).
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []  # decreasing values

        for x in nums2:
            while stack and x > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = x
            stack.append(x)

        return [next_greater.get(x, -1) for x in nums1]
