"""
Problem: Valid Parentheses (LeetCode 20)
Topic: Stack
Approach: Use a stack to store opening brackets. For each closing bracket, the top of the stack must be the matching opening.
Time: O(n)
Space: O(n)
Pitfall: Always check stack is not empty before popping; leftover openings means invalid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
