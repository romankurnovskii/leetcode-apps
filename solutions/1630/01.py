class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        res = []

        for i in range(len(l)):
            subarray = nums[l[i] : r[i] + 1]
            subarray.sort()

            if len(subarray) < 2:
                res.append(True)
                continue

            diff = subarray[1] - subarray[0]
            is_arithmetic = True

            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j - 1] != diff:
                    is_arithmetic = False
                    break

            res.append(is_arithmetic)

        return res
