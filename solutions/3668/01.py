class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Create a set for O(1) lookup
        friend_set = set(friends)
        res = []
        
        # Iterate through order and collect friends in their finishing order
        for num in order:
            if num in friend_set:
                res.append(num)
        
        return res

