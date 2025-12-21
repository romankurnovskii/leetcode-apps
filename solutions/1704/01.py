class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s)
        mid = n // 2

        count_first = 0
        count_second = 0

        # Count vowels in first half
        for i in range(mid):
            if s[i] in vowels:
                count_first += 1

        # Count vowels in second half
        for i in range(mid, n):
            if s[i] in vowels:
                count_second += 1

        return count_first == count_second
