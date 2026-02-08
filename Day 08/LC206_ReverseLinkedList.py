from typing import Optional

"""
Problem: Reverse Linked List (LeetCode 206)
Topic: Linked List
Approach: Iterative pointer reversal using prev and cur.
          For each node: save next, point cur.next to prev, then advance.
Time: O(n)
Space: O(1)
Pitfall: Save next node before changing cur.next, or you’ll lose the rest of the list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
