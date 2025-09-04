def addBinary( a: str, b: str) -> str:
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0:
        # Get current bits (0 if index is out of range)
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a + bit_b + carry

        # Calculate result bit and carry
        result_bit = total % 2
        carry = total // 2

        # Add result bit to beginning
        result = str(result_bit) + result

        i -= 1
        j -= 1

    # Add final carry if exists
    if carry:
        result = "1" + result

    return result
