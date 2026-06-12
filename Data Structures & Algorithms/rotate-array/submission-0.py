class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        i = 0
        j = n - k

        nums[:] = nums[j:] + nums[i:j]
        