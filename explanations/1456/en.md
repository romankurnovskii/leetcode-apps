> **Hint:**  Use a sliding window to count vowels in each substring of length k.

### Explanation

We want to find the most vowels in any substring of length k. To do this efficiently, we use a sliding window: we count the vowels in the first window, then as we move the window, we subtract the letter that leaves and add the new letter that enters.

We do this because it lets us update our count in constant time, instead of recounting every window from scratch. This makes our solution much faster, especially for long strings.

By always keeping track of the current number of vowels, we can quickly find the maximum as we slide the window across the string. 