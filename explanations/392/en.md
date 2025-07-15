> **Hint:**  Use two pointers to check if you can match all characters of s in t in order.

### Explanation

Let's imagine s as a list of items you want to find, and t as a long conveyor belt of items. You want to see if you can pick up all the items from s, in order, as they appear on the conveyor belt t. You use two pointers: one for s and one for t. Every time you see a match, you move the pointer for s forward. If you reach the end of s, it means you found all the items in order!

This approach is efficient because you only need to go through t once, and you never go back. It's perfect for checking subsequences quickly.
