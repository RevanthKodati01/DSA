from typing import List

"""
Problem: Merge Intervals (LeetCode 56)
Topic: Greedy / Sorting
Approach: Sort intervals by start. Keep a current interval and merge overlaps by extending end.
Time: O(n log n)
Space: O(n) for output (or O(1) extra if modify in-place)
Pitfall: Always sort first; merging without sorting fails.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
