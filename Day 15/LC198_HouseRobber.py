from typing import List

"""
Problem: House Robber (LeetCode 198)
Topic: Dynamic Programming (1D)
Approach: At each house i, choose:
          - skip: keep best so far
          - rob: nums[i] + best up to i-2
          Use two variables: rob1 (dp[i-2]) and rob2 (dp[i-1]).
Time: O(n)
Space: O(1)
Pitfall: Update order matters: compute new = max(rob2, rob1 + nums[i]) then shift rob1=rob2, rob2=new.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for x in nums:
            new = max(rob2, rob1 + x)
            rob1 = rob2
            rob2 = new
        return rob2
