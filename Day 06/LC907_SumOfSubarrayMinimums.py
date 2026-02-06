from typing import List

"""
Problem: Sum of Subarray Minimums (LeetCode 907)
Topic: Monotonic Stack
Approach: Each element nums[i] contributes nums[i] * (count of subarrays where it's the minimum).
          Find:
          - prevLess: distance to previous strictly less element
          - nextLessEq: distance to next less-or-equal element
          Using monotonic increasing stacks:
          - For prevLess: pop while >= (so remaining is strictly <)
          - For nextLessEq: pop while > (so remaining is <=)
          Contribution = nums[i] * left * right
Time: O(n)
Space: O(n)
Pitfall: Inequality choice matters to avoid double counting duplicates:
         use prev strictly less (<) and next less-or-equal (<=).
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # left[i] = number of subarrays ending at i where arr[i] is minimum (distance to prev strictly less)
        left = [0] * n
        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count

        # right[i] = number of subarrays starting at i where arr[i] is minimum (distance to next less-or-equal)
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD

        return ans
