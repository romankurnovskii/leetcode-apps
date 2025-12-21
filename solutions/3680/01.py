class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        res = []
        if n < 5:
            return res
        if n % 2:
            # Odd n: Adjacent pairs
            for i in range(0, 2 * n, 2):
                res.append([i % n, (i + 1) % n])
            for i in range(0, 2 * n, 2):
                res.append([(i + 1) % n, i % n])
        else:
            # Even n: Adjacent pairs
            for i in range(0, n, 2):
                res.append([i, i + 1])
            for i in range(0, n, 2):
                res.append([i + 1, i])
            for i in range(1, n, 2):
                res.append([i, (i + 1) % n])
            for i in range(1, n, 2):
                res.append([(i + 1) % n, i])

        for diff in range(2, (n + 1) // 2):
            # Find pairs that are diff apart
            start = res[-1][0] + 1
            for i in range(start, start + n):
                res.append([i % n, (i + diff) % n])
            start = res[-1][-1] - 1
            for i in range(start, start + n):
                res.append([(i + diff) % n, i % n])

        if n % 2 == 0:
            # Find pairs that are n/2 apart
            start = res[-1][0] - 1
            for i in range(start, start + n):
                res.append([i % n, (i + n // 2) % n])
        return res
