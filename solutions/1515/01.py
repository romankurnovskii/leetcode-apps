def findMinFibonacciNumbers(k):
    """
    Find the minimum number of Fibonacci numbers whose sum equals k.

    Args:
        k: int - Target sum to achieve

    Returns:
        int - Minimum number of Fibonacci numbers needed
    """
    # Generate Fibonacci numbers up to k
    fib_numbers = [1, 1]

    # Keep generating Fibonacci numbers until we exceed k
    while fib_numbers[-1] <= k:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > k:
            break
        fib_numbers.append(next_fib)

    # Use greedy approach: always choose largest possible Fibonacci number
    count = 0
    remaining = k

    # Start from the largest Fibonacci number and work backwards
    for i in range(len(fib_numbers) - 1, -1, -1):
        if fib_numbers[i] <= remaining:
            remaining -= fib_numbers[i]
            count += 1

            # If we've reached the target, we're done
            if remaining == 0:
                break

    return count
