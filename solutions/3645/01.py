class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        from collections import defaultdict
        import heapq
        
        # Group items by their limit values
        groups = defaultdict(list)
        for i, (v, l) in enumerate(zip(value, limit)):
            groups[l].append(v)
        
        res = 0
        active_count = 0
        
        # Process groups in order of limit (smallest first)
        for limit_val in sorted(groups.keys()):
            # Use min-heap to keep top min(limit_val, len(group)) values
            heap = []
            for v in groups[limit_val]:
                heapq.heappush(heap, v)
                if len(heap) > limit_val:
                    heapq.heappop(heap)
            
            # Sum all values in heap and add to result
            res += sum(heap)
            active_count += len(heap)
        
        return res

