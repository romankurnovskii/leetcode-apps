class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        # Sliding window approach: find minimum sum of subarray of length (n - k)
        # Then answer is total_sum - min_subarray_sum
        
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum
        
        # Slide the window
        for i in range(window_size, n):
            window_sum = window_sum - cardPoints[i - window_size] + cardPoints[i]
            min_sum = min(min_sum, window_sum)
        
        # Total sum minus minimum window sum
        total_sum = sum(cardPoints)
        res = total_sum - min_sum
        
        return res

