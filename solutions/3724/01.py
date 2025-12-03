class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = float('inf')
        
        # nums2 has one extra element, which must come from appending
        # Try each index j in nums1 as the one to append
        for j in range(n):
            # Cost to make nums1[j] match both nums2[j] and nums2[-1]
            # We need to adjust nums1[j] to one value, then append it
            # The cost is: |nums1[j] - nums2[j]| + |nums1[j] - nums2[-1]|
            # But we can optimize: make nums1[j] equal to one, then adjust the appended copy
            # Actually, we can make one copy nums2[j] and one copy nums2[-1]
            # Cost = |nums1[j] - nums2[j]| + |nums1[j] - nums2[-1]|
            # But wait, we append first, then adjust. So:
            # 1. Append nums1[j] (cost 0 for append operation itself)
            # 2. Adjust original to nums2[j]: |nums1[j] - nums2[j]|
            # 3. Adjust appended to nums2[-1]: |nums1[j] - nums2[-1]|
            
            cost = abs(nums1[j] - nums2[j]) + abs(nums1[j] - nums2[-1])
            
            # Cost to transform all other positions
            for i in range(n):
                if i != j:
                    cost += abs(nums1[i] - nums2[i])
            
            res = min(res, cost)
        
        return res

