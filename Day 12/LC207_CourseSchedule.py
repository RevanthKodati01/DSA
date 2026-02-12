from typing import List
from collections import deque

"""
Problem: Course Schedule (LeetCode 207)
Topic: Graphs / Topological Sort (BFS)
Approach: Build adjacency list + indegree array. Use Kahn’s algorithm:
          - push all nodes with indegree 0 into queue
          - pop, reduce indegree of neighbors, push any that become 0
          If we process all courses, schedule is possible.
Time: O(V + E)
Space: O(V + E)
Pitfall: Don’t forget to count processed nodes; cycle exists if processed != numCourses.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        done = 0

        while q:
            course = q.popleft()
            done += 1
            for nxt in graph[course]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return done == numCourses
