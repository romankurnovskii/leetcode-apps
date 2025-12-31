from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        # If a == b, then a ^ b == 0
        # So we need arr[i] ^ ... ^ arr[j-1] ^ arr[j] ^ ... ^ arr[k] == 0
        # Which means the XOR from i to k is 0
        # For each pair (i, k) where XOR from i to k is 0, any j in (i, k] works

        for i in range(n):
            xor = 0
            for k in range(i, n):
                xor ^= arr[k]
                if xor == 0:
                    res += k - i

        return res
