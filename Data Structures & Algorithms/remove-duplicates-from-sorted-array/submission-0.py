class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1
        
        return k 