class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest = float('inf')
        for price in prices:
            cheapest = min(cheapest, price)
            profit = price- cheapest
            max_profit= max(max_profit,profit)
        return max_profit