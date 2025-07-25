def is_palindrome(s: str) -> bool:
    left = 0  # Pointer starting from the beginning of the string
    right = len(s) - 1  # Pointer starting from the end of the string

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if left < right:
            if s[left].lower() != s[right].lower():
                res = False
                return res

            left += 1
            right -= 1

    res = True
    return res
