class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # If num = (x-1) + x + (x+1) = 3x
        # Then x = num / 3
        if num % 3 != 0:
            return []

        x = num // 3
        return [x - 1, x, x + 1]
