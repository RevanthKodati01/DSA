from typing import List

"""
Problem: Permutations (LeetCode 46)
Topic: Backtracking
Approach: Build permutations by choosing each unused element for the next position.
          Use a used[] array to mark elements already in the current path.
Time: O(n * n!)
Space: O(n) recursion + used[] (excluding output)
Pitfall: Don’t forget to backtrack (used[i] = False and path.pop()) after recursion.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def dfs() -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return res

