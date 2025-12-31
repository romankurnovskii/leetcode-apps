class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Get all source cities (left side) and destination cities (right side)
        sources, destinations = map(set, zip(*paths))
        # Destination city is the one that appears only on the right side
        res = (destinations - sources).pop()
        return res
