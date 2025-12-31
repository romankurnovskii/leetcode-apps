class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one != -1 and i - last_one - 1 < k:
                    return False
                last_one = i

        return True
