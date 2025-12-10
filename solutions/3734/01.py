from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Check if palindromic permutation is possible
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

        if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
            return ""

        # Build first half of palindrome
        chars = sorted(char_count.keys())
        half = []
        middle_char = ""

        # Distribute characters for first half
        for char in chars:
            count = char_count[char]
            if count % 2 == 1:
                middle_char = char
            half.extend([char] * (count // 2))

        # Try to find lexicographically smallest palindrome > target
        from itertools import permutations

        # Generate all permutations of the first half
        seen = set()
        candidates = []

        def build_palindrome(first_half):
            second_half = first_half[::-1]
            if middle_char:
                return "".join(first_half) + middle_char + "".join(second_half)
            else:
                return "".join(first_half) + "".join(second_half)

        # Try all unique permutations of first half
        for perm in set(permutations(half)):
            palindrome = build_palindrome(list(perm))
            if palindrome > target:
                candidates.append(palindrome)

        if not candidates:
            return ""

        return min(candidates)
