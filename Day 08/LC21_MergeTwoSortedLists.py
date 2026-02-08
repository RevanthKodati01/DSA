from typing import Optional

"""
Problem: Merge Two Sorted Lists (LeetCode 21)
Topic: Linked List
Approach: Use a dummy head and tail pointer. Repeatedly attach the smaller node from l1 or l2.
          At the end, attach the remaining list.
Time: O(n + m)
Space: O(1)
Pitfall: Always move the tail after attaching a node, and return dummy.next (not dummy).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
