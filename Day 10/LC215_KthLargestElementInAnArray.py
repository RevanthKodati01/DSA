from typing import List
import heapq

"""
Problem: Kth Largest Element in an Array (LeetCode 215)
Topic: Heap / Priority Queue
Approach: Maintain a min-heap of size k. Push each number; if heap grows > k, pop smallest.
          The heap top is the kth largest.
Time: O(n log k)
Space: O(k)
Pitfall: Use a MIN heap of size k (not a max heap), because Python heapq is min-heap by default.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
