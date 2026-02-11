from typing import List

"""
Problem: Subsets (LeetCode 78)
Topic: Backtracking
Approach: DFS decision at each index: include nums[i] or skip it. Add a copy of path to results.
Time: O(n * 2^n)
Space: O(n) recursion depth (excluding output)
Pitfall: Append a COPY of the current path (path[:]) to results, not the path reference.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(path[:])
                return

            # choice 1: skip nums[i]
            dfs(i + 1)

            # choice 2: take nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return res
