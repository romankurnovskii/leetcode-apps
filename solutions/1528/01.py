class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create result array of same length
        res = [""] * len(s)

        # Place each character at its correct index
        for i, char in enumerate(s):
            res[indices[i]] = char

        return "".join(res)
