class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            # Extract subarray of size k
            subarray = nums[i : i + k]

            # Check if all elements are consecutive and sorted
            # First, check if sorted in ascending order
            is_sorted = all(subarray[j] <= subarray[j + 1] for j in range(k - 1))

            if not is_sorted:
                res.append(-1)
                continue

            # Check if consecutive
            is_consecutive = all(
                subarray[j] + 1 == subarray[j + 1] for j in range(k - 1)
            )

            if is_consecutive:
                res.append(max(subarray))
            else:
                res.append(-1)

        return res
