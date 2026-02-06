from typing import List

"""
Problem: Next Greater Element II (LeetCode 503)
Topic: Monotonic Stack
Approach: Circular array. Iterate twice (0..2n-1) using i % n.
          Maintain a decreasing stack of indices whose next greater isn't found yet.
          Only push indices during the first pass (i < n).
Time: O(n)
Space: O(n)
Pitfall: Don't push during the second pass, or you'll duplicate indices and break logic.
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []  # indices, nums[stack] decreasing

        for i in range(2 * n):
            cur = nums[i % n]
            while stack and cur > nums[stack[-1]]:
                j = stack.pop()
                ans[j] = cur
            if i < n:
                stack.append(i)

        return ans

