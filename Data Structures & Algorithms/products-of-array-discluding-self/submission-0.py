class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = [1] * len(nums)
        before = 1

        for num in range(len(nums)):
            count[num] = before
            before *= nums[num]

        after = 1
        for d in range(len(nums)-1, -1, -1):
            count[d] *= after
            after *= nums[d]
        
        return(count)


        