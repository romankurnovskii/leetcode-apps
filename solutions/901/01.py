class StockSpanner:
    def __init__(self):
        self.stack = []  # Each element is a tuple (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _price, _span = self.stack.pop()
            span += _span
        self.stack.append([price, span])
        return span
