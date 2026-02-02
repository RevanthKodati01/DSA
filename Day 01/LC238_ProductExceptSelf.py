from typing import List

"""
Problem: Product of Array Except Self
Topic: Arrays + Prefix/Suffix
Approach:
  - First pass: res[i] = product of all nums before i (prefix)
  - Second pass: multiply by product of all nums after i (suffix)
Time: O(n)
Space: O(1) extra (excluding output array)
Pitfall: Do NOT use division; handle zeros naturally with prefix/suffix.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
