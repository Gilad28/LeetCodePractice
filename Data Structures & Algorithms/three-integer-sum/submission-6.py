class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums)-1
            while start < end:
                ans = nums[i] + nums[start] + nums[end]
                if ans == 0:
                    out.append([nums[i],nums[start],nums[end]])
                    end -= 1
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1    

                if ans > 0:
                    end -= 1
                if ans < 0:
                    start += 1

        return out



        