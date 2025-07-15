> **Hint:**  Use a dictionary to count occurrences, then check if the counts are unique using a set.

### Explanation

We want to know if every number in the array appears a unique number of times. First, we count how many times each number appears using a dictionary. Then, we check if all those counts are different by putting them in a set.

We do this because using a dictionary makes counting fast and easy, and a set lets us quickly check for duplicates among the counts. This approach is efficient and avoids unnecessary loops. 