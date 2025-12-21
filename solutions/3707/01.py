class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)

        # Try all possible split positions
        # Split at index i means: left = s[0..i], right = s[i+1..n-1]
        # Both must be non-empty, so i can range from 0 to n-2
        for i in range(n - 1):
            # Calculate score of left substring s[0..i]
            left_score = 0
            for j in range(i + 1):
                left_score += ord(s[j]) - ord("a") + 1

            # Calculate score of right substring s[i+1..n-1]
            right_score = 0
            for j in range(i + 1, n):
                right_score += ord(s[j]) - ord("a") + 1

            # Check if scores are equal
            if left_score == right_score:
                return True

        return False
