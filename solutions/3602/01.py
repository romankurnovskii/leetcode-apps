def concatHex36(n: int) -> str:
    n2 = n * n
    n3 = n * n * n
    hex_part = format(n2, 'X')
    base36_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base36_part = ''
    num = n3
    while num > 0:
        # Find the remainder when num is divided by 36,
        # use it as an index to get the corresponding base36 character,
        # and prepend it to base36_part.
        base36_part = base36_chars[num % 36] + base36_part
        num //= 36
    return hex_part + base36_part