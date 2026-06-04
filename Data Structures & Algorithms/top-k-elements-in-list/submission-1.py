class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = Counter(nums)
        heap = []

        for num,freq in freq_cnt.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        ans = []
        for pair in heap:
            ans.append(pair[1])
        
        return ans