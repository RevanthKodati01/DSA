from typing import List

"""
Problem: Contiguous Array (LeetCode 525)
Topic: Prefix Sum / HashMap
Approach: Convert 0 -> -1 and 1 -> +1. Then the problem becomes finding the longest subarray with sum 0.
          Track earliest index where each prefix sum occurs. If prefix sum repeats, subarray between them sums to 0.
Time: O(n)
Space: O(n)
Pitfall: Store the FIRST time a prefix sum appears (don’t overwrite), because that gives the longest length.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}  # prefix sum -> earliest index
        pre = 0
        best = 0

        for i, x in enumerate(nums):
            pre += 1 if x == 1 else -1

            if pre in first_index:
                best = max(best, i - first_index[pre])
            else:
                first_index[pre] = i  # store earliest occurrence

        return best
