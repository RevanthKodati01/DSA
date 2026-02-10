import heapq

"""
Problem: Find Median from Data Stream (LeetCode 295)
Topic: Heap / Priority Queue
Approach: Two heaps:
          - small (max-heap) holds lower half (store negatives)
          - large (min-heap) holds upper half
          Keep sizes balanced: len(small) == len(large) or len(small) == len(large)+1
          Median is top of small (odd) or average of tops (even).
Time: addNum -> O(log n), findMedian -> O(1)
Space: O(n)
Pitfall: Always rebalance heaps after insertion to maintain size and ordering invariant.
"""

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # 1) push to max-heap (small)
        heapq.heappush(self.small, -num)

        # 2) ensure ordering: max(small) <= min(large)
        if self.large and (-self.small[0] > self.large[0]):
            x = -heapq.heappop(self.small)
            heapq.heappush(self.large, x)

        # 3) rebalance sizes
        if len(self.small) > len(self.large) + 1:
            x = -heapq.heappop(self.small)
            heapq.heappush(self.large, x)
        elif len(self.large) > len(self.small):
            x = heapq.heappop(self.large)
            heapq.heappush(self.small, -x)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
