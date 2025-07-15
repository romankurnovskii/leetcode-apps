def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum
    return [(c + extraCandies) >= max_candies for c in candies]
