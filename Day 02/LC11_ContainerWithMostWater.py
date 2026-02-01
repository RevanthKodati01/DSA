from typing import List

"""
Problem: Container With Most Water (LeetCode 11)
Topic: Two Pointers / Arrays
Approach: Start with widest container (l=0, r=n-1). Compute area, then move the pointer
          with the smaller height inward (only chance to increase limiting height).
Time: O(n)
Space: O(1)
Pitfall: Always move the smaller height pointer; moving the taller one cannot increase area if width shrinks.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best
