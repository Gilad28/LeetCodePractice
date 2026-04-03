class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num,f in count.items():
            freq[f].append(num)
        
        out = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                out.append(num)
                if len(out) == k:
                    return out

        

        