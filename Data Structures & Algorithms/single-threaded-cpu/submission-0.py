class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []

        for i,task in enumerate(tasks):
            heapq.heappush(pending,[task[0],task[1],i])
        
        time = 0
        res = []

        while pending or available:
            while pending and pending[0][0] <= time:
                enqueTime,processingTime,idx = heapq.heappop(pending)
                heapq.heappush(available,[processingTime,idx])
            
            if not available:
                time = pending[0][0]
                continue
            
            processingTime,idx = heapq.heappop(available)
            time += processingTime
            res.append(idx)
            
        
        return res

        
        