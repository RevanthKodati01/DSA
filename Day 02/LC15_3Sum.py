from typing import List

"""
Problem: 3Sum (LeetCode 15)
Topic: Two Pointers / Sorting
Approach: Sort the array. Fix i, then use two pointers (l, r) to find pairs that sum to -nums[i].
          Skip duplicates for i, and also skip duplicates after finding a valid triplet.
Time: O(n^2)
Space: O(1) extra (excluding output)
Pitfall: Duplicate handling is the main trap—skip repeated i values, and skip repeated l/r values after a match.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optimization: if anchor > 0, remaining are > 0 (sorted) => cannot sum to 0
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicates on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res

