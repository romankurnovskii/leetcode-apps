class Solution:
    def countDistinct(self, n: int) -> int:
        # For each integer x from 1 to n, remove zeros and count distinct results
        distinct_set = set()

        for x in range(1, n + 1):
            # Remove zeros from decimal representation
            s = str(x)
            s_no_zeros = s.replace("0", "")
            if s_no_zeros:  # If not empty after removing zeros
                distinct_set.add(int(s_no_zeros))
            else:
                # If all zeros, the result is empty, but we can represent it as 0 or empty
                # Actually, removing zeros from a number with only zeros gives empty string
                # But we need to handle this - let's check the examples
                # For n=10: 10 -> "10" -> "1" -> 1
                # So we should add something for numbers that become empty
                # Actually, looking at example: n=10 gives 9 distinct (1-9), and 10 becomes 1
                # So empty strings might not be counted, or they become 0
                pass

        return len(distinct_set)
