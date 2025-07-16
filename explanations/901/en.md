## 901. Online Stock Span [Medium]

https://leetcode.com/problems/online-stock-span

## Description
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the StockSpanner class:
- StockSpanner() Initializes the object of the class.
- int next(int price) Returns the span of the stock's price given that today's price is price.

## Examples

Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

## Constraints
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next.

## Hint
- We are interested in finding the span or reach back in time over consecutive elements that meet a certain criterion (in this case, previous stock prices that are less than or equal to the current day's price).
- A monotonic stack allows us to efficiently track and update spans as new prices come in, maintaining the necessary order of comparison and ensuring we can calculate each day's span in O(1) average time.

## Explanation

This problem is a classic application of the monotonic stack technique. We want to efficiently find, for each new price, how many consecutive previous days (including today) had prices less than or equal to today's price. By maintaining a stack of pairs (price, span), we can pop off all previous prices that are less than or equal to the current price, summing their spans, and push the current price and its total span. This allows each price to be processed in amortized O(1) time, making the solution efficient for large input sizes. 