from typing import List

class Solution:
    def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l, r]
            if s < target:
                l += 1
            else:
                r -= 1
