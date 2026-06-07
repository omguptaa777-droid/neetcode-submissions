class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starting_elements = set()
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                starting_elements.add(num)
        ans = 0
        for num in starting_elements:
            i = 1
            while num + i in nums_set:
                i += 1
            ans = max(ans,i)
        return ans