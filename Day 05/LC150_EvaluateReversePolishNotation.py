from typing import List

"""
Problem: Evaluate Reverse Polish Notation (LeetCode 150)
Topic: Stack
Approach: Use a stack. Push numbers. On operator, pop two values (b then a), compute a op b, push result back.
Time: O(n)
Space: O(n)
Pitfall: Division must truncate toward zero (use int(a / b), not // which floors for negatives).
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))  # truncates toward 0

        return stack[-1]
