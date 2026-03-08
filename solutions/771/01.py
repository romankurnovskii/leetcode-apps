class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        result = 0               # Counter for how many jewels we found
        for s in stones:         # Loop through each character (stone) in stones
            if s in jewels:      # Check if this stone type is listed in jewels
                result += 1      # If yes, increase the counter
        return result            # Return the total count
