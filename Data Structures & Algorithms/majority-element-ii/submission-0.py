class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        th = math.floor(n/3)
        arr = [0] * (max(nums) + 1)

        for num in nums:
            arr[num] += 1
        
        res = []
        for i,freq in enumerate(arr):
            if freq > th:
                res.append(i)
        
        return res
 