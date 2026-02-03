"""
Problem: Longest Repeating Character Replacement (LeetCode 424)
Topic: Sliding Window / Frequency Counting
Approach: Maintain a window and count frequencies of characters in it.
          Let max_freq be the count of the most frequent char in the window.
          Window is valid if (window_size - max_freq) <= k (we can replace the rest).
          Expand right; if invalid, shrink from left.
Time: O(n)
Space: O(1) (only 26 uppercase letters)
Pitfall: Don't decrease max_freq when shrinking; keeping a "stale" max_freq is OK and still correct.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        best = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(max_freq, freq[ch])

            # If replacements needed > k, shrink window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
