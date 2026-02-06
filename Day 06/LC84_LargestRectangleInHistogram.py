from typing import List

"""
Problem: Largest Rectangle in Histogram (LeetCode 84)
Topic: Monotonic Stack
Approach: Maintain an increasing stack of indices (heights increasing).
          When we see a smaller height, pop bars and compute area where popped height is the limiting height.
          Use a sentinel 0 height at end to flush the stack.
Time: O(n)
Space: O(n)
Pitfall: Width calculation:
         - after popping index j, left boundary is stack[-1] (or -1 if empty)
         - width = i - left_boundary - 1
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices, heights increasing
        best = 0

        for i in range(len(heights) + 1):
            cur = heights[i] if i < len(heights) else 0  # sentinel
            while stack and cur < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, h * width)
            stack.append(i)

        return best
