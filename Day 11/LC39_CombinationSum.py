from typing import List

"""
Problem: Combination Sum (LeetCode 39)
Topic: Backtracking
Approach: DFS with index i (choose candidates[i] multiple times allowed).
          At each step:
          - take candidates[i] and stay at i (reuse)
          - or skip to i+1
          Stop when target == 0 (valid) or target < 0 (invalid).
Time: Exponential (depends on input; bounded by branching and target)
Space: O(target/min_candidate) recursion depth (excluding output)
Pitfall: Keep combinations in non-decreasing order by using index i to avoid duplicates.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        path = []

        def dfs(i: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            if i == len(candidates) or remain < 0:
                return

            # pruning: if smallest available is already too big
            if candidates[i] > remain:
                return

            # choice 1: take candidates[i]
            path.append(candidates[i])
            dfs(i, remain - candidates[i])  # reuse allowed
            path.pop()

            # choice 2: skip candidates[i]
            dfs(i + 1, remain)

        dfs(0, target)
        return res
