from typing import List

"""
Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)
Topic: Two Pointers / Arrays
Approach: Two pointers on sorted array. If sum < target move left++; if sum > target move right--.
Time: O(n)
Space: O(1)
Pitfall: Output indices are 1-based (return [l+1, r+1]).
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
