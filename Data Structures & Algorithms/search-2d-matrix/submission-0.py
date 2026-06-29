class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = m - 1

        while i <= j:
            mid = (i+j)//2

            if matrix[mid][n-1] < target:
                i = mid + 1

            elif matrix[mid][n-1] > target:
                if matrix[mid][0] <= target:
                    l = 0
                    r = n - 1

                    while l <= r:
                        c = (l+r)//2

                        if matrix[mid][c] < target:
                            l = c + 1
                        elif matrix[mid][c] > target:
                            r = c - 1
                        else:
                            return True  
                j = mid - 1 

            else:
                return True

        return False
        
