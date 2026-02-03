
"""
Problem: Longest Substring Without Repeating Characters (LeetCode 3)
Topic: Sliding Window / HashMap
Approach: Use a sliding window with a hashmap storing last seen index of each character.
          If a repeat occurs inside the window, move left to last_seen[ch] + 1.
Time: O(n)
Space: O(k) where k is number of distinct characters (<= n)
Pitfall: Only move left forward (never backward). Use ">= left" check before jumping.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best
