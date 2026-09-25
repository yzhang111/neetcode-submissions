class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                if value in rows[r]:
                    return False
                rows[r].add(value)

                if value in cols[c]:
                    return False

                cols[c].add(value)

                box_row = r //3 
                box_col = c //3
                v = box_row * 3 + box_col

                if value in boxes[v]:
                    return False
                
                boxes[v].add(value)
        return True
                
                
        