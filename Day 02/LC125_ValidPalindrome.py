"""
Problem: Valid Palindrome (LeetCode 125)
Topic: Two Pointers / Strings
Approach: Use left/right pointers. Skip non-alphanumeric characters and compare lowercase characters.
Time: O(n)
Space: O(1)
Pitfall: Make sure to skip non-alphanumeric on BOTH sides before comparing.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
