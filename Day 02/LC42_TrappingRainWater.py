from typing import List

"""
Problem: Trapping Rain Water (LeetCode 42)
Topic: Two Pointers / Arrays
Approach: Two pointers with left_max and right_max.
          - If height[l] < height[r], water on left depends on left_max.
          - Else, water on right depends on right_max.
          Add trapped water as (max_so_far - current_height) when current is below its side max.
Time: O(n)
Space: O(1)
Pitfall: Update left_max/right_max BEFORE adding water for that side, otherwise you may add negative/incorrect values.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                # Left side is the limiting side
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                # Right side is the limiting side
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1

        return water
