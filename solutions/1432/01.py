class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Find maximum: replace first non-9 digit with 9
        max_val = num_str
        for char in num_str:
            if char != "9":
                max_val = max_val.replace(char, "9")
                break

        # Find minimum:
        # If first digit is not 1, replace it with 1
        # Otherwise, replace first non-0, non-1 digit with 0
        min_val = num_str
        if num_str[0] != "1":
            first_char = num_str[0]
            min_val = min_val.replace(first_char, "1")
        else:
            # Find first digit that's not 0 or 1 and replace all occurrences with 0
            for char in num_str[1:]:
                if char not in "01":
                    min_val = min_val.replace(char, "0")
                    break

        res = int(max_val) - int(min_val)
        return res
