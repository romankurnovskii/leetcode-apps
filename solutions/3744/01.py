class Solution:
    def findKthCharacter(self, s: str, k: int) -> str:
        expanded = []
        i = 0
        n = len(s)

        while i < n:
            if s[i].isdigit():
                num_str = ""
                while i < n and s[i].isdigit():
                    num_str += s[i]
                    i += 1

                if i < n and s[i] == "(":
                    i += 1
                    substr = ""
                    depth = 1
                    while i < n and depth > 0:
                        if s[i] == "(":
                            depth += 1
                        elif s[i] == ")":
                            depth -= 1
                        if depth > 0:
                            substr += s[i]
                        i += 1

                    num = int(num_str)
                    expanded.extend(list(substr) * num)
                else:
                    expanded.append(s[i] if i < n else "")
                    i += 1
            else:
                expanded.append(s[i])
                i += 1

        return expanded[k - 1] if k <= len(expanded) else ""
