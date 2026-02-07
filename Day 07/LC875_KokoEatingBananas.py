from typing import List

"""
Problem: Koko Eating Bananas (LeetCode 875)
Topic: Binary Search on Answer
Approach: Binary search the eating speed k (1..max(piles)).
          Check feasibility: hours_needed = sum(ceil(pile/k)) must be <= h.
Time: O(n log M) where M = max(piles)
Space: O(1)
Pitfall: Compute ceil division as (pile + k - 1) // k (avoid floats).
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_finish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # ceil(p / k)
                if hours > h:  # early stop
                    return False
            return hours <= h

        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return l
