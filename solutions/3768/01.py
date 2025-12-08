class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        # Compress numbers to range [1, n]
        sorted_nums = sorted(set(nums))
        comp_map = {val: idx + 1 for idx, val in enumerate(sorted_nums)}
        compressed = [comp_map[num] for num in nums]
        n = len(compressed)
        
        # Fenwick Tree (Binary Indexed Tree) for counting
        class FenwickTree:
            def __init__(self, size):
                self.n = size
                self.tree = [0] * (size + 1)
            
            def update(self, idx, delta):
                while idx <= self.n:
                    self.tree[idx] += delta
                    idx += idx & -idx
            
            def query(self, idx):
                res = 0
                while idx > 0:
                    res += self.tree[idx]
                    idx -= idx & -idx
                return res
        
        # Initialize Fenwick Tree
        ft = FenwickTree(n)
        
        # Calculate inversion count for first window
        inv_count = 0
        for i in range(k):
            # Count numbers greater than compressed[i] in current window
            inv_count += i - ft.query(compressed[i])
            ft.update(compressed[i], 1)
        
        res = inv_count
        
        # Slide window
        for i in range(k, n):
            # Remove leftmost element
            ft.update(compressed[i - k], -1)
            # Count numbers smaller than removed element
            removed = compressed[i - k]
            smaller = ft.query(removed - 1)
            inv_count -= smaller
            
            # Add new element
            new_val = compressed[i]
            # Count numbers greater than new element in current window
            greater = (k - 1) - ft.query(new_val)
            inv_count += greater
            ft.update(new_val, 1)
            
            res = min(res, inv_count)
        
        return res
