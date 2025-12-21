class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        m = len(s)

        for i in range(m):
            row, col = startPos[0], startPos[1]
            count = 0

            for j in range(i, m):
                if s[j] == "L":
                    col -= 1
                elif s[j] == "R":
                    col += 1
                elif s[j] == "U":
                    row -= 1
                else:  # 'D'
                    row += 1

                if row < 0 or row >= n or col < 0 or col >= n:
                    break

                count += 1

            res.append(count)

        return res
