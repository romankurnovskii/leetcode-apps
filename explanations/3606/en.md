## 3606. Coupon Code Validator [Easy]

https://leetcode.com/problems/coupon-code-validator

## Description
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
- code[i]: a string representing the coupon identifier.
- businessLine[i]: a string denoting the business category of the coupon.
- isActive[i]: a boolean indicating whether the coupon is currently active.

A coupon is considered valid if all of the following conditions hold:
1. code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
2. businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
3. isActive[i] is true.

Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

## Examples

**Example 1**
Input:
code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
isActive = [true, true, true, true]

Output:
["PHARMA5", "SAVE20"]

Explanation:
- First coupon is valid.
- Second coupon has empty code (invalid).
- Third coupon is valid.
- Fourth coupon has special character @ (invalid).

**Example 2**
Input:
code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"]
businessLine = ["grocery", "electronics", "invalid"]
isActive = [false, true, true]

Output:
["ELECTRONICS_50"]

Explanation:
- First coupon is inactive (invalid).
- Second coupon is valid.
- Third coupon has invalid business line (invalid).

## Constraints
- n == code.length == businessLine.length == isActive.length
- 1 <= n <= 100
- 0 <= code[i].length, businessLine[i].length <= 100
- code[i] and businessLine[i] consist of printable ASCII characters.
- isActive[i] is either true or false.

## Hint
- Filter out any coupon where isActive[i] is false, code[i] is empty or contains non-alphanumeric/underscore chars, or businessLine[i] is not in the allowed set.
- Store each remaining coupon as a pair (businessLine[i], code[i]).
- Define a priority map, e.g. {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}.
- Sort the list of pairs by (priority[businessLine], code) and return the code values in order.

## Explanation

**Intuition**

The problem requires us to filter and sort coupons based on a set of validation rules and a custom sorting order. The key insight is to first validate each coupon for code format, business line, and active status, and then sort the valid ones by business line priority and code.

**Approach**

1. **Validation:**
   - Check that the code is non-empty and contains only alphanumeric characters or underscores.
   - Ensure the business line is one of the allowed categories: "electronics", "grocery", "pharmacy", or "restaurant".
   - Confirm the coupon is active.
2. **Priority Mapping:**
   - Assign a priority to each business line: electronics = 0, grocery = 1, pharmacy = 2, restaurant = 3.
3. **Collect Valid Coupons:**
   - For each valid coupon, store its business line and code as a pair.
4. **Sorting:**
   - Sort the valid coupons first by business line priority, then lexicographically by code within each business line.
5. **Result Extraction:**
   - Extract and return only the codes from the sorted list.

