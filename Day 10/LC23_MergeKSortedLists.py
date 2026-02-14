from typing import List, Optional
import heapq

"""
Problem: Merge k Sorted Lists (LeetCode 23)
Topic: Heap / Priority Queue / Linked List
Approach: Push the head of each list into a min-heap keyed by node value.
          Repeatedly pop the smallest node, attach to result, and push its next node if exists.
Time: O(N log k) where N is total number of nodes across lists
Space: O(k)
Pitfall: When node values tie, Python needs a tiebreaker (use an incrementing counter).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0  # tiebreaker for equal values

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        tail.next = None
        return dummy.next

