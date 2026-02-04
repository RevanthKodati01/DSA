from typing import List

"""
Problem: Product of Array Except Self (LeetCode 238)
Topic: Prefix/Suffix Product (Prefix Sum pattern variant)
Approach: Build output with prefix products in first pass.
          Then multiply by suffix products in second pass (right to left).
          No division, O(1) extra space besides output.
Time: O(n)
Space: O(1) extra (excluding output)
Pitfall: Ensure you set output[i] to prefix BEFORE updating prefix with nums[i], and same idea for suffix pass.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
