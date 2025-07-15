> **Hint:**  Use a hash map to count occurrences and find pairs efficiently.

### Explanation

Imagine you have a bag of numbers and you want to make as many pairs as possible that add up to k. For each number, check if you have seen its complement (k - number) before. If so, you can make a pair! Use a hash map to keep track of the numbers you have seen and how many are left.

This approach is efficient because it lets you find pairs in a single pass through the array. 