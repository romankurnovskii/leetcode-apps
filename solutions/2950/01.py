class Solution:
    def numberOfDivisibleSubstrings(self, word: str) -> int:
        # Map characters to values 1-9 (cyclic)
        # a->1, b->2, ..., i->9, j->1, k->2, ...
        def get_value(c: str) -> int:
            return (ord(c) - ord("a")) % 9 + 1

        n = len(word)
        res = 0

        # Use prefix sum to calculate substring sums in O(1)
        # For each starting position, iterate through all ending positions
        for i in range(n):
            prefix_sum = 0
            for j in range(i, n):
                prefix_sum += get_value(word[j])
                # Check if sum is divisible by 9
                if prefix_sum % 9 == 0:
                    res += 1

        return res
