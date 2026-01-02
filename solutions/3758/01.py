from typing import List


class Solution:
    def convertToDigits(self, s: str) -> str:
        word_to_digit = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        res = []
        i = 0
        n = len(s)

        while i < n:
            found = False
            for word, digit in word_to_digit.items():
                if s[i:].startswith(word):
                    res.append(digit)
                    i += len(word)
                    found = True
                    break
            if not found:
                res.append(s[i])
                i += 1

        return "".join(res)
