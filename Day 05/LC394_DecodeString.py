"""
Problem: Decode String (LeetCode 394)
Topic: Stack
Approach: Use stacks for numbers and previous strings.
          When we see '[': push current string and repeat count, reset current string.
          When we see ']': pop repeat count and previous string, set cur = prev + cur * count.
Time: O(n) (plus cost of building output)
Space: O(n)
Pitfall: Handle multi-digit numbers (e.g., "12[a]") by num = num*10 + digit.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        cur = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                num_stack.append(num)
                str_stack.append(cur)
                num = 0
                cur = ""

            elif ch == "]":
                k = num_stack.pop()
                prev = str_stack.pop()
                cur = prev + cur * k

            else:
                cur += ch

        return cur
