from typing import List
from functools import lru_cache

def max_dot_product(nums1: List[int], nums2: List[int]) -> int:
    """
    Returns the maximum dot product of non-empty subsequences
    from nums1 and nums2.
    """
    m, n = len(nums1), len(nums2)
    NEG_INF = -10**20

    @lru_cache(None)
    def dp(i: int, j: int, took: bool) -> int:
        if i == m or j == n:
            return 0 if took else NEG_INF

        take = nums1[i] * nums2[j] + dp(i + 1, j + 1, True)
        skip_nums1 = dp(i + 1, j, took)
        skip_nums2 = dp(i, j + 1, took)

        res = max(take, skip_nums1, skip_nums2)
        return res

    res = dp(0, 0, False)
    return res


# Example usage
if __name__ == "__main__":
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]
    print(max_dot_product(nums1, nums2))  # Expected output: 18
