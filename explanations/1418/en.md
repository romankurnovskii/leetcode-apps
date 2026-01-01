## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a list of food orders (each with table number and food item), we need to display a table showing the number of each food item ordered per table, with tables and food items in lexicographical order.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of orders can be up to 10^4.
- **Time Complexity:** O(n + t * f) where n is the number of orders, t is the number of tables, and f is the number of food items - we need to process orders, then format the table.
- **Space Complexity:** O(t * f) - we need to store counts for each table-food combination.
- **Edge Case:** If a table didn't order a particular food, the count should be 0. Tables and foods should be sorted lexicographically.

**1.2 High-level approach:**

The goal is to use a nested dictionary to count orders per table and food item, then format the results into a table with proper sorting.

![Food order table visualization](https://assets.leetcode.com/static_assets/others/food-table.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each table, check each food item and count orders. This is what we essentially do, but we organize it efficiently.
- **Optimized Strategy:** Use a dictionary to count all orders first, then format the table. This is O(n) for counting and O(t * f) for formatting.
- **Optimization:** By using a dictionary structure, we can efficiently count and then format the results without redundant iterations.

**1.4 Decomposition:**

1. Extract all unique food items and sort them.
2. Extract all unique table numbers and sort them.
3. Use a dictionary to count orders: table_orders[table][food] = count.
4. Build the result table: first row is header ["Table"] + foods, then one row per table with counts.
5. Return the formatted table.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]`

- Foods set: `{"Ceviche", "Beef Burrito", "Fried Chicken", "Water"}`
- Sorted foods: `["Beef Burrito", "Ceviche", "Fried Chicken", "Water"]`
- Tables: `{3, 5, 10}`
- Sorted tables: `[3, 5, 10]`
- Count dictionary: `table_orders[3]["Ceviche"] = 2, table_orders[3]["Fried Chicken"] = 1, ...`

**2.2 Start Checking:**

We build the table row by row.

**2.3 Trace Walkthrough:**

| Step | Row | Content |
| ---- | --- | ------- |
| 1    | Header | ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"] |
| 2    | Table 3 | ["3", "0", "2", "1", "0"] |
| 3    | Table 5 | ["5", "0", "1", "0", "1"] |
| 4    | Table 10 | ["10", "1", "0", "0", "0"] |

**2.4 Increment and Loop:**

We iterate through sorted tables and for each table, we add counts for each sorted food item.

**2.5 Return Result:**

The result is a 2D array representing the formatted table with headers and data rows, sorted appropriately.

