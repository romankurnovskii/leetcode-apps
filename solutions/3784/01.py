class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        from collections import defaultdict

        # Sum up costs for each character
        char_to_cost = defaultdict(int)
        for ch, co in zip(s, cost):
            char_to_cost[ch] += co

        # Find the character with maximum total cost
        max_cost = max(char_to_cost.values())

        # Keep the character with max cost, delete all others
        # Answer is total cost minus the max cost
        return sum(cost) - max_cost
