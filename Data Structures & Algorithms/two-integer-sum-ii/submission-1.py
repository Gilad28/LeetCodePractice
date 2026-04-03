class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        temp = ""
        while temp != target:
            temp = numbers[start] + numbers[end]
            
            if temp > target:
                end -= 1
            if temp < target:
                start += 1

        return [start+1,end+1]
        