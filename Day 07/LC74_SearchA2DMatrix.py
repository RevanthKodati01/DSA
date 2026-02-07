from typing import List

"""
Problem: Search a 2D Matrix (LeetCode 74)
Topic: Binary Search
Approach: Treat the matrix as a flattened sorted array of length m*n.
          Map mid -> (row = mid // n, col = mid % n) and do normal binary search.
Time: O(log (m*n))
Space: O(1)
Pitfall: Don’t do binary search per row; flattened approach is simpler and truly log(m*n).
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
