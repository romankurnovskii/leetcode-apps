def checkDivisibility(n: int) -> bool:
    original_n = n

    digit_sum = 0
    digit_product = 1

    temp_n = n

    # Extract digits using arithmetic until the number becomes 0.
    while temp_n > 0:
        digit = temp_n % 10

        digit_sum += digit
        digit_product *= digit

        temp_n //= 10

    total_divisor = digit_sum + digit_product

    # The constraints (n >= 1) ensure total_divisor is never zero.
    res = original_n % total_divisor == 0

    return res
