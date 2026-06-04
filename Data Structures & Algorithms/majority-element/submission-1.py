class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        f = defaultdict(int)

        for num in nums:
            f[num] += 1
        
        ans = 0
        freq = 0
        for k,v in f.items():
            if v > freq:
                freq = v
                ans = k
        
        return ans
        