class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # Convert n to string to iterate through digits
        s = str(n)
        
        # Count frequency of each digit
        freq = {}
        for digit in s:
            freq[digit] = freq.get(digit, 0) + 1
        
        # Find the minimum frequency
        min_freq = min(freq.values())
        
        # Find all digits with minimum frequency and return the smallest
        least_frequent_digits = [int(d) for d, count in freq.items() if count == min_freq]
        return min(least_frequent_digits)

