from typing import List
import heapq

"""
Problem: Top K Frequent Elements (LeetCode 347)
Topic: Heap / Priority Queue
Approach: Count frequencies, then keep a min-heap of (freq, num) of size k.
          Pop when heap grows > k. Return the elements in the heap.
Time: O(n log k)
Space: O(n)
Pitfall: Heap stores (frequency, value). Don’t forget to build frequency map first.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        heap = []
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for f, num in heap]
