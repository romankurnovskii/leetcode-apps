from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        res = [0] * n
        res[0] = pref[0]

        # For each position i, we have: pref[i] = res[0] ^ res[1] ^ ... ^ res[i]
        # We know: pref[i-1] = res[0] ^ res[1] ^ ... ^ res[i-1]
        # Therefore: pref[i] = pref[i-1] ^ res[i]
        # So: res[i] = pref[i] ^ pref[i-1]
        for i in range(1, n):
            res[i] = pref[i] ^ pref[i - 1]

        return res
