def climbStairs(n: int) -> int:
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev, curr = 1, 2

    for i in range(3, n + 1):
        next_val = prev + curr
        prev, curr = curr, next_val

    return curr
