from typing import List, Dict

"""
Problem: Accounts Merge (LeetCode 721)
Topic: Union Find (Disjoint Set Union)
Approach: Union all emails within the same account (connect each email to the first email in that account).
          After unions, group emails by their root, sort them, and attach the account name.
Time: O(E α(E) + E log E) where E = number of emails
Space: O(E)
Pitfall: Multiple accounts can share emails; DSU must be built over emails (strings), not over account indices.
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent: Dict[str, str] = {}
        rank: Dict[str, int] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            rank.setdefault(x, 0)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: str, b: str) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        email_to_name: Dict[str, str] = {}

        # Union emails in each account
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                email_to_name[email] = name
                union(first_email, email)

        # Group emails by root
        groups: Dict[str, List[str]] = {}
        for email in email_to_name:
            root = find(email)
            groups.setdefault(root, []).append(email)

        # Build result
        res = []
        for root, emails in groups.items():
            emails.sort()
            res.append([email_to_name[root]] + emails)

        return res
