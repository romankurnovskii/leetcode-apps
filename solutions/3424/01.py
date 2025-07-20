def minCost(arr: List[int], brr: List[int], k: int) -> int:
    # Cost without rearrangement
    cost_no_rearrange = sum(abs(a - b) for a, b in zip(arr, brr))
    # Cost with rearrangement (sort both arrays)
    cost_rearrange = sum(abs(a - b) for a, b in zip(sorted(arr), sorted(brr))) + k
    # Return the minimum
    return min(cost_no_rearrange, cost_rearrange)
