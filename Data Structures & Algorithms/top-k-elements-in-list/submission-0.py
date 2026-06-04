class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = dict(sorted(freq.items(),key=lambda x: x[1],reverse=True))
        ans = []
        for key,val in sorted_freq.items():
            if k == 0:
                break
            ans.append(key)
            k -= 1
        return ans