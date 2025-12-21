def isAnagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False

        char_count[char] -= 1

        # If count becomes negative, strings are not anagrams
        if char_count[char] < 0:
            return False

    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True
