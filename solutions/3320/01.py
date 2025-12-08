class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        # Try all 4 parity patterns: all even, all odd, even-odd, odd-even
        patterns = [
            lambda x: x % 2 == 0,  # all even
            lambda x: x % 2 == 1,  # all odd
            lambda x, i: (x % 2 == 0) if i % 2 == 0 else (x % 2 == 1),  # even-odd
            lambda x, i: (x % 2 == 1) if i % 2 == 0 else (x % 2 == 0),  # odd-even
        ]

        # For simple patterns (all even, all odd)
        for pattern in patterns[:2]:
            count = sum(1 for num in nums if pattern(num))
            res = max(res, count)

        # For alternating patterns
        # Try even-odd pattern
        count_even_odd = 0
        last_parity = None
        for num in nums:
            if last_parity is None:
                if num % 2 == 0:
                    count_even_odd = 1
                    last_parity = 0
            else:
                expected = 1 - last_parity
                if num % 2 == expected:
                    count_even_odd += 1
                    last_parity = expected
        res = max(res, count_even_odd)

        # Try odd-even pattern
        count_odd_even = 0
        last_parity = None
        for num in nums:
            if last_parity is None:
                if num % 2 == 1:
                    count_odd_even = 1
                    last_parity = 1
            else:
                expected = 1 - last_parity
                if num % 2 == expected:
                    count_odd_even += 1
                    last_parity = expected
        res = max(res, count_odd_even)

        return res
