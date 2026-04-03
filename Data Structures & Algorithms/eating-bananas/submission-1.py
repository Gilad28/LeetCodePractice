class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least = 1
        most = max(piles)
        leasthours = most

        while least <= most:
            k = (least + most) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                leasthours = k
                most = k - 1

            else:
                least = k + 1 

        return leasthours

        