class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set()
        for num in nums:
            consec.add(num)

        print(consec)
        maxc = 0
        for num in consec:
            if num-1 not in consec:
                cur = num
                count = 1
                while cur+1 in consec:
                    cur += 1
                    count += 1
                maxc = max(count, maxc)

        return maxc
                