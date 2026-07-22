class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap,(-dist,[x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _,points in heap:
            res.append(points)
        
        return res