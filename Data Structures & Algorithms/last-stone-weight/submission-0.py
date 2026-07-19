class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []

        for w in stones:
            heapq.heappush(heap,-w)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap,x-y)
        
        return -heap[0] if heap else 0