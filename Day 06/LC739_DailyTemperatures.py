from typing import List

"""
Problem: Daily Temperatures (LeetCode 739)
Topic: Monotonic Stack
Approach: Maintain a monotonic decreasing stack of indices (temps decreasing).
          When current temp is greater than temp at stack top, we found the next warmer day for that index.
Time: O(n)
Space: O(n)
Pitfall: Stack stores INDICES (not temperatures) so we can compute days difference.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # indices, temperatures[stack] is decreasing

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans
