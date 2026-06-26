class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        days = 0
        n = len(self.stack)
        i = n-1
        while i >= 0 and self.stack[i] <= price:
            days += 1
            i -= 1
        return days




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)