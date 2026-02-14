from typing import List

"""
Problem: Jump Game (LeetCode 55)
Topic: Greedy
Approach: Track the farthest index reachable so far (max_reach).
          Iterate i from 0..n-1; if i > max_reach, we are stuck -> False.
          Update max_reach = max(max_reach, i + nums[i]).
Time: O(n)
Space: O(1)
Pitfall: Early failure check (i > max_reach) is key; don’t try DFS/DP (too slow).
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)

        return True
