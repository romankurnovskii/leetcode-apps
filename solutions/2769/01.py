class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # To maximize x, we should decrease x and increase num in each operation
        # After t operations: x becomes x - t, num becomes num + t
        # For them to be equal: x - t = num + t
        # Therefore: x = num + 2 * t
        res = num + 2 * t
        return res

