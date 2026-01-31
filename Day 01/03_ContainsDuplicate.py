from typing import List

"""
Problem: Contains Duplicate
Topic: Arrays + HashSet
Approach: Use a set to detect repeated elements in O(1) average lookup time.
Time: O(n)
Space: O(n)
Pitfall: Sorting works too (O(n log n)), but set is optimal.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
