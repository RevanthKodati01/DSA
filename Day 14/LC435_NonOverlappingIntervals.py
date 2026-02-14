from typing import List

"""
Problem: Non-overlapping Intervals (LeetCode 435)
Topic: Greedy
Approach: To remove minimum intervals, keep maximum non-overlapping intervals.
          Sort by end time. Greedily pick intervals with earliest end; count removals when overlap occurs.
Time: O(n log n)
Space: O(1) extra (excluding sort)
Pitfall: Sort by END (not start). Earliest finish leaves most room for future intervals.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end

        return removals
