## Explanation

To solve the Two Sum problem, we want to find two numbers in the array that add up to a given target. The most efficient way is to use a hash map (dictionary) to store the numbers we have seen so far and their indices. As we iterate through the array, for each number, we check if the complement (target - current number) exists in the hash map. If it does, we have found the solution. Otherwise, we add the current number and its index to the hash map. This approach has O(n) time complexity.

## Hint

Try using a hash map to keep track of the numbers you have seen so far and their indices.

## Points

- Time complexity: O(n) using a hash map.
- Brute-force solution is O(n^2) and not efficient for large arrays.
- There is always exactly one solution, and you may not use the same element twice.
- Be careful with duplicate numbers in the array.
