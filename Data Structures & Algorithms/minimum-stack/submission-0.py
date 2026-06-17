class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt:
            self.minSt.append(val)
        else:
            if val < self.minSt[-1]:
                self.minSt.append(val)
            else:
                self.minSt.append(self.minSt[-1])

    def pop(self) -> None:
        if self.st:
            self.st = self.st[:-1]
            self.minSt = self.minSt[:-1]

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        if self.minSt:
            return self.minSt[-1]
