class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        n = len(nums)
        if k == 0:
            return False
        q = deque()
        q.append(nums[0])
        while j < n:
            
            if j - i <= k:
                if nums[j] in q:
                    return True
                else:
                    q.append(nums[j])
                    j += 1
            else:
                q.popleft()
                i += 1
        return False 

        
