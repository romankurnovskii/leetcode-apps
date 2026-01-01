class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = {"c": 0, "r": 0, "o": 0, "a": 0, "k": 0}
        res = 0
        active = 0

        for char in croakOfFrogs:
            if char not in count:
                return -1

            count[char] += 1

            if char == "c":
                active += 1
                res = max(res, active)
            elif char == "k":
                active -= 1

            # Check validity
            if (
                count["c"] < count["r"]
                or count["r"] < count["o"]
                or count["o"] < count["a"]
                or count["a"] < count["k"]
            ):
                return -1

        if active != 0:
            return -1

        return res
