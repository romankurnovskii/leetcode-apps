class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the difference (costA - costB)
        # This prioritizes people who save more by going to city A
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        res = 0

        # First n people go to city A, rest go to city B
        for i in range(n):
            res += costs[i][0]  # City A
        for i in range(n, len(costs)):
            res += costs[i][1]  # City B

        return res
