from typing import Optional

"""
Problem: Linked List Cycle (LeetCode 141)
Topic: Linked List / Two Pointers
Approach: Floyd’s Cycle Detection (tortoise and hare).
          slow moves 1 step, fast moves 2 steps. If they meet, cycle exists.
Time: O(n)
Space: O(1)
Pitfall: Always check fast and fast.next before moving fast two steps to avoid None errors.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
