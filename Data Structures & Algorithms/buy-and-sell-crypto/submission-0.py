class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buy = prices[0]
        sell = 0
        profit = 0

        for i in range(1,n):
            if buy > prices[i]:
                buy = prices[i]
            else:
                sell = prices[i]
                profit = max(profit,sell-buy)
        return profit
