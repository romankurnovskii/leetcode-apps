def maxVowels(s: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    current_vowel_count = 0

    # 1. Calculate the vowel count for the initial window (first k characters)
    for i in range(k):
        if s[i] in vowels:
            current_vowel_count += 1

    max_vowel_count = current_vowel_count

    # 2. Slide the window across the rest of the string
    # The right pointer 'i' starts from k up to len(s) - 1
    for i in range(k, len(s)):
        # Remove the contribution of the character leaving the window
        # The character leaving is at index (i - k)
        if s[i - k] in vowels:
            current_vowel_count -= 1

        # Add the contribution of the new character entering the window
        # The new character entering is at index (i)
        if s[i] in vowels:
            current_vowel_count += 1

        max_vowel_count = max(max_vowel_count, current_vowel_count)

    res = max_vowel_count
    return res
