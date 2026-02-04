"""
Problem: Min Stack (LeetCode 155)
Topic: Stack
Approach: Maintain two stacks:
          - main stack for values
          - min stack for current minimum at each push
          On pop, pop from both. getMin is top of min stack.
Time: O(1) per operation
Space: O(n)
Pitfall: Push to min stack every time (use min(current, previous_min)), not only when value is smaller.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
