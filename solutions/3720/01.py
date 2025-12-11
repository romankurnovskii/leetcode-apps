from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Count frequency of each character
        cnt = [0] * 26
        for char in s:
            cnt[ord(char) - ord("a")] += 1

        res = []

        def backtrack(path: list, count: list, big: bool) -> bool:
            if len(path) == len(target):
                if big:
                    res.extend(path)
                    return True
                return False

            pos = len(path)
            # Try each character from 'a' to 'z'
            for c in range(26):
                if count[c] == 0:
                    continue

                char = chr(c + ord("a"))
                # If prefix is not yet bigger than target, skip chars smaller than target[pos]
                if not big and char < target[pos]:
                    continue

                # Choose this character
                path.append(char)
                count[c] -= 1
                new_big = big or (char > target[pos])

                if backtrack(path, count, new_big):
                    return True

                # Backtrack
                path.pop()
                count[c] += 1

            return False

        backtrack([], cnt, False)
        return "".join(res)
