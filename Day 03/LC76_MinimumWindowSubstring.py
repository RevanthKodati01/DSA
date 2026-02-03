"""
Problem: Minimum Window Substring (LeetCode 76)
Topic: Sliding Window / HashMap
Approach: Expand right to satisfy all required characters from t.
          Once valid, shrink left to minimize the window while staying valid.
          Track best (smallest) valid window seen.
Time: O(n) where n = len(s)
Space: O(k) where k = number of distinct chars in t
Pitfall: Use "formed == required" to know when window is valid, and update counts carefully when shrinking.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float("inf")
        best_l = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try to shrink while window is valid
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_l: best_l + best_len]
