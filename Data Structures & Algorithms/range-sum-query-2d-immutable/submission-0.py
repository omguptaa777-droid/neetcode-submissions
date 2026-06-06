class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(self.matrix)):
            prefix = 0
            for j in range(len(self.matrix[0])):
                prefix += self.matrix[i][j]
                self.pre[i+1][j+1] = self.pre[i][j+1] + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.pre[row2+1][col2+1]
        above = self.pre[row1][col2+1]
        left = self.pre[row2+1][col1]
        top_left = self.pre[row1][col1]

        res = bottom_right - above - left + top_left
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)