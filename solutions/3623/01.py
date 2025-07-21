from collections import defaultdict

MOD = 10**9 + 7


def countTrapezoids(points):
    y_groups = defaultdict(int)
    for x, y in points:
        y_groups[y] += 1
    pairs = []
    for c in y_groups.values():
        if c >= 2:
            pairs.append(c * (c - 1) // 2)
    total_sum = sum(pairs)
    sum_of_squares = sum(x * x for x in pairs)
    res = (total_sum * total_sum - sum_of_squares) // 2
    return res % MOD
