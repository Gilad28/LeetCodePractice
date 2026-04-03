class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        small = 1
        big = max(piles)

        while small <= big:
            k = (big + small) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours > h:
                small = k + 1
            
            else:
                best_k = k
                big = k - 1 
            
        return best_k
            

        