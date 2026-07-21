class Solution:
    def isValidSudoku(self, board: board[board[str]]) -> bool:        
        seen = set()

        for i in range(9):
            for j in range(9):
                if (board[i][j] != '.' ):
                    if (board[i][j] in seen):
                        return False
                    else:
                        seen.add(board[i][j])
            seen.clear()

        for i in range(9):
            for j in range(9):
                if (board[j][i] != '.' ):
                    if (board[j][i] in seen):
                        return False
                    else:
                        seen.add(board[j][i])
            seen.clear()
        seen_dict = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen_dict[(j // 3) * 3 + (i // 3)]:
                        return False
                    else:
                        seen_dict[(j // 3) * 3 + (i // 3)].add(board[i][j])
                        
        return True





        
        
        

        