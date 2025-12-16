class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        mx = max(arrivals) if arrivals else 0
        ctr = [0] * (mx + 1)
        res = 0
        
        for idx, item in enumerate(arrivals):
            # Remove item that left the window
            if idx >= w:
                left_item = arrivals[idx - w]
                if left_item != 0:  # Only decrement if it was kept
                    ctr[left_item] -= 1
            
            # Check if we need to discard
            if ctr[item] >= m:
                res += 1
                arrivals[idx] = 0  # Mark as discarded
            else:
                ctr[item] += 1
        
        return res

