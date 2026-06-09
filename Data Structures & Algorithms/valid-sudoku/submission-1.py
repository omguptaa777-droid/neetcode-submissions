class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(list)
        col = defaultdict(list)
        sq = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if val in row[r] or val in col[c] or val in sq[(r//3,c//3)]:
                    return False
                row[r].append(val)
                col[c].append(val)
                sq[(r//3,c//3)].append(val)
        
        return True