class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # Process the string in chunks of length k and compute hashed chars.
        res = []
        for i in range(0, len(s), k):
            chunk = s[i : i + k]
            total = sum(ord(c) - ord('a') for c in chunk)
            hashed = total % 26
            res.append(chr(ord('a') + hashed))
        return ''.join(res)
