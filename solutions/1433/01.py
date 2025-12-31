class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Sort both strings
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)

        # Check if s1 can break s2
        can_break_1 = all(sorted_s1[i] >= sorted_s2[i] for i in range(len(sorted_s1)))

        # Check if s2 can break s1
        can_break_2 = all(sorted_s2[i] >= sorted_s1[i] for i in range(len(sorted_s2)))

        res = can_break_1 or can_break_2
        return res
