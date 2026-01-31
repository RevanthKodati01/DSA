from typing import List

"""
Problem: Two Sum (Unsorted)
Topic: Arrays + HashMap
Approach: HashMap (store value -> index, check complement)
Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i

        return []
