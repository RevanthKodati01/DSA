from typing import Optional

"""
Problem: Remove Nth Node From End of List (LeetCode 19)
Topic: Linked List / Two Pointers
Approach: Use a dummy node. Move fast pointer n steps ahead, then move slow+fast until fast hits end.
          slow.next is the node to remove.
Time: O(n)
Space: O(1)
Pitfall: Use a dummy head to handle removing the actual head node cleanly.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast is at last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove slow.next
        slow.next = slow.next.next
        return dummy.next
