class Solution:
    def kthCharacter(self, k: int) -> str:
        # Start with 'a' at position 1
        # Each operation doubles the string length
        # We trace back to find which character in the original string contributed to position k

        # Count how many transformations (+1 operations) we need
        transformations = 0

        # Trace back from k to position 1
        pos = k
        while pos > 1:
            # Find the largest power of 2 <= pos
            power = 1
            while power * 2 <= pos:
                power *= 2

            if pos == power:
                # pos is exactly a power of 2, it's in the new half
                pos = pos - power
            else:
                # pos is in the appended half
                pos = pos - power
                transformations += 1

        # Start with 'a' (ASCII 97) and apply transformations
        # Each transformation adds 1 to the character
        result_char = ord("a") + transformations
        return chr(result_char)
