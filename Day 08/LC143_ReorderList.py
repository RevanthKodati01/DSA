from typing import Optional

"""
Problem: Reorder List (LeetCode 143)
Topic: Linked List
Approach:
  1) Find middle using slow/fast pointers.
  2) Reverse second half of the list.
  3) Merge the two halves by alternating nodes.
Time: O(n)
Space: O(1)
Pitfall: Cut the list at the middle (slow.next = None) before merging, or you may create cycles.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        second = slow.next
        slow.next = None  # split list
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev  # new head of reversed second half

        # 3) Merge alternating
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
