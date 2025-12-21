class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Group numbers by remainder when divided by 3
        rem = [[], [], []]
        for num in nums:
            rem[num % 3].append(num)

        # Sort each group in descending order
        for i in range(3):
            rem[i].sort(reverse=True)

        res = 0

        # Case 1: Three numbers with remainder 0
        if len(rem[0]) >= 3:
            res = max(res, sum(rem[0][:3]))

        # Case 2: One from each remainder (0, 1, 2)
        if rem[0] and rem[1] and rem[2]:
            res = max(res, rem[0][0] + rem[1][0] + rem[2][0])

        # Case 3: Three numbers with remainder 1
        if len(rem[1]) >= 3:
            res = max(res, sum(rem[1][:3]))

        # Case 4: Three numbers with remainder 2
        if len(rem[2]) >= 3:
            res = max(res, sum(rem[2][:3]))

        return res
