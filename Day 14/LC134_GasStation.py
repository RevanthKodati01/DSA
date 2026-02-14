from typing import List

"""
Problem: Gas Station (LeetCode 134)
Topic: Greedy
Approach: If total gas < total cost, impossible.
          Otherwise, the start index is found by scanning:
          keep tank += gas[i] - cost[i]. If tank drops below 0, reset start = i+1 and tank = 0.
Time: O(n)
Space: O(1)
Pitfall: The total sum check is mandatory; without it you might return an invalid start.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start
