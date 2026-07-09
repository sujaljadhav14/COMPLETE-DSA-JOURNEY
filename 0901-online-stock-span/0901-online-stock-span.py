class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        span=1
        while self.stack and price>=self.stack[-1][0]:
            oldprice, oldspan = self.stack.pop()
            span += oldspan
        self.stack.append((price,span))
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)