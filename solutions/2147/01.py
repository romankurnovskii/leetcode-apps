class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        # Count total seats
        seat_count = corridor.count("S")

        # If total seats is odd or zero, no valid division
        if seat_count == 0 or seat_count % 2 != 0:
            return 0

        res = 1
        seats_seen = 0
        i = 0

        # Process the corridor
        while i < len(corridor):
            if corridor[i] == "S":
                seats_seen += 1

                # When we've seen 2 seats, we've completed a segment
                if seats_seen == 2:
                    # Look ahead to find the next segment (next 2 seats)
                    # Count plants between current segment and next segment
                    plants_between = 0
                    j = i + 1

                    # Skip plants until we find the next seat
                    while j < len(corridor) and corridor[j] == "P":
                        plants_between += 1
                        j += 1

                    # If we found another seat (meaning there's a next segment)
                    if j < len(corridor):
                        # We can place divider in (plants_between + 1) positions
                        # (before each plant + after the last plant)
                        res = (res * (plants_between + 1)) % MOD
                        seats_seen = 0  # Reset for next segment
                        i = j - 1  # Will be incremented by loop
            i += 1

        return res
