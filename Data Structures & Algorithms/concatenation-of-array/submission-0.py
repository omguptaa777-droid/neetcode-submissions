class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i < n:
            nums.append(nums[i])
            i += 1
        
        return nums