class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        count = Counter(nums)
        res = 0
        
        for num in list(count.keys()):
            complement = k - num
            
            if complement in count:
                if num == complement:
                    # Same number, can pair with itself
                    pairs = count[num] // 2
                    res += pairs
                    count[num] -= pairs * 2
                else:
                    # Different numbers
                    pairs = min(count[num], count[complement])
                    res += pairs
                    count[num] -= pairs
                    count[complement] -= pairs
        
        return res

