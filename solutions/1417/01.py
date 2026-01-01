class Solution:
    def reformat(self, s: str) -> str:
        digits = [c for c in s if c.isdigit()]
        letters = [c for c in s if c.isalpha()]

        if abs(len(digits) - len(letters)) > 1:
            return ""

        res = []
        if len(digits) >= len(letters):
            for i in range(len(letters)):
                res.append(digits[i])
                res.append(letters[i])
            if len(digits) > len(letters):
                res.append(digits[-1])
        else:
            for i in range(len(digits)):
                res.append(letters[i])
                res.append(digits[i])
            if len(letters) > len(digits):
                res.append(letters[-1])

        return "".join(res)
