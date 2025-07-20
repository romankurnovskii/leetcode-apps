from collections import Counter

MOD = 10**9 + 7


def countTrapezoids(points: List[List[int]]) -> int:
    y_count = Counter(y for x, y in points)
    c2 = [c * (c - 1) // 2 for c in y_count.values() if c >= 2]
    res = 0
    for i in range(len(c2)):
        for j in range(i + 1, len(c2)):
            res = (res + c2[i] * c2[j]) % MOD
    return res
