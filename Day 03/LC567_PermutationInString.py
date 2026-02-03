"""
Problem: Permutation in String (LeetCode 567)
Topic: Sliding Window / Frequency Counting
Approach: Use a fixed-size window of length len(s1) over s2.
          Compare character counts of the window with s1 counts.
Time: O(n) where n = len(s2)
Space: O(1) (26 lowercase letters)
Pitfall: Update counts correctly when sliding: add right char, remove left char.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # counts for lowercase letters
        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        # initial window
        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        # slide window
        for right in range(m, n):
            window[ord(s2[right]) - ord('a')] += 1
            left = right - m
            window[ord(s2[left]) - ord('a')] -= 1

            if window == need:
                return True

        return False
