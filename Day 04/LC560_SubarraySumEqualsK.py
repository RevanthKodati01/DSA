from typing import List

"""
Problem: Subarray Sum Equals K (LeetCode 560)
Topic: Prefix Sum / HashMap
Approach: Use running prefix sum. For each prefix sum `pre`, the number of subarrays ending here with sum k
          equals how many times we've seen (pre - k) before. Store counts of prefix sums in a hashmap.
Time: O(n)
Space: O(n)
Pitfall: Initialize count of prefix sum 0 as 1 (prefix_count[0] = 1), or you’ll miss subarrays starting at index 0.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        pre = 0
        ans = 0

        for x in nums:
            pre += x
            ans += prefix_count.get(pre - k, 0)
            prefix_count[pre] = prefix_count.get(pre, 0) + 1

        return ans
