class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort pairs by nums2 in descending order
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        import heapq

        # Use min heap to maintain k largest nums1 values
        heap = []
        res = 0
        current_sum = 0

        for num1, num2 in pairs:
            # Add current num1 to heap and sum
            heapq.heappush(heap, num1)
            current_sum += num1

            # If we have more than k elements, remove the smallest
            if len(heap) > k:
                current_sum -= heapq.heappop(heap)

            # If we have exactly k elements, calculate score
            if len(heap) == k:
                # num2 is the minimum in current selection (since we sorted descending)
                score = current_sum * num2
                res = max(res, score)

        return res
