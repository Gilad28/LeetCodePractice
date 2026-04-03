class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_profit = 0

        for day in prices:
            if day - lowest_price > best_profit:
                best_profit = day - lowest_price
                
            if day < lowest_price:
                lowest_price = day
        return best_profit
            