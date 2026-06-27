class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.heap = []
        self.idx = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.heap,(-self.freq[val],-self.idx,val))
        self.idx += 1

    def pop(self) -> int:
        _,_,val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()