class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Use rolling array of size 3 to save space
        # dp[i] represents minimum cost to reach step i
        v0 = v1 = v2 = 0
        
        for i, c in enumerate(costs):
            # From step i, we can reach step i+1, i+2, or i+3
            # Cost = previous cost + jump cost (1, 4, or 9) + step cost
            v = min(v0 + 9, v1 + 4, v2 + 1) + c
            v0, v1, v2 = v1, v2, v
        
        return v2

