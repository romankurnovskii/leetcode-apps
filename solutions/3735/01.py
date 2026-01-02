class Solution:
    def smallestString(self, s: str, k: int) -> str:
        s_list = list(s)
        n = len(s_list)

        for i in range(n):
            if k <= 0:
                break

            target = "a"
            for j in range(26):
                char = chr(ord("a") + j)
                dist = min(
                    abs(ord(s_list[i]) - ord(char)),
                    26 - abs(ord(s_list[i]) - ord(char)),
                )
                if dist <= k:
                    target = char
                    k -= dist
                    break

            s_list[i] = target

        return "".join(s_list)
