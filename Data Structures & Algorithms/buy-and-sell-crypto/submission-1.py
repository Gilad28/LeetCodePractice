class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        curr = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                print(prices[r], prices[l])
                curr = max(prices[r] - prices[l], curr)
            
        return curr