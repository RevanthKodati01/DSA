from typing import List

"""
Problem: Partition Labels (LeetCode 763)
Topic: Greedy
Approach: Record last index of each character.
          Scan string and track current partition end as max(last[ch]) seen so far.
          When i reaches end, close a partition and start new one.
Time: O(n)
Space: O(1) (26 lowercase letters)
Pitfall: Partition end must be the furthest last occurrence among all chars in current partition.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
