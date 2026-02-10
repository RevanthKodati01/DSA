from typing import List
import heapq

"""
Problem: K Closest Points to Origin (LeetCode 973)
Topic: Heap / Priority Queue
Approach: Use a max-heap of size k using negative distances.
          Keep k closest points; if size > k, pop farthest (most negative smallest?).
          In Python, simulate max-heap by pushing (-dist, point).
Time: O(n log k)
Space: O(k)
Pitfall: Use squared distance (x*x + y*y) to avoid sqrt; ordering stays correct.
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # (-dist, x, y)
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)  # removes farthest due to most negative dist
        return [[x, y] for _, x, y in heap]
