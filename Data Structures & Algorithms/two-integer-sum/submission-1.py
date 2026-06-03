class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        seen[nums[0]] = 0
        for i in range(1,len(nums)):
            rem = target - nums[i]
            if rem in seen:
                return [seen[rem],i]
            else:
                seen[nums[i]] = i
         