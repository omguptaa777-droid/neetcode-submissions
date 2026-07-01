class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or self.timemap[key][0][1] > timestamp:
            return ""
        l = 0
        r = len(self.timemap[key]) - 1

        res = 0
        while l <= r:
            mid = (l+r)//2

            if self.timemap[key][mid][1] > timestamp:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        
        return self.timemap[key][res][0] 

