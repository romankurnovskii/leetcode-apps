class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of values to Roman symbols
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        res = ""

        # Greedily subtract largest possible values
        for i in range(len(values)):
            count = num // values[i]
            res += symbols[i] * count
            num %= values[i]

        return res
