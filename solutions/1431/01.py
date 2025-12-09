class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies
        max_candies = max(candies)
        
        res = []
        
        # For each kid, check if adding extraCandies makes them have the most
        for candy_count in candies:
            if candy_count + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        
        return res
