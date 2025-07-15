def uniqueOccurrences(arr):
    from collections import Counter

    count = Counter(arr)
    return len(set(count.values())) == len(count)
